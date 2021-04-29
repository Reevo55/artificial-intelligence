from Problem import Problem
from Variable import Variable
from Constraints import *
import copy


class EinsteinProblem(Problem):
    VARIABLES_SIZE = 25

    def __init__(self, variable_choser, value_choser):
        self.solutions = []
        self.variables = []
        self.constraints = []
        self.set_variables = 0
        self.domain_length = 5
        self.variable_choser = variable_choser
        self.value_choser = value_choser
        self._init()

    def is_solved(self):
        return len(self.variables) == self.set_variables

    def category_constraint(self, v1, v2, v3, v4, v5):
        c1 = ValuesConstraintNotEqual(v1, v2)
        c2 = ValuesConstraintNotEqual(v1, v3)
        c3 = ValuesConstraintNotEqual(v1, v4)
        c4 = ValuesConstraintNotEqual(v1, v5)
        c5 = ValuesConstraintNotEqual(v2, v3)
        c6 = ValuesConstraintNotEqual(v2, v4)
        c7 = ValuesConstraintNotEqual(v2, v5)
        c8 = ValuesConstraintNotEqual(v3, v4)
        c9 = ValuesConstraintNotEqual(v3, v5)
        c10 = ValuesConstraintNotEqual(v4, v5)

        c = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

        self.constraints = self.constraints + c

    def save_solution(self):
        if self.solutions == []:
            self.solutions = copy.deepcopy(self.variables)

    def print_solutions(self):
        print("===============SOLUTION=================")
        for s in self.solutions:
            print(s)

    def _init(self):
        self.domain = [0, 1, 2, 3, 4]
        d = self.domain

        norwegian = Variable("Norwegian", [0])
        dane = Variable("Dane", d)
        english = Variable("English", d)
        german = Variable("German", d)
        swede = Variable("Swede", d)
        self.category_constraint(norwegian, dane, english, german, swede)

        yellow = Variable("Yellow", d)
        blue = Variable("Blue", d)
        red = Variable("Red", d)
        green = Variable("Green", d)
        white = Variable("White", d)
        self.category_constraint(yellow, blue, red, green, white)

        water = Variable("Water", d)
        tea = Variable("Tea", d)
        milk = Variable("Milk", [2])
        coffee = Variable("Coffee", d)
        beer = Variable("Beer", d)
        self.category_constraint(water, tea, milk, coffee, beer)

        cigar = Variable("Cigar", d)
        light = Variable("Light", d)
        no_filter = Variable("No Filter", d)
        pipe = Variable("Pipe", d)
        mentol = Variable("Mentol", d)
        self.category_constraint(cigar, light, no_filter, pipe, mentol)

        cat = Variable("Cat", d)
        horse = Variable("Horse", d)
        bird = Variable("Bird", d)
        fish = Variable("Fish", d)
        dog = Variable("Dog", d)
        self.category_constraint(cat, horse, bird, fish, dog)

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

        c2 = ValuesConstraintEqual(english, red)
        c3 = ValuesConstraintLeft(green, white)
        c4 = ValuesConstraintEqual(dane, tea)
        c5 = ValuesConstraintNext(light, cat)
        c6 = ValuesConstraintEqual(yellow, cigar)
        c7 = ValuesConstraintEqual(german, pipe)
        c9 = ValuesConstraintNext(light, water)
        c10 = ValuesConstraintEqual(no_filter, bird)
        c11 = ValuesConstraintEqual(swede, dog)
        c12 = ValuesConstraintNext(norwegian, blue)
        c13 = ValuesConstraintNext(horse, yellow)
        c14 = ValuesConstraintEqual(mentol, beer)
        c15 = ValuesConstraintEqual(green, coffee)

        self.constraints = self.constraints + [
            c2,
            c3,
            c4,
            c5,
            c6,
            c7,
            c9,
            c10,
            c11,
            c12,
            c13,
            c14,
            c15,
        ]
