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

    def __repr__(self):
        return f"Name: {self.name}, Domain: {self.domain}, Value: {self.value} \n"
