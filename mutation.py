import copy
import random
from generatePopulation import connectTwoPoints
from Chromosome import *
from evaluate import evaluate

def mutation(individual):
    return mutatePath(random.choice(individual.paths), 0)

def mutatePath(path, segmentId):
    if segmentId <= len(path.segments) - 3 and segmentId >= 0:
        random_segment = path.segments[segmentId]
    else:
        return;

    first_segment = random_segment
    third_segment = path.segments[segmentId + 2]

    first_segment.length += 1

    if first_segment.direction == 'right':
        if third_segment.direction == 'right':
            third_segment.length -= 1
        elif third_segment.direction == 'left':
            third_segment.length += 1
    elif first_segment.direction == 'left':
        if third_segment.direction == 'right':
            third_segment.length += 1
        elif third_segment.direction == 'left':
            third_segment.length -= 1
    elif first_segment.direction == 'up':
        if third_segment.direction == 'up':
            third_segment.length += 1
        elif third_segment.direction == 'down':
            third_segment.length -= 1
    elif first_segment.direction == 'down':
        if third_segment.direction == 'up':
            third_segment.length -= 1
        elif third_segment.direction == 'down':
            third_segment.length += 1   





