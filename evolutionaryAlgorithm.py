from Chromosome import *
from generatePopulation import *
from selectorMethods import roulette, tournament, ROULETTE_CONST
from cross import cross
import random
from evaluate import *
from mutation import mutation
from timingFunc import *

CROSS_OVER_CHANCE = 0.4
MUTATION_CHANCE = 0.4


def getBestFromPopulation(plate, population):
    bestIndividual = ''
    bestIndividualScore = 99999

    for ind in population:
        ind_score = evaluate(ind, plate)
        if bestIndividualScore > ind_score:
            bestIndividual = ind
            bestIndividualScore = ind_score

    return bestIndividual, bestIndividualScore

@timing
def evolutionaryAlgorithm(plate, populationNum, iterations, bestIndividualScore):
    print("Evaluating...")
    last_population = generatePopulation(populationNum, plate)

    bestScore = 99999
    bestIndividual = ''

    current_population = []
    lastSumOfEvals = 0
    sumOfEvals = 0

    for individual in last_population:
        sumOfEvals += ROULETTE_CONST - evaluate(individual, plate)

    if bestScore < bestIndividualScore:
        return bestIndividual

    bestIndividual, bestScore = getBestFromPopulation(plate, last_population)



    for i in range(0, iterations):
        lastSumOfEvals = sumOfEvals
        sumOfEvals = 0

        current_population.append(bestIndividual)
        last_population.remove(bestIndividual)

        while len(current_population) < populationNum:
            individual_1 = roulette(last_population, lastSumOfEvals, plate)
            individual_2 = tournament(last_population, plate)

            if random.uniform(0, 1) < CROSS_OVER_CHANCE:
                individual_1, individual_2 = cross(individual_1, individual_2)

            if random.uniform(0, 1) < MUTATION_CHANCE:
                mutation(individual_1)

            if random.uniform(0, 1) < MUTATION_CHANCE:
                mutation(individual_2)

            if len(current_population) < populationNum:
                sumOfEvals += ROULETTE_CONST - evaluate(individual_1, plate)
                current_population.append(individual_1)
            if len(current_population) < populationNum:
                sumOfEvals += ROULETTE_CONST - evaluate(individual_1, plate)
                current_population.append(individual_2)

        if bestScore < bestIndividualScore:
            return bestIndividual
        
        last_population = current_population
        current_population = []

    return bestIndividual

    


