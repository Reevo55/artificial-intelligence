from Problem import Problem
from Variable import Variable
from timingFunc import timing


class Backtracking:
    def __init__(self, problem):
        self.problem = problem

    @timing
    def solve(self):
        def solve_rec(variable):
            if self.problem.is_solved():
                if self.problem.save_solution():
                    return False
                else:
                    return True

            for value in variable.domain:
                if self.problem.check_constraints(variable, value):
                    self.problem.set_variable(variable, value)

                    if solve_rec(self.problem.get_next_variable()):
                        return True

                    self.problem.reset_variable(variable)

            return False

        # # #
        solve_rec(self.problem.get_first_variable())
        self.problem.print()
