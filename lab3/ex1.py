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

def relax(road_time, d, pi, u, v):
    d[v] = d[u] + road_time
    pi[v] = u

def decreaseKey(Q,d,u,v,rt_u_v):
    d[v] = d[u] + rt_u_v
    heapq.heappush(Q,(d[v],v))

def dijkstra(graph, s):
    # creo l'insieme di nodi
    # insieme dei nodi che hanno out-degree > 0
    V = set(graph.weighted_adj_list.keys())
    i = 0
    for el in V:
        V = V.union(set(graph.weighted_adj_list[el].keys())) # insieme dei nodi adiacenti ad ogni nodo con out-degree > 0. Così prendo anche i nodi con grado entrante = 0
    # a questo punto V è l'insieme dei nodi
    #print("Insieme di nodi",V)

    d = dict()
    pi = dict()
    initSSSP(d,pi,s,V)
    Q = [] # heap per la priorità

    # rendo Q la coda di min-priorità
    for node in V:
        heapq.heappush(Q, (d[node],node)) 

    # print("heap",Q)
    while Q:
        # estraggo il minimo
        node = heapq.heappop(Q)
        # node e' una tupla => node[0] = distanza dalla sorgente al nodo(chiave dello heap); node[1] = nodo vero e proprio
        u = node[1] 
        # print("min ", u)
        
        for v in graph.weighted_adj_list[u].keys(): # per ogni nodo adiacente al minimo estratto...
            # print("adj",v)
            # Road Time from u to v => rt_u_v
            rt_u_v = graph.getRoadTime(u,v) # ricavo il tempo di percorrenza tra il minimo estratto e ogni suo vicino
            if d[u] + rt_u_v < d[v]:
                relax(rt_u_v, d, pi, u, v) # se possibile rilasso l'arco u -> v
                decreaseKey(Q,d,u,v,rt_u_v) # e aggiorno lo heap col nuovo valore rilassato
                # print("heap",Q)
    return d
                
'''
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
        path = Dijkstra(weightedGraph, supernode)
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
'''

path = "SFroad.txt"

S = [3718987342, 915248218, 65286004]
D = [261510687, 3522821903, 65319958, 65325408, 65295403, 258913493]
weightedGraph = weightedGraphFromFile(path)
#print("Graph ",weightedGraph.weighted_adj_list)
#dijkstra(weightedGraph,1)
print ("RESULT ",dijkstra(weightedGraph,1))




#creo grafico
'''plp.plot(time,capacity)
plp.xlabel("Capacity of plan")
plp.ylabel("Time of the longest path in the plan")
plp.title("San Francisco's plan of emergency")
plp.show()'''
