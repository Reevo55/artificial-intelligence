from evaluate import evaluate
import random

TOURNAMENT_CHOSENS_NUM = 8
ROULETTE_CONST = 10000

def roulette(population, plate):
    roulette_arr = []
    sumOfEvals = 0

    for individual in population:
        sumOfEvals += ROULETTE_CONST - evaluate(individual, plate)

    for individual in population:
        percantage = int((ROULETTE_CONST - evaluate(individual, plate)) / sumOfEvals * 100)
        roulette_arr +=  percantage * [individual]

    return random.choice(roulette_arr)

def tournament(population, plate):
    if len(population) <= TOURNAMENT_CHOSENS_NUM: 
        return pickBest(population, plate)

    chosens = set()

    while len(chosens) != TOURNAMENT_CHOSENS_NUM:
        chosens.add(random.choice(population))

    return pickBest(chosens, plate)

def pickBest(candidates, plate):
    bestIndividual = ''
    bestIndividualScore = 99999

    for individual in candidates:
        individualScore = evaluate(individual, plate)

        if bestIndividualScore > individualScore:
            bestIndividual = individual
            bestIndividualScore = individualScore

    return bestIndividual

    