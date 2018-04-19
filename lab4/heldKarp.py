
from utils.graphFromFile import graphFromFile

from math import inf

def HKTSP(graph):
    #struct = dictGenerator2()
    V = frozenset([x for x in range(1,graph.Dimension + 1)])
    return HKVisit(1,V,graph)

def HKVisit(v,S,graph):
    print(graph.d)
    if S == {v}:
        return graph.CalcDistance(v,1,graph.getWeightType())
    elif (v,S) in graph.d and graph.d[(v,S)] != None:
        return graph.d[(v,S)]
    else:
        min_dist = inf
        min_prec = None
        for u in (S - {v}):
            dist = HKVisit(u,S - {v},graph)
            relax_val = dist + graph.CalcDistance(u,v, graph.getWeightType())
            if relax_val < min_dist:
                min_dist = relax_val
                min_prec = u
        
        graph.d[(v,S)] = min_dist
        graph.pi[(v,S)] = min_prec
        
        return min_dist

    

graph = graphFromFile("graphs/burma14.tsp")

res = HKTSP(graph)
