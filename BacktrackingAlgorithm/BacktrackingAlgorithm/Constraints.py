from abc import ABC, abstractmethod


class Constraint(ABC):
    variable_1 = None

    def check_constraint(self):
        pass


class ValueConstraint(Constraint):
    def __init__(self, variable, value):
        self.variable_1 = variable
        self.value = value

    def check_constraint(self):
        return self.variable_1.value == self.value or not self.variable_1.has_value()


class ValuesConstraint(Constraint):
    def __init__(self, variable_1, variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2

    def check_values(self):
        return not self.variable_1.has_value() or not self.variable_2.has_value()


class ValuesConstraintEqual(ValuesConstraint):
    def check_constraint(self):
        return self.variable_1.value == self.variable_2.value or self.check_values()


class ValuesConstraintNotEqual(ValuesConstraint):
    def check_constraint(self):
        return self.variable_1.value != self.variable_2.value or self.check_values()


class ValuesConstraintNext(ValuesConstraint):
    def check_constraint(self):
        return (
            self.variable_1.value - self.variable_2.value == 1
            or self.variable_2.value - self.variable_1.value == 1
            or self.check_values()
        )


class ValuesConstraintLeft(ValuesConstraint):
    def check_constraint(self):
        return self.variable_2.value - self.variable_1.value == 1 or self.check_values()
