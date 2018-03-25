# questo script genera un grafo NON orientato dal file ti testo
import itertools
from collections import defaultdict
import numpy as np

class generateUndirectedGraphFromFile:
    def __init__(self,path):
        self.path = path
        # lista delle adj: e un dizionario il quale associa un set ad ogni chiave. Il set contiene i nodi adiacenti
        self.adj_list = defaultdict(set)
        f = np.loadtxt(self.path, delimiter="\t")
        for line in f:
            l = [int(n) for n in line]

            if (l[0] != l[1]):
                self.adj_list[l[0]].add(l[1])
        #print(self.adj_list)
