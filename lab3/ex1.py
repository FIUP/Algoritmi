import heapq
from utils.weightedGraphFromFile import *
import math
import matplotlib.pyplot as plp
from utils.minHeap import *
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


def decreaseKey(Q,x):
    heapq.heappush(Q,x)


def dijkstra(graph, s, V,maximum):
    d = dict()
    pi = dict()
    initSSSP(d,pi,s,V)
    Q = [] # heap per la priorità

    # rendo Q la coda di min-priorità
    for node in V:
        heapq.heappush(Q, [d[node],node])

    while Q:
        if len(Q) > maximum: # salvo la grandezza massima che lo heap può raggiungere
            maximum = len(Q)
        # estraggo il minimo
        node = heapq.heappop(Q)
        # node e' una tupla => node[0] = distanza dalla sorgente al nodo(chiave dello heap); node[1] = nodo vero e proprio
        u = node[1]

        for v in graph.weighted_adj_list[u].keys(): # per ogni nodo adiacente al minimo estratto...
            # Road Time from u to v => rt_u_v
            rt_u_v = graph.getRoadTime(u,v) # ricavo il tempo di percorrenza tra il minimo estratto e ogni suo vicino
            if d[u] + rt_u_v < d[v]:
                old_w = d[v]
                relax(rt_u_v, d, pi, u, v) # se possibile rilasso l'arco u -> 
                #decreaseKey(Q,[d[v],v])
                decrease_key2(Q,v,old_w,d[v])  # e aggiorno lo heap col nuovo valore rilassato
            
                
    #print("scanning in",T.time()-t0,"B.U",i)        
    return (d,pi,maximum)

def parent(i):
    return int((i - 1) / 2)

def bubble_up(Q, i):
        """Takes the node with index i and puts it in the correct position to restore the heap state.
        :param i: index of the node to bubble up
        :return: None
        """
        p = parent(i)
        while i > 0 and Q[i] < Q[p]:
            Q[i], Q[p] = Q[p], Q[i]
            i = p
            p = parent(i)

def decrease_key2(Q, node, old_val, new_val):
        """Updates the distance of the node (old_val) with the new computed distance (new_val), only if the latter
        is greater than the first.
        :param node: identifier of the node, it's not its index
        :param old_val: used as heap.index([old_val, node]) just to find the index of the node that needs the update
        :param new_val: value that will be assigned to the target node - only if new_val > old_val
        :return:
        """
        i = Q.index([old_val, node])
        if Q[i][0] < new_val:
            return False

        Q[i][0] = new_val
        bubble_up(Q,i)
        return True

def CCRP(weightedGraph, S, D):
    
    capacity = []
    time = []
    #aggiungo il super nodo sorgente per ricondurci ad un caso con una sorgente unica
    supernode = 0
    weightedGraph.weighted_adj_list[supernode] = defaultdict(list)
    for source in S:
        weightedGraph.weighted_adj_list[supernode][source].extend([0, math.inf])

    # creo l'insieme di nodi
    # insieme dei nodi che hanno out-degree > 0
    l1 = list(weightedGraph.weighted_adj_list.keys())
    l2 = []
    for el in l1:
        l2 = l2 + list(weightedGraph.weighted_adj_list[el].keys())
    V = set(l1 +  l2)
    # a questo punto V è l'insieme dei nodi

    maximum = 0 # il suo valore sarà il numero di nodi dello heap più grande al momento
    worst_heap_size = 0 # il suo valore sarà il numero di nodi dello heap più grande
    while True:
        t0 = T.time()
        (d,pi,maximum) = dijkstra(weightedGraph, supernode, V, maximum)
        print("t=",T.time()-t0)
        if(worst_heap_size < maximum): # di tutti gli heap, trovo quello peggiore
            worst_heap_size = maximum
        #nodo destinazione con percorso a costo minore
        dest = {k: v for k, v in d.items() if k in D}
        best_destination = min(dest, key = dest.get)
        #genero path
        path = []
        if d[best_destination] != math.inf:
            path = [best_destination]
            father = pi[best_destination]
            while father:
                path = [father] + path
                father = pi[father]

        #se non trovo un percorso ho concluso la creazione del piano
        if not path:
            break

        flow = math.inf
        t = 0
        #trovo la minima capacità degli archi nel path e calcolo il suo tempo
        for i in range(len(path)-1):
            c = weightedGraph.getRoadCapacity(path[i],path[i+1])
            t += weightedGraph.getRoadTime(path[i],path[i+1])
            if (c < flow):
                flow = c
        #diminuisco le capacità degli archi
        for i in range(len(path)-1):
            weightedGraph.weighted_adj_list[path[i]][path[i+1]][1] -= flow
            #se la capacità diventa 0 elimino l'arco dal grafo
            if weightedGraph.getRoadCapacity(path[i], path[i+1]) == 0:
                del weightedGraph.weighted_adj_list[path[i]][path[i+1]]
        #aggiungo la nuova capacità
        if capacity:
            flow += capacity[-1]
        capacity.append(flow)
        #aggiungo il tempo di percorrenza
        time.append(t)
        #condizione del ciclo

    measureQuality(worst_heap_size,len(V)) # ho usato più spazio in memoria per velocizzare l'algoritmo. Ma quanto in piu?

    return (time,capacity)

def measureQuality(w_h_s,n_h_s):
    i_h_s = round(((w_h_s - n_h_s) * 100) / 19262,2) # increase heap size
    normal_depth = round(math.log(n_h_s,2) + 1,2) # calcolo l'altezza dello heap normale
    worst_depth = round(math.log(w_h_s,2) + 1,2) # calcolo l'altezza dello heap peggiore

    # le differenze sono infime...

    print("Worst heap size: ",w_h_s,". Normal heap size:",n_h_s,". => Increase of ",i_h_s,"%")
    print("Original heap depth: ",normal_depth,". Worst depth: ",worst_depth,"Difference: ",round(worst_depth - normal_depth,2))


# PRE = (time è in ore. Esemprio: time = 132.96411)
def decimaleToSexasegimale(time): 
    sexasegimal_time = []
    for el in time:
        hours = int(el)
        minutes = int(round((el * 60) % 60,0))
        seconds = int(round((el * 3600) % 60,0))
        sexasegimal_time.append(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    return sexasegimal_time

path = "SFroad.txt"

S = [3718987342, 915248218, 65286004]
D = [261510687, 3522821903, 65319958, 65325408, 65295403, 258913493]
weightedGraph = weightedGraphFromFile(path)

(time,capacity) = CCRP(weightedGraph, S, D)
#creo grafico

plp.plot(capacity,time)
plp.xlabel("Capacity of plan")
plp.ylabel("Time of the longest path in the plan")
plp.title("San Francisco's plan of emergency")
plp.show()
