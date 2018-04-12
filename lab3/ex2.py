from utils.weightedGraphFromFile import *
import math

'''
Qual'è la capacità massima di veicoli che possono entrare in città dai tre nodi sorgente?
Qual'è la capacità massima di veicoli che possono giungere contemporaneamente ai sei ospedali di destinazione?
Confrontate questi due valori con la capacità massima del piano che avete trovato con CCRP: dove si trova il collo di bottiglia?

'''

def getMaxCapacityFromSource(weightedGraphgraph, S):
    capacity = 0
    for s in S:
        V = weightedGraph.getAdjNodes(s)
        for v in V:
            capacity += weightedGraph.getRoadCapacity(s,v)
    return capacity


def getMaxCapacityToDestination(weightedGraphgraph, D):
    capacity = 0
    for d in D:
        V = weightedGraph.getPredNodes(d)
        for v in V:
            capacity += weightedGraph.getRoadCapacity(v,d)
    return capacity



path = "SFroad.txt"
S = [3718987342, 915248218, 65286004]
D = [261510687, 3522821903, 65319958, 65325408, 65295403, 258913493]
weightedGraph = weightedGraphFromFile(path)
print (getMaxCapacityFromSource(weightedGraph, S))
print (getMaxCapacityToDestination(weightedGraph,D))
