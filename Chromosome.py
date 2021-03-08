class Chromosome:
    def __init__(self, paths):
        self.paths = paths

    def __str__(self):
        return f'Path: {self.paths}, Width: {self.width}, Height: {self.height}'

    def __repr__(self):
        return f'Path: {self.paths}, Width: {self.width}, Height: {self.height}'

class Path:
    segments = []

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Path start: {self.start}, end: {self.end}, segments: {self.segments}'
    
    def __repr__(self):
        return f'Path start: {self.start}, end: {self.end}, segments: {self.segments}'

    
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