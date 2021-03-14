import copy
import random
from Chromosome import *

def onePointCrossover(mother, father):
    print("Length of paths: " + str(len(mother.paths)))
    cross_point = random.randint(1, len(mother.paths) - 2)

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