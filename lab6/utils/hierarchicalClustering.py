from collections import defaultdict
from closestPairAlgorithm import fastClosestPair 

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
    
    L = clusters_dict.keys() # Lista dei centri
    centers_list_ord_x = sorted(L, key = lambda coord: coord[0]) # lista dei centri ordinata secondo l'asse x
    centers_list_ord_y = sorted(L, key = lambda coord: coord[1]) # lista dei centri ordinata secondo l'asse y

    while len(clusters_dict) > k:
        (d,i,j) = fastClosestPair(centers_list_ord_x, centers_list_ord_y)
        C = clusters_dict[i].extend(clusters_dict[j]) # todo: decidere se appendere il più corto al più lungo
        clusters_dict[calcCenter(C)] = C
        del clusters_dict[i]
        del clusters_dict[j]

    return clusters_dict


