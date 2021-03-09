from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulationForPlate, generateIndividual
from evaluate import *
from Chromosome import *

POPULATION_NUMBER = 5
RANDOM_METHOD_ITERATIONS = 20

plates = loadDataPCBs()
plate6x6 = plates[0]

# population = generatePopulationForPlate(plate6x6, POPULATION_NUMBER)
# print('========== POPULATION ============')
# print(population)

def randomMethod(plate, iterations):
    bestIndividual = ''
    bestIndividualScore = 99999

    for i in range(0, iterations):
        randIndividual = generateIndividual(plate)
        randIndividualScore = evaluate(randIndividual, plate)

        if bestIndividualScore > randIndividualScore:
            bestIndividual = randIndividual
            bestIndividualScore = randIndividualScore

    print('Best individual score: ' + str(bestIndividualScore))
    return bestIndividual

bestIndividual = randomMethod(plate6x6, RANDOM_METHOD_ITERATIONS)
print(bestIndividual)

# print('=============================METODA LOSOWA===================================')
# individual = generateIndividual(plate6x6)
# print("--- INDIVIDUAL --- ")
# print(individual)
# print("Suma segmentów: " + str(sumOfSegments(individual)))
# print("Suma długości segmentów: " + str(sumOfLengths(individual)))
# print("Ilość przecięć: " + str(sumOfIntersections(individual)))
# print("Ilość punktów poza płytką: " + str(sumOfOutsiders(individual, plate6x6)))
# print("Suma punktów: " + str(evaluate(individual, plate6x6)))