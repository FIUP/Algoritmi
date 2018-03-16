'''Come prima cosa determinate dei valori di n, p e m tali che la procedura ER e la procedura UPA generino un grafo
con lo stesso numero di nodi ed un numero di archi simile a quello della rete reale.

Quindi, per ognuno dei tre grafi (rete reale, ER, UPA), simulate un attacco che disabiliti i nodi
della rete uno alla volta seguendo un ordine casuale, fino alla disattivazione di tutti i nodi del grafo,
e calcolate la resilienza del grafo dopo ogni rimozione di un nodo.

Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala
lineare (non log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea
per ognuna delle curve.
L'asse orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n),
mentre l'asse verticale alla dimensione della componente connessa piu grande rimasta dopo aver rimosso un certo numero di nodi.
Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori di p e m utilizzati.
Allegate il file con la figura nell'apposito spazio.'''

from utils.generateUndirectedGraphER import generateUndirectedGraphER
from utils.generateUndirectedGraphFromFile import generateUndirectedGraphFromFile
import random
n = 1476
p = 0.15 #(n archi*100/n^2)
m = 1

generalGraph = generateUndirectedGraphFromFile("as19991212.txt")
ERgraph = generateUndirectedGraphER(n,p)
# UPAgraph =

def resilience(graph):
    color = ["white" for i in range(len(graph.V))]
    CC = []
    for i in range(len(graph.V)):
        if (color[i] == "white"):
            comp = DFSVisited(graph,i,[])

def DFSVisited(graph,u,visited):
    graph

def randomAttack(graph):
    # print("Graph to attack: ",graph.adj_list)
    random_node = -1
    L = []
    # seleziona un nodo casuale dalla lista delle adiacenze se il grafo non vuoto
    if graph and graph.adj_list:
        random_node = random.choice(graph.adj_list.keys())
        # e ne estraggo la relativa lista dei nodi adiacenti
        L = graph.adj_list[random_node]
        # print("random node: ",random_node)
        # print("list: ",L)
    
    #rimuovo il nodo estratto casualmente da tutte le liste delle adj nel quale compare
    for nodes in L:
        if random_node in graph.adj_list[nodes]: # TODO: ma questo controllo serve??
            graph.adj_list[nodes].remove(random_node)
    
    # infine rimuovo la chiave corrispondente al nodo estratto casualmente
    graph.adj_list.pop(random_node, None)

    # print("final graph: ",graph.adj_list)


#randomAttack(generalGraph)
#randomAttack(ERgraph)
