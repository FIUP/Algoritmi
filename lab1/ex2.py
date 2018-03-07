from utils.inDegree import inDegree
import utils.buildGraphInDegreeDistribution as bG
import numpy
import matplotlib.pyplot as pyp
import random

def generateERGraph(n,p):
    V = [inDegree(i,0) for i in range(n)]
    i = 0
    while (i < len(V)):
        j = 0
        while (j < len(V)):
            a = random.random()
            if (a < p and i != j):
                V[j].in_degree = V[j].in_degree + 1
            j = j + 1
        i = i + 1
    return V

graphER = generateERGraph(1000,0.5)
in_degree = bG.buildGraphInDegreeDistribution(graphER,1000)
in_degree = list(map(lambda x: x/1000, in_degree))
pyp.loglog([i for i in range(1000)],in_degree)
pyp.show()
