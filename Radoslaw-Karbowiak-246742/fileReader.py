import os
from os import listdir
from os.path import isfile, join
from PCB import PCB, Connection
from Chromosome import *

zadPath = "\\problemy-testowe\\zad\\"
dirPath = os.path.dirname(os.path.abspath(__file__)) + zadPath

filesToRead = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]

def loadDataPCBs():
    data = []

    for file in filesToRead:
        f = open(dirPath + file, "r")
        dimensions = f.readline();
        
        width = int(dimensions.split(";")[0])
        height = int(dimensions.split(";")[1])

        connectionsArr = [];
        for line in f.readlines():
            points = line.split(";");

            start = Point(int(points[0]), int(points[1]))
            end = Point(int(points[2]), int(points[3]))

            connection = Connection(start, end)
            connectionsArr.append(connection)

        data.append(PCB(width, height, connectionsArr))

    return data

    
