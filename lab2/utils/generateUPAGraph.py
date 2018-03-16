import numpy as np
import matplotlib.pyplot as pyp
import random
from collections import defaultdict
from utils.generateUndirectedGraphER import generateUndirectedGraphER

class UPATrial:
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes #numero di nodi del grafo
        self.node_numbers = [] #lista di numeri di nodo da cui estrarre
		self.adj_list = defaultdict(set)
        for i in range(m):
            for j in range (m):
                self.node_numbers.append(i)


    def runTrial(self, m):

        V = set()
        for i in range(m): #pesco m numeri a caso e li inserisco nella lista V (aumenterà il loro indegree)
            u = random.choice(self.node_numbers)
            V.add(u)

		#aggiorno la lista di node_numbers in modo che ogni num di nodo appaia con la giusta probabilità
        self.node_numbers.append(self.num_nodes) #aggiungo il nuovo nodo
		
		#per ognuno dei nodi estratti aggiungo num node cambiando la probabilità
		for x in range(len(V))
			self.node_numbers.append(self.num_nodes)
		
		
        self.node_numbers.extend(list(V)) #aumento l'indegree dei nodi pescati
        self.num_nodes += 1 #aggiorno il numero di nodi del grafo

	
def UPAgraph(n,m):
	ugraph = generateUndirectedGraphER(m,1).adj_list #creo un uER completo
	v = UPATrial(m)
	for node in range(m,n):
		adjs = v.runTrial(m)
		ugraph[node] = adjs
		for adj in adjs:
			ugraph[adj].add(node)
	return ugraph
	


