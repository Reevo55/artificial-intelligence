from Problem import Problem
from Variable import Variable
from Constraints import *


class EinsteinProblem(Problem):
    VARIABLES_SIZE = 25

    def __init__(self):
        self.domain_length = 5
        self.set_variables = 0
        self._init()

    def check_constraints(self, variable, value):
        if self.category_contains(variable, value):
            return False

        previous_value = variable.value
        variable.value = value

        for constraint in self.constraints:
            if not constraint.check_constraint():
                variable.value = previous_value
                return False

        variable.value = previous_value

        return True

    def is_solved(self):
        return self.variables[-1].has_value()

    def save_solution(self):
        for variable in self.variables:
            print(variable)

        return False

    def set_variable(self, variable, value):
        variable.value = value

    def reset_variable(self, variable):
        variable.reset_value()
        self.set_variables -= 1

    def get_first_variable(self):
        return self.variables[0]

    def get_next_variable(self):
        if self.set_variables < len(self.variables) - 1:
            self.set_variables += 1

        return self.variables[self.set_variables]

    def category_contains(self, variable, value):
        def helper(index, value):
            if index >= 0 and index <= 4:
                start = 0
            elif index >= 5 and index <= 9:
                start = 5
            elif index >= 10 and index <= 14:
                start = 10
            elif index >= 15 and index <= 19:
                start = 15
            else:
                start = 20

            for i in range(start, start + 5):
                if self.variables[i].value == value:
                    return True

            return False

        # # #
        if value == -1:
            return False

        for i in range(0, len(self.variables)):
            if self.variables[i].name == variable.name:
                return helper(i, value)

    def _init(self):
        self.domain = [0, 1, 2, 3, 4]
        d = self.domain

        norwegian = Variable("Norwegian", d)
        dane = Variable("Dane", d)
        english = Variable("English", d)
        german = Variable("German", d)
        swede = Variable("Swede", d)

        yellow = Variable("Yellow", d)
        blue = Variable("Blue", d)
        red = Variable("Red", d)
        green = Variable("Green", d)
        white = Variable("White", d)

        water = Variable("Water", d)
        tea = Variable("Tea", d)
        milk = Variable("Milk", d)
        coffee = Variable("Coffee", d)
        beer = Variable("Beer", d)

        cigar = Variable("Cigar", d)
        light = Variable("Light", d)
        no_filter = Variable("No Filter", d)
        pipe = Variable("Pipe", d)
        mentol = Variable("Mentol", d)

        cat = Variable("Cat", d)
        horse = Variable("Horse", d)
        bird = Variable("Bird", d)
        fish = Variable("Fish", d)
        dog = Variable("Dog", d)

        self.variables = [
            norwegian,
            dane,
            english,
            german,
            swede,
            yellow,
            blue,
            red,
            green,
            white,
            water,
            tea,
            milk,
            coffee,
            beer,
            cigar,
            light,
            no_filter,
            pipe,
            mentol,
            cat,
            horse,
            bird,
            fish,
            dog,
        ]

        c1 = ValueConstraint(norwegian, 0)
        c2 = ValuesConstraintEqual(english, red)
        c3 = ValuesConstraintLeft(green, white)
        c4 = ValuesConstraintEqual(dane, tea)
        c5 = ValuesConstraintNext(light, cat)
        c6 = ValuesConstraintEqual(yellow, cigar)
        c7 = ValuesConstraintEqual(german, pipe)
        c8 = ValueConstraint(milk, 2)
        c9 = ValuesConstraintNext(light, water)
        c10 = ValuesConstraintEqual(no_filter, bird)
        c11 = ValuesConstraintEqual(swede, dog)
        c12 = ValuesConstraintNext(norwegian, blue)
        c13 = ValuesConstraintNext(horse, yellow)
        c14 = ValuesConstraintEqual(mentol, beer)
        c15 = ValuesConstraintEqual(green, coffee)

        self.constraints = {
            c1,
            c2,
            c3,
            c4,
            c5,
            c6,
            c7,
            c8,
            c9,
            c10,
            c11,
            c12,
            c13,
            c14,
            c15,
        }
