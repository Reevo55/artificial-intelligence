from fileReader import loadDataPCBs, loadDataChromosomes
from PCB import PCB, Connection, Point
from generatePopulation import generatePopulation

plates = loadDataChromosomes()
plate6x6 = plates[0]

population = generatePopulation(plate6x6)

