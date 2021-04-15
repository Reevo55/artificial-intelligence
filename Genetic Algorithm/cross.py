import copy
import random
from Chromosome import *

def cross(mother, father):
    cross_point = random.randint(0, len(mother.paths) - 1)
    return onePointCrossover(mother, father, cross_point)

def onePointCrossover(mother, father, cross_point):
    if cross_point >= len(mother.paths) or cross_point < 0: 
        raise ValueError("Cross_point must be smaller then path length and bigger then zero.")

    child_one_path = []
    child_two_path = []

    for i in range(0, len(mother.paths)): 
        if i <= cross_point:
            child_one_path.append(copy.deepcopy(mother.paths[i]))
            child_two_path.append(copy.deepcopy(father.paths[i]))
        else:
            child_one_path.append(copy.deepcopy(father.paths[i]))
            child_two_path.append(copy.deepcopy(mother.paths[i]))

    child_one = Chromosome(child_one_path)
    child_two = Chromosome(child_two_path)

    return child_one, child_two