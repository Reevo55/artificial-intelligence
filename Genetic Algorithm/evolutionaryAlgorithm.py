from Chromosome import *
from generatePopulation import *
from selectorMethods import roulette, tournament, ROULETTE_CONST
from cross import cross
import random
from evaluate import *
from mutation import mutation
from timingFunc import *

from matplotlib import pyplot as plt

CROSS_OVER_CHANCE = 0.25
MUTATION_CHANCE = 0.25

scoreDict = {}

def getWorstFromPopulation(plate, population):
    worstIndividual = ''
    worstIndividualScore = 0

    for ind in population:
        if ind not in scoreDict:
            scoreDict[ind] = evaluate(ind, plate)

        ind_score = scoreDict[ind]
        
        if worstIndividualScore < ind_score:
            worstIndividual = ind
            worstIndividualScore = ind_score

    return worstIndividual, worstIndividualScore

def getBestFromPopulation(plate, population):
    bestIndividual = ''
    bestIndividualScore = 99999

    for ind in population:
        if ind not in scoreDict:
            scoreDict[ind] = evaluate(ind, plate)

        ind_score = scoreDict[ind]
        if bestIndividualScore > ind_score:
            bestIndividual = ind
            bestIndividualScore = ind_score

    return bestIndividual, bestIndividualScore

def getAvgPopulation(plate, population):
    sum = 0

    for ind in population:
        if ind not in scoreDict:
            scoreDict[ind] = evaluate(ind, plate)
        
        sum += scoreDict[ind]

    return sum / len(population)

@timing
def evolutionaryAlgorithm(plate, populationNum, iterations, bestIndividualScore):
    print("Evaluating...")
    last_population = generatePopulation(populationNum, plate)

    bestIndividualArr = []
    worstIndividualArr = []
    avgArr = []

    skipped = 0
    bestScore = 99999
    bestIndividual = ''

    current_population = []
    lastSumOfEvals = 0
    sumOfEvals = 0

    for individual in last_population:
        if individual not in scoreDict:
            scoreDict[individual] = evaluate(individual, plate)
        else: skipped += 1

        sumOfEvals += ROULETTE_CONST - scoreDict[individual]

    if bestScore < bestIndividualScore:
        return bestIndividual

    bestIndividual, bestScore = getBestFromPopulation(plate, last_population)
    worstIndividual, worstIndividualScore = getWorstFromPopulation(plate, last_population)


    for i in range(0, iterations):
        print("Evaluating... [" + str(i + 1) + " out of " + str(iterations) + "]") 
        lastSumOfEvals = sumOfEvals
        sumOfEvals = 0
        
        bestIndividualArr.append(scoreDict[bestIndividual])
        worstIndividualArr.append(scoreDict[worstIndividual])
        avgArr.append(getAvgPopulation(plate, last_population))

        current_population.append(bestIndividual)
        last_population.remove(bestIndividual)

        while len(current_population) < populationNum:
            # individual_1 = roulette(last_population, lastSumOfEvals, plate)
            # individual_2 = roulette(last_population, lastSumOfEvals, plate)
            individual_2 = tournament(last_population, plate)
            individual_1 = tournament(last_population, plate)

            if random.uniform(0, 1) < CROSS_OVER_CHANCE:
                individual_1, individual_2 = cross(individual_1, individual_2)

            if random.uniform(0, 1) < MUTATION_CHANCE:
                mutation(individual_1)

            if random.uniform(0, 1) < MUTATION_CHANCE:
                mutation(individual_2)

            if len(current_population) < populationNum:
                if individual_1 not in scoreDict:
                    scoreDict[individual_1] = evaluate(individual_1, plate)
                else: skipped += 1

                sumOfEvals += ROULETTE_CONST - scoreDict[individual_1]
                current_population.append(individual_1)
            if len(current_population) < populationNum:
                if individual_2 not in scoreDict:
                    scoreDict[individual_2] = evaluate(individual_2, plate)
                else: skipped += 1

                sumOfEvals += ROULETTE_CONST - scoreDict[individual_2]
                current_population.append(individual_2)

        bestIndividual, bestScore = getBestFromPopulation(plate, current_population)
        worstIndividual, worstIndividualScore = getWorstFromPopulation(plate, current_population)

        if bestScore < bestIndividualScore:
            return bestIndividual
        
        last_population = current_population
        current_population = []

    print("Skipped: " + str(skipped))
    

    draw_plot(bestIndividualArr, worstIndividualArr, avgArr)

    return bestIndividual

    
def draw_plot(bestIndividualArr, worstIndividualArr, avgIndividualArr):
    plt.title("Wartości przystosowań w populacji")
    plt.ylabel("Wartości przystosowania")
    plt.xlabel("Numer populacji")

    populationNum = list(range(0, len(bestIndividualArr)))

    plt.plot(populationNum, bestIndividualArr, label='Najlepszy osobnik w populacji')
    plt.plot(populationNum, worstIndividualArr, label='Najgorszy osobnik w populacji')
    plt.plot(populationNum, avgIndividualArr, linestyle='--', label='Średnia w populacji')

    plt.legend()
    plt.show(block=False)
    plt.show()


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