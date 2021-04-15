from evaluate import evaluate
import random

TOURNAMENT_CHOSENS_NUM = 5
ROULETTE_CONST = 1000

def roulette(population, populationScore, plate):
    roulette_arr = []

    for individual in population:
        percantage = int((ROULETTE_CONST - evaluate(individual, plate)) / populationScore * (len(population)*10))
        roulette_arr +=  percantage * [individual]

    return random.choice(roulette_arr)

def tournament(population, plate):
    if len(population) <= TOURNAMENT_CHOSENS_NUM: 
        return pickBest(population, plate)

    chosens = random.choices(population, k=TOURNAMENT_CHOSENS_NUM)

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

    