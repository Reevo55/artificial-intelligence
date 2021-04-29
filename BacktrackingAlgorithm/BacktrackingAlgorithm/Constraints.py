from abc import ABC, abstractmethod
import copy


class Constraint(ABC):
    variable_1 = None
    variable_2 = None

    def check_constraint(self):
        pass

    def clear_domain(self, variable, value):
        pass


# class ValueConstraint(Constraint):
#     def __init__(self, variable, value):
#         self.variable_1 = variable
#         self.value = value

#     def check_constraint(self):
#         return self.variable_1.value == self.value or not self.variable_1.has_value()

#     def clear_domain(self, variable, value):
#         pass


class ValuesConstraint(Constraint):
    def __init__(self, variable_1, variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2

    def check_values(self):
        return not self.variable_1.has_value() or not self.variable_2.has_value()


class ValuesConstraintEqual(ValuesConstraint):
    def check_constraint(self):
        return self.variable_1.value == self.variable_2.value or self.check_values()

    def clear_domain(self, variable, value):
        domain = variable.domain

        filtered_domain = []

        if len(domain) == 0:
            return

        for d in domain:
            if d == value:
                filtered_domain.append(d)

        variable.domain = filtered_domain


class ValuesConstraintNotEqual(ValuesConstraint):
    def check_constraint(self):
        return self.variable_1.value != self.variable_2.value or self.check_values()

    def clear_domain(self, variable, value):
        variable.remove_from_domain([value])


class ValuesConstraintNext(ValuesConstraint):
    def check_constraint(self):
        return (
            self.variable_1.value - self.variable_2.value == 1
            or self.variable_2.value - self.variable_1.value == 1
            or self.check_values()
        )

        def clear_domain(self, variable, value):
            domain = variable.domain

            filtered_domain = []

            if len(domain) == 0:
                return

            for d in domain:
                if not (d == value - 1 or d == value + 1):
                    filtered_domain.append(d)

            if not filtered_domain == []:
                variable.domain = filtered_domain


class ValuesConstraintLeft(ValuesConstraint):
    def check_constraint(self):
        return self.variable_2.value - self.variable_1.value == 1 or self.check_values()

    def clear_domain(self, variable, value):
        domain = variable.domain

        filtered_domain = []

        if len(domain) == 0:
            return

        for d in domain:
            if d == value - 1:
                filtered_domain.append(d)

        if not filtered_domain == []:
            variable.domain = filtered_domain
