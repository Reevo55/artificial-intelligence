from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulationForPlate, generateIndividual
from evaluate import *
from Chromosome import *
from timingFunc import timing
from visualisation import *

POPULATION_NUMBER = 5
RANDOM_METHOD_ITERATIONS = 10000

plates = loadDataPCBs()
plate = plates[4]

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

bestIndividual = randomMethod(plate, RANDOM_METHOD_ITERATIONS)
print('Best individual: ')
print(bestIndividual)

printSums(bestIndividual, plate)

arrOfPoints = getPointsFromSegments(bestIndividual, plate)

draw_plots(getPointsFromSegments(bestIndividual, plate), (plate.width, plate.height))

