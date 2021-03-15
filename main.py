from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulation, generateIndividual
from evaluate import *
from selectors import roulette, tournament
from Chromosome import *
from timingFunc import timing
from cross import onePointCrossover, cross
from visualisation import draw_plots
import time

POPULATION_NUMBER = 5
RANDOM_METHOD_ITERATIONS = 100000

plates = loadDataPCBs()
plate = plates[1]

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

# bestIndividual = randomMethod(plate6x6, RANDOM_METHOD_ITERATIONS)
# print('Best individual: ')
# print(bestIndividual)

# printSums(bestIndividual, plate)

# arrOfPoints = getPointsFromSegments(bestIndividual, plate)

# draw_plots(getPointsFromSegments(bestIndividual, plate), (plate.height, plate.width))

# GENERATE POPULATION

population = generatePopulation(POPULATION_NUMBER, plate)

print('======================MOTHER ROULETTE================')
mother = roulette(population, plate)
print(mother)

print('=====================FATHER TOURNAMENT===========================')
father = tournament(population, plate)
print(father)

draw_plots(getPointsFromSegments(mother, plate), (plate.height, plate.width))
draw_plots(getPointsFromSegments(father, plate), (plate.height, plate.width))

print('======================CROSS=======================')

child_1, child_2 = cross(father, mother)

draw_plots(getPointsFromSegments(child_1, plate), (plate.height, plate.width))
draw_plots(getPointsFromSegments(child_2, plate), (plate.height, plate.width))

