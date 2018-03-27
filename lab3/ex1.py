import heapq
import weightedGraphFromFile.py as weightedGraph
import math

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
