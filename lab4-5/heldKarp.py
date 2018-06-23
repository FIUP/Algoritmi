from utils.graphFromFile import graphFromFile
import os
from math import inf
import time as T
import sys #libreria per interrompere l'esecuzione

def HKTSP(graph):

    V = frozenset([x for x in range(1,graph.Dimension + 1)])
    t0 = T.time()
    return HKVisit(1,V,graph,t0)

def HKVisit(v,S,graph,t0):

    if S == {v}:
        return graph.adj_list[v-1][0] #graph.CalcDistance(v,1,graph.getWeightType())
    elif (v,S) in graph.d and graph.d[(v,S)] != None:
        return graph.d[(v,S)]
    else:
        min_dist = inf
        min_prec = None
        for u in (S - {v}):
            dist = HKVisit(u,S - {v},graph,t0)
            relax_val = dist + graph.adj_list[u-1][v-1]#graph.CalcDistance(u,v, graph.getWeightType())
            if relax_val < min_dist:
                min_dist = relax_val
                min_prec = u

            if T.time() - t0 > 10:
                return min_dist


        graph.d[(v,S)] = min_dist
        graph.pi[(v,S)] = min_prec
        #if T.time() - t0 > 120: #dopo x secondi
        #    print(graph.d[(1,V)])
        #    sys.exit("Esecuzione terminata")

        return min_dist
