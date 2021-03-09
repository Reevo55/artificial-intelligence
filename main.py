from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulationForPlate, generateIndividual
from evaluate import *
from Chromosome import *
import time
from timingFunc import timing


POPULATION_NUMBER = 5
RANDOM_METHOD_ITERATIONS = 100

plates = loadDataPCBs()
plate = plates[3]

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

bestIndividual = randomMethod(plate6x6, RANDOM_METHOD_ITERATIONS)
print('Best individual: ')
print(bestIndividual)

printSums(bestIndividual, plate)

arrOfPoints = getPointsFromSegments(bestIndividual, plate)

draw_plots(getPointsFromSegments(bestIndividual, plate), (plate.height, plate.width))

