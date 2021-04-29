class Variable:
    DEFAULT_VALUE = -1

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.value = self.DEFAULT_VALUE

    def has_value(self):
        return self.value != self.DEFAULT_VALUE

    def reset_value(self):
        self.value = self.DEFAULT_VALUE

    def has_value_domain(self):
        return len(self.domain) != 0

    def remove_from_domain(self, domain_values):
        if len(self.domain) == 0:
            return

        filtered_domain = []

        for d in self.domain:
            for v in domain_values:
                if d != v:
                    filtered_domain.append(d)
                    break

        self.domain = filtered_domain

    def __repr__(self):
        return f"Name: {self.name}, Domain: {self.domain}, Value: {self.value} \n"

    def __eq__(self, other):
        return self.name == other.name
