import numpy as np
import matplotlib.pyplot as pyp
import random

class DPATrial:
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes #numero di nodi del grafo
        self.node_numbers = [] #lista di numeri di nodo da cui estrarre
        for i in range(m):
            for j in range (m):
                self.node_numbers.append(i)


    def runTrial(self, m):

        V = set()
        for i in range(m): #pesco m numeri a caso e li inserisco nella lista V (aumenterà il loro indegree)
            u = random.choice(self.node_numbers)
            V.add(u)

        self.node_numbers.append(self.num_nodes) #aggiungo il nuovo nodo
        self.node_numbers.extend(V) #aumento l'indegree dei nodi pescati
        self.num_nodes += 1 #aggiorno il numero di nodi del grafo


m = 12
n = 27770
p = DPATrial(m)

for k in range(n - p.num_nodes): #pesco fino ad avere 27770 nodi
    p.runTrial(m)

#mostro il numero di nodi e archi totali
print (p.num_nodes)
print (len(p.node_numbers))

#Calcolo l'in-degree di ogni nodo
in_degree = dict()
for node in p.node_numbers:
    in_degree[node] = -1

for n in p.node_numbers:
    in_degree[n] += 1


#Calcolo la distribuzione dell'in-degree
distribution = np.zeros(27770)
for node in in_degree:
    distribution[in_degree[node]] += 1

#Normalizzazione
distribution = list(map(lambda x : x/27770, distribution))

#grafico
pyp.loglog(distribution)
pyp.show()
