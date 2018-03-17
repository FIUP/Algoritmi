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

from utils.graphGenerator import graphGenerator
import random
import matplotlib.pyplot as plp
from sys import setrecursionlimit

n = 1476
p = 0.00001 #(n archi*100/n^2)
m = 1
path = "as19991212.txt"
setrecursionlimit(10000)

def DFSVisited(graph,u,visited,color):
    color[u] = "gray"
    visited.add(u)
    for v in graph.adj_list[u]:
        if (color[v] == "white"):
            visited = DFSVisited(graph,v,visited,color)
    color[u] = "black"
    return visited


def resilience(graph):
    color = dict()
    for i in graph.adj_list.keys():
        color[i] = "white"
    CC = []
    visited = set()
    for i in graph.adj_list.keys():
        if (color[i] == "white"):
            comp = DFSVisited(graph,i,visited,color)
            CC.append(comp)
    return CC


def randomAttack(graph):
    # print("Graph to attack: ",graph.adj_list)
    random_node = -1
    L = []
    # seleziona un nodo casuale dalla lista delle adiacenze se il grafo non vuoto
    if graph and graph.adj_list:
        random_node = random.choice(list(graph.adj_list.keys()))
        #print(random_node)
        # e ne estraggo la relativa lista dei nodi adiacenti
        L = graph.adj_list[random_node]
        # print("random node: ",random_node)
        # print("list: ",L)

    #rimuovo il nodo estratto casualmente da tutte le liste delle adj nel quale compare
    for nodes in L:
        graph.adj_list[nodes].remove(random_node)

    # infine rimuovo la chiave corrispondente al nodo estratto casualmente
    graph.adj_list.pop(random_node, None)

    #calcolo la dimensione della massima componente connessa
    newresilience = resilience(graph)
    if not newresilience:
        return 0
    return max(len(l) for l in newresilience)


all_graphs = graphGenerator(path,n,p)
ERgraph = all_graphs.ER_graph
generalGraph = all_graphs.graph_from_file
# UPAgraph = all_graphs.UPA_graph

resilience_general = []
resilience_ER = []
resilience_UPA = []

for i in range(n): # TODO da gestire il caso in cui la lista ritornata è vuota
    #resilience_general.append(randomAttack(generalGraph))
    resilience_ER.append(randomAttack(ERgraph))
    #resilience_UPA.append(randomAttack(UPAgraph))

#plp.plot(resilience_general,  label = "General Graph")
plp.plot(resilience_ER, label = "ER Graph p = 0.15")
#plp.plot(resilience_UPA, label = "UPA Graph m = ")
plp.xlabel('The number of nodes removed')
plp.ylabel('Size of largest connected component after node removal')
plp.title('The resilience of General, ER and UPA Graphs')
plp.legend()
#plp.plot(resilience_ER)
plp.show()
