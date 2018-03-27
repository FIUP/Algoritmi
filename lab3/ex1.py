import heapq
from utils.weightedGraphFromFile import *
import math
import matplotlib.pyplot as plp

''' Usate l'algoritmo CCRP per trovare un piano di evacuazione nel grafo della Città di San Francisco.
I nodi sorgente del piano sono i tre ingressi autostradali della città:

nodo 3718987342 (Golden Gate Bridge)
nodo 915248218 (Oakland Bay Bridge)
nodo 65286004 (James Lick Freeway)
I nodi destinazione corrispondono a sei ospedali cittadini:
nodo 261510687 (San Francisco General Hospital)
nodo 3522821903 (UC Medical Center)
nodo 65319958 (Saint Francis Memorial Hospital)
nodo 65325408 (Saint Mary's Medical Center)
nodo 65295403 (CPMP California Campus)
nodo 258913493 (Kaiser-Permanente Medical Center)

Mostrate l'andamento dell'algoritmo in un grafico a linee dove l'asse x corrisponde alle capacità
e l'asse y al tempo di percorrenza. Il grafico deve mostrare come cresce la capacità ed il tempo di percorrenza
al crescere del numero di percorsi inseriti nel piano dall'algoritmo. '''


'''
- CCRP
- DJIKISTRA
- GRAFICO
'''
def initSSSP(d,pi,s, V):
    for node in V:
        d[node] = math.inf #cast a float forse
        pi[node] = None
    d[s] = 0

def Relax(road_time, d, pi, u, v):
    d[v] = d[u] + road_time
    pi[v] = u

def Dijkstra(graph, s):
    l1 = graph.weigthed_adj_list.keys()

    V = set(l1)

    d = dict()
    pi = dict()

    initSSSP(d,pi,s, V)
    Q = list(V)
    heap = list()
    for node in V:
        heapq.heappush(heap,graph.getRoadTime(s,node) (V)) #boh
    while Q:
        u = heapq.heappop(Q) #min
        for node in graph.weigthed_adj_list[u].keys():
            if d[u] + RT < d[node]:
                Relax (RT,d,pi,u,v)
                Decrease

def CCRP(weightedGraph, S, D):
    capacity = []
    time = []
    max_time = 0
    #aggiungo il super nodo sorgente per ricondurci ad un caso con una sorgente unica
    supernode = 0
    for source in S:
        weightedGraph[supernode] = {source : [0, math.inf]}

    plan = []
    #non esiste do While in python
    #lo simulo con
    #while True:
    #   do something
    #   if condiction():
    #       break
    while True:
        path = [33242031,65292114,65312672]
        plan.extend(path)
        flow = math.inf
        t = 0
        #trovo la minima capacità degli archi nel path e calcolo il suo tempo
        for i in range(len(path)-1):
            c = weightedGraph[path[i]][path[i+1]][1]
            print(c)
            t += weightedGraph[path[i]][path[i+1]][0]
            if (c < flow):
                flow = c
        #diminuisco le capacità degli archi
        for i in range(len(path)-1):
            weightedGraph[path[i]][path[i+1]][1] -= flow
            #se la capacità diventa 0 elimino l'arco dal grafo
            if weightedGraph[path[i]][path[i+1]][1] == 0:
                del weightedGraph[path[i]][path[i+1]]
        #aggiungo la nuova capacità
        if capacity:
            flow += capacity[-1]
        capacity.append(flow)
        #aggiungo il tempo di percorrenza maggiore
        if (t > max_time):
            max_time = t
        time.append(max_time)
        #condizione del ciclo
        if not path:
            break

    return (time,capacity)
path = "SFroad.txt"

S = [3718987342, 915248218, 65286004]
D = [261510687, 3522821903, 65319958, 65325408, 65295403, 258913493]
weightedGraph = weightedGraphFromFile(path)
(time,capacity) = CCRP(weightedGraph.weighted_adj_list, S, D)




#creo grafico
plp.plot(time,capacity)
plp.xlabel("Capacity of plan")
plp.ylabel("Time of the longest path in the plan")
plp.title("San Francisco's plan of emergency")
plp.show()
