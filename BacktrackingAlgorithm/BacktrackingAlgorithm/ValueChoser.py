from abc import ABC, abstractmethod
from Constraints import *
import copy

NOTHING_RETURNED = -999


class ValueChooser:
    @abstractmethod
    def get_next_value(self, current_var, constraints, used_values):
        pass


class NextValueChooser(ValueChooser):
    def get_next_value(self, current_var, constraints, used_values):
        if current_var is None:
            return NOTHING_RETURNED

        if len(used_values) == 0:
            current_val = -1
        else:
            current_val = used_values[-1]

        domain = current_var.domain

        for i in range(len(domain)):
            if domain[i] == current_val:
                if i + 1 < len(domain):
                    return domain[i + 1]
            elif domain[i] > current_val:
                return domain[i]

        return NOTHING_RETURNED


class LeastConstrainedValueChooser(ValueChooser):
    def sum_constrained(self, var, binaryConstraint):
        constrained = 0
        if not var.has_value():
            for v in var.domain:
                var.value = v

                if binaryConstraint.check_constraint():
                    constrained += 1

                var.reset_value()

        return constrained

    def calculate_constrained(self, binaryConstraint, current_var):
        constrained = 0

        v1 = binaryConstraint.variable_1
        v2 = binaryConstraint.variable_2

        if v1 == current_var:
            constrained += self.sum_constrained(v2, binaryConstraint)
        elif v2 == current_var:
            constrained += self.sum_constrained(v1, binaryConstraint)

        return constrained

    def get_next_value(self, current_var, constraints, used_values):
        domain = current_var.domain

        max_constrained = -1
        result = NOTHING_RETURNED

        for val in domain:
            if val in used_values:
                continue

            current_var.value = val
            constrained = 0

            for c in constraints:
                constrained += self.calculate_constrained(c, current_var)

            if constrained > max_constrained:
                max_constrained = constrained
                result = val

        current_var.reset_value()

        return result