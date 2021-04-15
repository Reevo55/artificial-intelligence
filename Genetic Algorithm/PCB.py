class PCB:
    def __init__(self, width, height, connections):
        self.width = width
        self.height = height
        self.connections = connections

    def __str__(self):
        return f'PCB width X = {self.width}, height X = {self.height}, connections = {self.connections} \n'

    def __repr__(self):
        return f'PCB width X = {self.width}, height X = {self.height}, connections = {self.connections} \n'

class Connection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def setPath(self, path):
        self.path = path
    
    def getPath(self):
        return self.path

    def __str__(self):
        return f'Connection start = {self.start}, end = {self.end}'

    def __repr__(self):
        return f'Connection start = {self.start}, end = {self.end}'
