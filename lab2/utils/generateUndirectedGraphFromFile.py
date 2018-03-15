# questo script genera un grafo NON orientato dal file ti testo
import itertools
from collections import defaultdict
import numpy as np

class generateUndirectedGraphFromFile:
    def __init__(self,path):
        self.path = path
        self.V = set()
        self.E = set()
        # lista delle adj: e un dizionario il quale associa un set ad ogni chiave. Il set contiene i nodi adiacenti
        self.adj_list = defaultdict(set)
        f = np.loadtxt(self.path, delimiter="\t")
        for line in f:
            # la lettura dal file mi ritorna sempre float, quindi li converto in int
            # brutto ...
            l = [int(n) for n in line] 
            # print l
            # aggiungo i nodi a V
            self.V.add(l[0])
            self.V.add(l[1])
            # Aggiungo l'arco a E, tenendo conto che il grafo NON orientato
            # itertools.combination: https://stackoverflow.com/questions/35047737/unordered-pairs-pair-sets-in-python-from-a-list
            for edge in itertools.combinations(l,2):
                # senza sorted(edge) otterremmo una lista che distingue le coppie non ordinate
                self.E.add(tuple(sorted(edge)))
            self.adj_list[l[0]].add(l[1])
        print self.V
        print self.E
        print self.adj_list

# generateUndirectedGraphFromFile("../as19991212.txt")

