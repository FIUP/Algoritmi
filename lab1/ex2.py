from utils.inDegree import inDegree
import utils.buildGraphInDegreeDistribution as bG
import numpy
import matplotlib.pyplot as pyp
import random

def generateERGraph(n,p):
    V = [inDegree(i,0) for i in range(n)]
    i = 0
    for i in range(0,len(V)):
        j = 0
        for j in range(0,len(V)):
            a = random.random()
            if (a < p and i != j):
                V[j].in_degree = V[j].in_degree + 1
            j = j + 1
        i = i + 1
    return V

n = 1000
p = 0.15
graphER = generateERGraph(n,p)
in_degree = bG.buildGraphInDegreeDistribution(graphER,n)
in_degree = list(map(lambda x: x/n, in_degree))
pyp.loglog([i for i in range(n)],in_degree)
pyp.show()
