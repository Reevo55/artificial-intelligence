from abc import ABC, abstractmethod


class VariableChoser:
    @abstractmethod
    def get_next_variable(self, variables):
        pass


class NextVariableChooser(VariableChoser):
    def get_next_variable(self, variables):
        for var in variables:
            if not var.has_value():
                return var

        return None


class MostConstrainedVariableChooser(VariableChoser):
    def get_next_variable(self, variables):
        smallest_domain = 99999
        next_variable = None

        for v in variables:
            if v.has_value():
                continue

            if len(v.domain) < smallest_domain:
                smallest_domain = len(v.domain)
                next_variable = v

        return next_variable