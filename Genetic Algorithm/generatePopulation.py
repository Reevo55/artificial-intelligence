from Chromosome import *
import random
import copy

RANDOMIZER_SEED = 0.6
LENGTH_RANDOM_MAX = 4

def generateIndividual(plate):
    paths = []

    for connection in plate.connections:
        start = connection.start
        end = connection.end

        segments = createLutePath(start, end)

        path = Path(start, end, segments)
        paths.append(path)

    individual = Chromosome(paths)
    return individual

def checkOpposite(direction_1, direction_2):
    if (direction_1 == 'right' and direction_2 == 'left') or (direction_1 == 'left' and direction_2 == 'right'):
        return True
    if (direction_1 == 'up' and direction_2 == 'down') or (direction_1 == 'down' and direction_2 == 'up'):
        return True
    
    return False

def generatePopulation(populationNumber, plate):
    population = []

    for i in range(0, populationNumber):
        population.append(generateIndividual(plate))
    
    return population
    

def createLutePath(start, end):
    currPosition = Point(start.x, start.y)
    segments = []

    lastDirection = ''

    while not (currPosition.x == end.x and currPosition.y == end.y):
        if random.uniform(0, 1) < RANDOMIZER_SEED:
            length = random.randint(1, LENGTH_RANDOM_MAX)

            random_direction = random.randint(1, 5)

            x = currPosition.x
            y = currPosition.y

            if random_direction == 1:
                direction = 'right'
                currPosition.x = currPosition.x + length
            elif random_direction == 2:
                direction = 'left'
                currPosition.x = currPosition.x - length
            elif random_direction == 3:
                direction = 'down'
                currPosition.y = currPosition.y - length
            else:
                direction = 'up'
                currPosition.y = currPosition.y + length

            if not checkOpposite(lastDirection, direction):
                segment = Segment(direction, length)
                segments.append(segment)
                lastDirection = direction
            else:
                currPosition.x = x
                currPosition.y = y


        if currPosition.x != end.x:
            diffrence = currPosition.x - end.x
            length = random.randint(1, abs(diffrence))

            if diffrence < 0 :
                direction = 'right'
            else:
                length = -1 * length
                direction = 'left'

            if not checkOpposite(lastDirection, direction):
                currPosition.x = currPosition.x + length

                segment = Segment(direction, abs(length))
                segments.append(segment)
                lastDirection = direction

        if currPosition.y != end.y:
            diffrence = currPosition.y - end.y
            length = random.randint(1, abs(diffrence))

            if diffrence < 0 :
                direction = 'up'
            else:
                length = -1 * length
                direction = 'down'

            if not checkOpposite(lastDirection, direction):
                currPosition.y = currPosition.y + length

                segment = Segment(direction, abs(length))
                segments.append(segment)
                lastDirection = direction
    return segments


def connectTwoPoints(start, end):
    currPosition = Point(start.x, start.y)
    segments = []

    lastDirection = ''

    while not (currPosition.x == end.x and currPosition.y == end.y):
        if currPosition.x != end.x:
            diffrence = currPosition.x - end.x
            length = abs(diffrence)

            if diffrence < 0 :
                direction = 'right'
            else:
                length = -1 * length
                direction = 'left'

            if not checkOpposite(lastDirection, direction):
                currPosition.x = currPosition.x + length

                segment = Segment(direction, abs(length))
                segments.append(segment)
                lastDirection = direction

        if currPosition.y != end.y:
            diffrence = currPosition.y - end.y
            length = abs(diffrence)

            if diffrence < 0 :
                direction = 'up'
            else:
                length = -1 * length
                direction = 'down'

            if not checkOpposite(lastDirection, direction):
                currPosition.y = currPosition.y + length

                segment = Segment(direction, abs(length))
                segments.append(segment)
                lastDirection = direction
    return segments

def flattenSegments(segments):
    flattenSegments = []
    curr = segments[0]
    added = False

    for segm in segments[1:]:
        if curr.direction == segm.direction:
            curr.length += segm.length
            added = False
        else:
            flattenSegments.append(copy.deepcopy(curr))
            curr = segm
            added = True

    if not added:
        flattenSegments.append(copy.deepcopy(curr))

    return flattenSegments



