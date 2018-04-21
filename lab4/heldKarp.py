from utils.graphFromFile import graphFromFile
import os

from utils.graphFromFile import graphFromFile

from math import inf

def HKTSP(graph):

    V = frozenset([x for x in range(1,graph.Dimension + 1)])
    return HKVisit(1,V,graph)

def HKVisit(v,S,graph):
    if S == {v}:
        return graph.adj_list[v-1][0] #graph.CalcDistance(v,1,graph.getWeightType())
    elif (v,S) in graph.d and graph.d[(v,S)] != None:
        return graph.d[(v,S)]
    else:
        min_dist = inf
        min_prec = None
        for u in (S - {v}):
            dist = HKVisit(u,S - {v},graph)
            relax_val = dist + graph.adj_list[u-1][v-1] #graph.CalcDistance(u,v, graph.getWeightType())
            if relax_val < min_dist:
                min_dist = relax_val
                min_prec = u


        graph.d[(v,S)] = min_dist
        graph.pi[(v,S)] = min_prec

        return min_dist

graph = graphFromFile("graphs/burma14.tsp")
res = HKTSP(graph)
print("RESULT",res)

'''# itero su tutti i file in graphs che terminano con .tsp
for filename in os.listdir("graphs/"):
    if filename.endswith(".tsp"):
        graph = graphFromFile("graphs/"+filename)
        res = HKTSP(graph)'''
