import numpy as np
from collections import defaultdict, namedtuple
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
        self.Dimension = int(f.readline().strip().split()[1]) # self.Dimension
        self.EdgeWeightType = f.readline().strip().split()[1] # EDGE_WEIGHT_TYPE

        self.d = {}
        self.pi = {}

        # dobbiamo generare due dizionari che hanno come key la tupla (v, S)
       # self._generateDistanceAndFatherDict(self.d,self.pi)

        #vado avanti con la lettura fino a NODE_COORD_SECTION
        while f.readline().strip()!="NODE_COORD_SECTION":
            pass

        #lista dei nodi lista[indice]->[x,y]
        nodelist = []
        N = self.Dimension
        for i in range(0, self.Dimension):
            x,y = f.readline().strip().split()[1:]
            nodelist.append([float(x), float(y)])

        self.adj_list=[[0 for x in range(self.Dimension)] for y in range(self.Dimension)]

        #nodelist.append([int(math.modf(float(x))[1]), int(math.modf(float(y))[1])])


        for x in range(self.Dimension):
            for y in range(self.Dimension):
                self.x=1
                self.adj_list[x][y] = self.CalcDistance(nodelist[x], nodelist[y], self.EdgeWeightType)
        #print(nodelist)
        #print(self.adj_list)

    def CalcDistance(self, source,dest,type):
        if type == "EUC_2D":
            dist = math.sqrt((source[0]-dest[0])**2 + (source[1]-dest[1])**2)
            dist = round(dist)
            return dist
        else:
            if type == "GEO":
                #converto coord in radianti
                source_lat = self.CalcRadian(source[0])
                source_long = self.CalcRadian(source[1])
                dest_lat = self.CalcRadian(dest[0])
                dest_long = self.CalcRadian(dest[1])
                #calcolo la distanta
                RRR = 6378.388
                q1 = math.cos(source_long - dest_long)
                q2 = math.cos(source_lat - dest_lat)
                q3 = math.cos(source_lat + dest_lat)
                dist = int(RRR * math.acos(0.5*((1.0+q1)*q2 - (1.0 - q1) * q3) ) + 1.0)
                return dist

    def CalcRadian(self, i):
        deg = int(i)
        min = i - deg
        return (math.pi *(deg + 5*min/3.0)/180.0)

    def getWeightType(self):
        return self.EdgeWeightType
