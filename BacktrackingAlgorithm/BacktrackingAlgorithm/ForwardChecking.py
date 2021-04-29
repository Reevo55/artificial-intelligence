from Problem import Problem
from Variable import Variable
from timingFunc import timing
from ValueChoser import NOTHING_RETURNED
import copy


class ForwardChecking:
    def __init__(self, problem):
        self.problem = problem
        self.counter_nodes = 0

    def save_domain_states(self, domain_states):
        for i in range(len(self.problem.variables)):
            variable = self.problem.variables[i]
            domain_states.append(variable.domain)

    def restore_domain_states(self, domain_states):
        for i in range(len(self.problem.variables)):
            variable = self.problem.variables[i]
            variable.domain = domain_states[i]

    def clear_domains(self, variable, value):
        for i in range(len(self.problem.constraints)):
            c = self.problem.constraints[i]

            v1 = c.variable_1
            v2 = c.variable_2

            if (v1.name == variable.name) and not v2.has_value():
                c.clear_domain(v2, value)

            elif (v2.name == variable.name) and not v1.has_value():
                c.clear_domain(v1, value)

    @timing
    def solve_all(self):
        self.counter_nodes = 0

        def solve_rec(variable):

            if self.problem.is_solved():
                self.problem.save_solution()
                return

            used_values = []
            value = self.problem.get_next_value(variable, used_values)

            while value != NOTHING_RETURNED:
                self.counter_nodes += 1
                used_values.append(value)
                domain_states = []

                self.save_domain_states(domain_states)
                self.clear_domains(variable, value)

                self.problem.set_variable(variable, value)

                solve_rec(self.problem.get_next_variable())

                self.problem.reset_variable(variable)
                self.restore_domain_states(domain_states)
                variable.remove_from_domain([value])

                value = self.problem.get_next_value(variable, used_values)

        solve_rec(self.problem.get_first_variable())
        return self.counter_nodes

    @timing
    def solve_one(self):
        self.counter_nodes = 0

        def solve_rec(variable):
            self.counter_nodes += 1
            if self.problem.is_solved():
                self.problem.save_solution()
                return True

            used_values = []
            value = self.problem.get_next_value(variable, used_values)

            while value != NOTHING_RETURNED:
                used_values.append(value)
                domain_states = []

                self.save_domain_states(domain_states)
                self.clear_domains(variable, value)

                self.problem.set_variable(variable, value)

                if solve_rec(self.problem.get_next_variable()):
                    return True

                self.problem.reset_variable(variable)
                self.restore_domain_states(domain_states)
                variable.remove_from_domain([value])

                value = self.problem.get_next_value(variable, used_values)

        solve_rec(self.problem.get_first_variable())
        return self.counter_nodes
