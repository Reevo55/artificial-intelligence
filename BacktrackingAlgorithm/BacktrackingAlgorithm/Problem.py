from abc import ABC, abstractmethod
from Variable import Variable
from Constraints import *
from ValueChoser import *
from VariableChoser import *
import copy


class Problem(ABC):
    solutions = []
    variables = []
    constraints = []
    set_variables = 0
    variable_choser = None
    value_choser = None

    def check_constraints(self, variable, value):
        previous_value = variable.value
        variable.value = value

        for constraint in self.constraints:
            if not constraint.check_constraint():
                variable.value = previous_value
                return False

        variable.value = previous_value

        return True

    @abstractmethod
    def is_solved(self):
        pass

    def set_variable(self, variable, value):
        variable.value = value
        self.set_variables += 1

    def reset_variable(self, variable):
        variable.reset_value()
        self.set_variables -= 1

    def save_solution(self):
        self.solutions.append(copy.deepcopy(self.variables))

    def print_solutions(self):
        for solution in self.solutions:
            print("SOLUTION")
            for variable in solution:
                print(variable)

    def get_next_value(self, variable, used_values):
        return self.value_choser.get_next_value(variable, self.constraints, used_values)

    def get_next_variable(self):
        return self.variable_choser.get_next_variable(self.variables)

    def get_first_variable(self):
        return self.variables[0]