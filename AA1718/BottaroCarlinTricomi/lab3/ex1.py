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


'''
####################################
    CONSIGLIO PER IL DOCENTE
####################################

Gentile professore,
    prima di leggere il codice, le consigliamo di leggere l'esercizio 3 contenente le domande teoriche, specialmente l'ultima domanda, ovvero
    quella che spiega l'implementazione e l'uso del min-heap.
'''


def initSSSP(d,pi,s, V):
    for node in V:
        d[node] = math.inf #cast a float forse
        pi[node] = None
    d[s] = 0

def relax(road_time, d, pi, u, v):
    d[v] = d[u] + road_time
    pi[v] = u


def decreaseKey(Q,x): # decrease key che pusha sempre -> più veloce
    heapq.heappush(Q,x)

def decreaseKey2(Q, node, old_w, new_val): # decrease key tradizionale. Solo una delle due è utilizzata
        i = Q.index([old_w, node]) # trovo l'indice del nodo nell'array Q
        if Q[i][0] < new_val:
            return False

        Q[i][0] = new_val # aggiorno la chiave
        bubbleUp(Q,i) # e sistemo l'albero per mantenere la proprietà di min-heap
        return True    

def bubbleUp(Q, i):
        p = parent(i)
        while i > 0 and Q[i] < Q[p]:
            aux = Q[i]
            Q[i] = Q[p]
            Q[p] = aux
            i = p
            p = parent(i)

def parent(i):
    return int((i - 1) / 2)


def dijkstra(graph, s, V,maximum):
    # creo il dizionario delle distanze e de puntatori al padre
    d = dict() 
    pi = dict()
    # e li inizializzo
    initSSSP(d,pi,s,V)
    Q = [] # heap per la priorità

    # rendo Q la coda di min-priorità
    for node in V:
        heapq.heappush(Q, [d[node],node])

    while Q:
        # maximum serve per misurare la complessità in spazio nel caso usassi decreaseKey, cioè quella che pusha sempre
        if len(Q) > maximum: # salvo la grandezza massima che lo heap può raggiungere
            maximum = len(Q)
        
        # estraggo il minimo
        node = heapq.heappop(Q)
        
        # node e' un array => node[0] = distanza dalla sorgente al nodo(chiave dello heap); node[1] = chiave (identificativo) nodo vero e proprio
        u = node[1] 

        for v in graph.weighted_adj_list[u].keys(): # per ogni nodo adiacente al minimo estratto...
            # Road Time from u to v => rt_u_v
            rt_u_v = graph.getRoadTime(u,v) # ricavo il tempo di percorrenza tra il minimo estratto e ogni suo vicino
            if d[u] + rt_u_v < d[v]: # se ho trovato un nuovo cammino minimo...
                old_w = d[v] # salvo il valore vecchio della chiave dello heap per decraseKey2
                relax(rt_u_v, d, pi, u, v) # rilasso l'arco u -> v
                ####
                
                '''Solo uno tra questi due decreaseKey può essere decommentato'''
               
                decreaseKey(Q,[d[v],v]) # e aggiorno lo heap col nuovo valore rilassato (veloce ma occupa più spazio)
                #decreaseKey2(Q,v,old_w,d[v])  # e aggiorno lo heap col nuovo valore rilassato  (non occupa più spazio del normale, ma 40 volte più lento)
               
                ####

    return (d,pi,maximum)

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
        print("Dijkstra in =",T.time()-t0)

        if(worst_heap_size < maximum): # di tutti gli heap prodotti di dijkstra, trovo quello peggiore (con più nodi)
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
