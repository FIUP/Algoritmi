from utils.graphFromFile import graphFromFile
from utils.dictGenerator import dictGenerator2

from math import inf

def HKTSP(graph):
    #struct = dictGenerator2()
    d = list()
    pi = list()
    return HKVisit(d,pi,0,graph)

def HKVisit(d,pi,v,S):
    
    if S == {v}:
        return w(v,0,graph.getWeightType())
    elif d[v,S]:
        return d[v,S]
    else:
        min_dist = inf
        min_prec = None
        for u in (S - {v}):
            dist = HKVisit(d,pi,u,S - {v})
            relax_val = dist + w(u,v, graph.getWeightType())
            if relax_val < min_dist:
                min_dist = relax_val
                min_prec = u
        
        d[v,S] = min_dist
        pi[v,S] = min_prec
        
        return min_dist


def w(from_node, to_node, weight_type):

    

graph = graphFromFile("graphs/berlin52.tsp")
