from Problem import Problem
from Variable import Variable
from timingFunc import timing


class Backtracking:
    def __init__(self, problem):
        self.problem = problem
        self.counter_nodes = 0

    @timing
    def solve_all(self):
        self.counter_nodes = 0

        def solve_rec(variable):
            if variable is None:
                return False

            if self.problem.is_solved():
                self.problem.save_solution()
                return False

            for value in variable.domain:
                self.counter_nodes += 1
                if self.problem.check_constraints(variable, value):
                    self.problem.set_variable(variable, value)

                    if solve_rec(self.problem.get_next_variable()):
                        return True

                    self.problem.reset_variable(variable)

            return False

        # # #
        solve_rec(self.problem.get_first_variable())
        # self.problem.print_solutions()
        return self.counter_nodes

    @timing
    def solve_one(self):
        self.counter_nodes = 0

        def solve_rec(variable):
            if self.problem.is_solved():
                self.problem.save_solution()
                return True

            for value in variable.domain:
                self.counter_nodes += 1
                if self.problem.check_constraints(variable, value):
                    self.problem.set_variable(variable, value)

                    if solve_rec(self.problem.get_next_variable()):
                        return True

                    self.problem.reset_variable(variable)

            return False

        # # #
        solve_rec(self.problem.get_first_variable())
        # self.problem.print_solutions()
        return self.counter_nodes
