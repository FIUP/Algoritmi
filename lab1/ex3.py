'''Considerate ora l'Algoritmo DPA(m, n) per generare grafi casuali visto a lezione.
Implementate l'algoritmo e usatelo per generare un grafo casuale con un numero di nodi e di archi simile al grafo delle citazioni.
Scegliere il valore n da passare all'algoritmo è facile: basta usare un valore vicino al numero di nodi del grafo delle citazioni.
Siccome ogni iterazione dell'algoritmo aggiunge m archi al grafo, usare un valore intero vicino al grado uscente medio del grafo
delle citazioni è una buona scelta per m.

Dopo aver scelto m e n, generate il grafo casuale e calcolate la distribuzione del grado entrante normalizzata.
Specificare i valori di m e n che avete scelto nella casella di testo che appare dopo aver premuto sul bottone "Aggiungi consegna"
e allegate il file con il grafico di dispersione in scala log-log come nella Domanda 1.'''

from utils.inDegree import inDegree
import utils.buildGraphInDegreeDistribution as bG
import numpy
import matplotlib.pyplot as pyp

def generateDPAGraph(n,m):
    V = [inDegree(i,m-1) for i in range(m)]
    
