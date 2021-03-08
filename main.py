from fileReader import loadDataPCBs
from PCB import PCB, Connection
from generatePopulation import generatePopulationForPlate

POPULATION_NUMBER = 5

plates = loadDataPCBs()
plate6x6 = plates[0]

population = generatePopulationForPlate(plate6x6, POPULATION_NUMBER)

print('========== POPULATION ============')

print(population)


