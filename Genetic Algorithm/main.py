from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulation, generateIndividual
from evaluate import *
from Chromosome import *
from timingFunc import timing
from cross import onePointCrossover, cross
from mutation import *
from evolutionaryAlgorithm import evolutionaryAlgorithm, randomMethod
from selectorMethods import *
from visualisation import draw_plots
import time

POPULATION_NUMBER = 100
METHOD_ITERATIONS = 200


plates = loadDataPCBs()
plate = plates[4] 
# plate = plates[1]


bestIndividual = evolutionaryAlgorithm(plate, POPULATION_NUMBER, METHOD_ITERATIONS, 15)
bestIndividualRandom = randomMethod(plate, METHOD_ITERATIONS)

print("=================BEST INDIVIDUAL=========================")
print(bestIndividual)
print(evaluate(bestIndividual, plate))
print(printSums(bestIndividual, plate))
draw_plots(getPointsFromSegments(bestIndividual), (plate.width, plate.height))

print("=================BEST INDIVIDUAL random=========================")
print(bestIndividualRandom)
print(evaluate(bestIndividualRandom, plate))
print(printSums(bestIndividualRandom, plate))
draw_plots(getPointsFromSegments(bestIndividualRandom), (plate.width, plate.height))

# bestIndividual = randomMethod(plate, METHOD_ITERATIONS)

# print('Best individual: ')
# print(bestIndividual)
# printSums(bestIndividual, plate)


# arrOfPoints = getPointsFromSegments(bestIndividual, plate)


# GENERATE POPULATION

# population = generatePopulation(POPULATION_NUMBER, plate)

# print('======================MOTHER ROULETTE================')
# mother = roulette(population, plate)
# print(mother)

# print('=====================FATHER TOURNAMENT===========================')
# father = tournament(population, plate)
# print(father)

# mutation(mother)




