class Chromosome:
    def __init__(self, paths):
        self.paths = paths

    def __str__(self):
        return f'Path: {self.paths} \n'

    def __repr__(self):
        return f'Path: {self.paths} \n'

class Path:
    segments = []

    def __init__(self, start, end, segments):
        self.start = start
        self.end = end
        self.segments = segments

    def __str__(self):
        return f'Path start: {self.start}, end: {self.end}, \n segments: {self.segments} \n'
    
    def __repr__(self):
        return f'Path start: {self.start}, end: {self.end}, \n segments: {self.segments} \n'

    
class Segment:
    direction = ''
    length = ''

    def __init__(self, direction, length):
        self.direction = direction
        self.length = length

    def __str__(self):
        return f'Segment direction: {self.direction}, length: {self.length}'

    def __repr__(self):
        return f'Segment direction: {self.direction}, length: {self.length}'

class Direction: 
    def __init__(self, direction):
        if direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down':
            self.direction = direction
        else:
            raise ValueError('Direction does not match standard')

    def __str__(self):
        return f'{self.direction}'
    def __repr__(self):
        return f'{self.direction}'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash((self.x, self.y))