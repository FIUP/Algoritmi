from utils.readFromFile import readFromFile 
from collections import defaultdict
from ClosestPairAlgorithm import fastClosestPair 

def calcCenter(P):
       sum_x, sum_y = 0.0, 0.0
       for (x,y) in P:
           sum_x = sum_x + x
           sum_y = sum_y + y
        
       n = len(P)
       return (sum_x/n , sum_y/n)



def hierarchicalClustering(P, k):
    # dizionario che ha come chiave il centro del cluster e come valore l'insieme delle coordinate nel cluster
    clusters_dict = defaultdict(list)

    for i in P:
        clusters_dict[i] = i
    
    while len(clusters_dict) > k:
        (d,i,j) = fastClosestPair(clusters_dict.keys())
        C = clusters_dict[i].extend(clusters_dict[j]) # todo: decidere se appendere il più corto al più lungo
        clusters_dict[calcCenter(C)] = C
        del clusters_dict[i]
        del clusters_dict[j]

    return clusters_dict


