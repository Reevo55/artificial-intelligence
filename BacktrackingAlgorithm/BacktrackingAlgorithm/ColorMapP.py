from Problem import Problem
from Constraints import *
from Variable import Variable
import random
import copy
import math


class MapProblem(Problem):
    domain = []
    points = []
    edges = []
    points = []

    def __init__(
        self,
        x_size,
        y_size,
        variable_length,
        domain_length,
        variable_choser,
        value_choser,
    ):
        self.solutions = []
        self.variables = []
        self.constraints = []
        self.points = []
        self.domain = []
        self.edges = []
        self.set_variables = 0
        self.variable_choser = None
        self.value_choser = None
        self.variable_length = variable_length
        self.domain_length = domain_length
        self.set_variables = 0
        self.x_size = x_size
        self.y_size = y_size
        self.variable_choser = variable_choser
        self.value_choser = value_choser

        for i in range(domain_length):
            self.domain.append(i)

        self.generate_map_problem()

    def generate_map_problem(self):
        self.create_points(self.variable_length)
        self.create_edges()

    def create_points(self, variable_length):
        while variable_length > 0:
            x = random.randint(0, self.x_size)
            y = random.randint(0, self.y_size)
            created_point = Point(x, y)

            if not self.check_point_exists(created_point):
                self.points.append(created_point)
                self.variables.append(
                    Variable(self.create_var_name(created_point), self.domain)
                )
                variable_length -= 1

    def create_var_name(self, point):
        return "(" + str(point.x) + ", " + str(point.y) + ")"

    def create_edges(self):
        while True:
            attempt = 0
            help_points = copy.deepcopy(self.points)

            while attempt < len(self.points):
                chosen_point = help_points[random.randint(0, len(help_points) - 1)]
                closest_point = self.find_closest_point(chosen_point)

                if closest_point.x != -1:
                    self.create_edge(chosen_point, closest_point)
                    break

                help_points.remove(chosen_point)
                attempt += 1

            if attempt < len(self.points) - 1:
                continue

            break

    def create_edge(self, point_1, point_2):
        self.edges.append(Edge(point_1, point_2))
        variable_1 = self.find_variable_by_name(self.create_var_name(point_1))
        variable_2 = self.find_variable_by_name(self.create_var_name(point_2))
        self.constraints.append(ValuesConstraintNotEqual(variable_1, variable_2))

    def find_variable_by_name(self, name):
        for v in self.variables:
            if v.name == name:
                return v

    def check_point_exists(self, point):
        for p in self.points:
            if p == point:
                return True

        return False

    def is_solved(self):
        return len(self.variables) == self.set_variables

    def print_map(self):
        print("=====================================")
        print("Points: ")

        for p in self.points:
            print(p)

        print("=====================================")
        print("Edges: ")

        for e in self.edges:
            print(e)

    def find_closest_point(self, point):
        closest_point = Point(-1, -1)
        distance = 999999

        for i in range(len(self.points)):
            candidate = self.points[i]

            if (
                candidate == point
                or self.check_if_connected(candidate, point)
                or self.check_if_intersects(candidate, point)
            ):
                continue

            help_distance = self.calculate_distance(candidate, point)

            if help_distance < distance:
                distance = help_distance
                closest_point = candidate

        return closest_point

    def check_if_intersects(self, point_1, point_2):
        for e in self.edges:
            if self.is_intersecting(point_1, point_2, e.p1, e.p2):
                return True

        return False

    def check_if_connected(self, point_1, point_2):
        for e in self.edges:
            p1 = e.p1
            p2 = e.p2

            if (p1 == point_1 and p2 == point_2) or (p1 == point_2 and p2 == point_1):
                return True

        return False

    def is_intersecting(self, p1, q1, p2, q2):
        if p1 == p2 or p1 == q2 or q1 == p2 or q1 == q2:
            return False

        o1 = self.orient(p1, q1, p2)
        o2 = self.orient(p1, q1, q2)
        o3 = self.orient(p2, q2, p1)
        o4 = self.orient(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and self.is_on_edge(p1, p2, q1):
            return True
        if o2 == 0 and self.is_on_edge(p1, q2, q1):
            return True
        if o3 == 0 and self.is_on_edge(p2, p1, q2):
            return True
        if o4 == 0 and self.is_on_edge(p2, q1, q2):
            return True

        return False

    def orient(self, p1, p2, p3):
        value = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

        if value == 0:
            return 0
        elif value > 0:
            return 1
        else:
            return 2

    def calculate_distance(self, p1, p2):
        pow_x = (p1.x - p2.x) * (p1.x - p2.x)
        pow_y = (p1.y - p2.y) * (p1.y - p2.y)

        return math.sqrt(pow_x + pow_y)

    def is_on_edge(self, p1, p2, p3):
        if (
            p2.x <= max(p1.x, p3.x)
            and p2.y <= max(p2.y, p3.y)
            and p2.x >= max(p1.x, p3.x)
            and p2.y >= max(p1.y, p3.y)
        ):
            return True

        return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point x = {self.x}, y = {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Point 1: [{self.p1}], Point 2: [{self.p2}]"
