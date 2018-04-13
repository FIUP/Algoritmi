import numpy as np
from collections import defaultdict
import math


# il grafo è rappresentato come matrice delle adiacenze,
# dove gli indice di riga e colonna rappresentano i nodi, e il valore
# deferenziato è la distanza tra i nodi

class graphFromFile:
    def __init__(self, path):
        f = open(path, 'r')

        # Leggo l'header
        Name = f.readline().strip().split()[1] # NAME
        FileType = f.readline().strip().split()[1] # TYPE
        Comment = f.readline().strip().split()[1] # COMMENT
        Dimension = f.readline().strip().split()[1] # DIMENSION
        EdgeWeightType = f.readline().strip().split()[1] # EDGE_WEIGHT_TYPE

        #vado avanti con la lettura fino a NODE_COORD_SECTION
        while f.readline().strip()!="NODE_COORD_SECTION":
            pass

        #lista dei nodi lista[indice]->[x,y]
        nodelist = []
        N = int(Dimension)
        for i in range(0, int(Dimension)):
            x,y = f.readline().strip().split()[1:]
            nodelist.append([int(math.modf(float(x))[1]), int(math.modf(float(y))[1])])

        adj_list=[[0 for x in range(int(Dimension))] for y in range(int(Dimension))]

        for x in range(int(Dimension)):
            for y in range(int(Dimension)):
                adj_list[x][y] = nodelist[x][0]+nodelist[y][0]
        print(nodelist)
        print(adj_list)
