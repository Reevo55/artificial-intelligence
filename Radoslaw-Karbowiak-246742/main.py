from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulation, generateIndividual
from evaluate import *
from Chromosome import *
from timingFunc import timing
from cross import onePointCrossover, cross
from mutation import *
from evolutionaryAlgorithm import evolutionaryAlgorithm
from selectorMethods import *

import time

POPULATION_NUMBER = 50
METHOD_ITERATIONS = 40

plates = loadDataPCBs()
plate = plates[1]

bestIndividual = evolutionaryAlgorithm(plate, POPULATION_NUMBER, METHOD_ITERATIONS, 20)

print("=================BEST INDIVIDUAL=========================")
print(bestIndividual)
print(evaluate(bestIndividual, plate))
print(printSums(bestIndividual, plate))


@timing
def randomMethod(plate, iterations):
    bestIndividual = ''
    bestIndividualScore = 99999

    for i in range(0, iterations):
        print('Evaluating...')
        randIndividual = generateIndividual(plate)
        randIndividualScore = evaluate(randIndividual, plate)

        if bestIndividualScore > randIndividualScore:
            bestIndividual = randIndividual
            bestIndividualScore = randIndividualScore

    print('====================================================')
    print('Best individual score: ' + str(bestIndividualScore))
    print('====================================================')
    return bestIndividual

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




