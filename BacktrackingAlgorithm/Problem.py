from abc import ABC, abstractmethod
from Variable import Variable
from Constraints import *


class Problem(ABC):
    solutions = []
    variables = []
    constraints = []

    @abstractmethod
    def check_constraints(self, variable, value):
        pass

    @abstractmethod
    def is_solved(self):
        pass

    @abstractmethod
    def set_variable(self, variable, value):
        pass

    @abstractmethod
    def reset_variable(self, variable):
        pass

    @abstractmethod
    def get_first_variable(self):
        pass

    @abstractmethod
    def get_next_variable(self):
        pass

    def save_solution(self):
        solution = []
        for v in self.variables:
            solution.append(v)

        if self.check_duplicate(solution):
            return False

        self.solutions.append(solution)
        return True

    def check_duplicate(self, solution):
        for s in self.solutions:
            is_duplicate = True
            for i in range(len(s)):
                if solution[i].name != s[i].name and solution[i].value != s[i].value:
                    is_duplicate = False
                    break

            if is_duplicate:
                return True

        return False

    def print(self):
        print("===============SOLVED=================")
        for s in self.solutions:
            print("Solution: ")

            print(s)
