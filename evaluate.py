from Chromosome import *    
import copy

W_SEGMENTS = 1
W_LENGTH = 2
W_OUTSIDERS = 20
W_INTERSECTION = 15



def sumOfSegments(individual):
    sum = 0
    lastDirection = ''

    for path in individual.paths:
        for segment in path.segments:
            if segment.direction != lastDirection:
                sum += 1
                lastDirection = segment.direction
    
    return sum

def sumOfLengths(individual):
    sum = 0

    for path in individual.paths:
        for segment in path.segments:
            sum += segment.length

    return sum
        
def sumOfIntersections(individual):
    intersections = 0
    points = set()
    pArr = []

    for path in individual.paths:
        if path.start in points:
            intersections += 1
        
        points.add(path.start)
        pArr.append(path.start)
        currPoint = Point(path.start.x, path.start.y)

        pointsArr = []
        segmentsPoints = segmentsToPoints(currPoint, path.segments)
        pointsArr.extend(segmentsPoints)
        
        for point in pointsArr:
            if point in points:
                intersections += 1

            points.add(point)

        pArr.extend(pointsArr)

    return intersections

def sumOfOutsiders(individual, plate):
    pointsArr = []
    sumOfOutsiders = 0

    for path in individual.paths:
        pointsArr.append(path.start)

        currPoint = Point(path.start.x, path.start.y)
        segmentsPoints = segmentsToPoints(currPoint, path.segments)
        
        pointsArr.extend(segmentsPoints)
    
    for point in pointsArr:
        if point.x < 0 or point.x >= plate.width:
            sumOfOutsiders += 1
        if point.y < 0 or point.y >= plate.height:
            sumOfOutsiders += 1

    return sumOfOutsiders 

def segmentsToPoints(currPoint, segments):
    points = []
    for segment in segments:
        segmentPoints = lengthToPoints(currPoint, segment.length, segment.direction)
        points.extend(segmentPoints)

    return points
                
def lengthToPoints(currPoint, length, direction):
    points = []

    for i in range(0, length):
        if direction == 'right':
            currPoint.x = currPoint.x + 1            
        elif direction == 'left':
            currPoint.x = currPoint.x - 1
        elif direction == 'up':
            currPoint.y = currPoint.y + 1
        else:
            currPoint.y = currPoint.y - 1
        
        points.append(copy.deepcopy(currPoint))
    
    return points

def evaluate(individual, plate):
    sumOfS = sumOfSegments(individual)
    sumOfL = sumOfLengths(individual)
    sumOfO = sumOfOutsiders(individual, plate)
    sumOfI = sumOfIntersections(individual)

    sum = 0
    sum += W_SEGMENTS * sumOfS
    sum += W_LENGTH * sumOfL
    sum += W_OUTSIDERS * sumOfO
    sum += W_INTERSECTION * sumOfI

    return sum

def printSums(individual, plate):
    sumOfS = sumOfSegments(individual)
    sumOfL = sumOfLengths(individual)
    sumOfO = sumOfOutsiders(individual, plate)
    sumOfI = sumOfIntersections(individual)

    print('Sum of segments: ' + str(sumOfS))
    print('Sum of length: ' + str(sumOfL))
    print('Sum of outsiders: ' + str(sumOfO))
    print('Sum of intersections: ' + str(sumOfI))
    
def getPointsFromSegments(individual, plate):
    pArr = []

    for path in individual.paths:
        currArr = []

        currArr.append(path.start)
        currPoint = Point(path.start.x, path.start.y)

        segmentsPoints = segmentsToPoints(currPoint, path.segments)

        currArr.extend(segmentsPoints)
        pArr.append(currArr)

    return pArr