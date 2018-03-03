''' A lezione abbiamo visto l'algoritmo ER(n, p) per generare grafi casuali.
Confrontate la forma della distribuzione che avete ottenuto nella Domanda 1 con quella generata da ER.
Per farlo potete generare diversi grafi casuali per valori diversi di n e di p. Rispondete quindi alle seguenti domande:
 - Com'è fatta la distribuzione del grado entrate di un grafo generato con ER? Descrivete a parole la sua forma.
 - Ha una forma simile a quella del grafo delle citazioni oppure no? Spiegate brevemente le differenze e le somiglianze tra
   le due distribuzioni.
'''
from utils.inDegree import inDegree
import utils.buildGraphInDegreeDistribution as bG
import numpy
import matplotlib.pyplot as pyp
import random

def generateERGraph(n,p):
    V = [inDegree(i,0) for i in range(n)]
    i = 0
    while (i < len(V)):
        j = 0
        while (j < len(V)):
            a = random.random()
            if (a < p and i != j):
                V[j].in_degree = V[j].in_degree + 1
            j = j + 1
        i = i + 1
    return V

graphER = generateERGraph(1000,0.15)
in_degree = bG.buildGraphInDegreeDistribution(graphER,1000)
in_degree = list(map(lambda x: x/1000, in_degree))
pyp.loglog([i for i in range(1000)],in_degree)
pyp.show()
