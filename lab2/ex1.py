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
p = 0.003 #(n archi*100/n^2)
m = 2
path = "as19991212.txt"
setrecursionlimit(10000)


def DFSVisited(graph,u,visited,color):
    color[u] = "gray"
    visited.append(u)
    for v in graph.adj_list[u]:
        if (color[v] == "white"):
            visited = DFSVisited(graph,v,visited,color)
    color[u] = "black"
    return visited


def maxCC(graph):
    color = dict()
    for i in graph.adj_list.keys():
        color[i] = "white"
    CC = []
    for i in graph.adj_list.keys():
        if (color[i] == "white"):
            comp = DFSVisited(graph,i,[],color)
            CC.append(comp)
    return CC


def calcResilience(graph, attack_order):
    # print("Graph to attack: ",graph.adj_list)
    start_max_cc = maxCC(graph) #calcolo resilienza iniziale
    resilience = [start_max_cc]

    for node in attack_order: #per ogni nodo da rimuovere
        for nodes in graph.adj_list[node]: #elimino tutti gli archi del nodo
            if node in graph.adj_list[nodes]:
                graph.adj_list[nodes].remove(node)
        graph.adj_list.pop(node) #elimino il nodo
        max_cc = maxCC(graph) #calcolo la nuova resilienza max
        resilience.append(max_cc) #e la aggiungo alla lista di resilienze

    return resilience



all_graphs = graphGenerator(path,n,p,m)
ERgraph = all_graphs.ER_graph
generalGraph = all_graphs.graph_from_file
UPAgraph = all_graphs.UPA_graph

print(UPAgraph.adj_list)

resilience_general = []
resilience_ER = []
resilience_UPA = []

#genero ordine casuale di nodi di un grafico
def random_order(ugraph):
    nodes = list(ugraph.adj_list.keys())
    random.seed(1)      # imposto il seed per garantire lo stesso risultato
    random.shuffle(nodes)
    return nodes


#creo un ordine d'attacco
attack_order= random_order(ERgraph)
x_value = range(len(attack_order) + 1)

resilience_general = calcResilience(generalGraph,attack_order)
resilience_ER= calcResilience(ERgraph,attack_order)
resilience_UPA= calcResilience(UPAgraph,attack_order)

print("RESILIENZA _____________________________",  resilience_general)

'''
plp.grid()
plp.plot(x_value, resilience_general,  label = "General Graph")
plp.plot(x_value,resilience_ER, label = "ER Graph p = 0.15")
plp.plot(x_value,resilience_UPA, label = "UPA Graph m = 1")
plp.xlabel('The number of nodes removed')
plp.ylabel('Size of largest connected component after node removal')
plp.title('The resilience of General, ER and UPA Graphs')
plp.legend()
#plp.plot(resilience_ER)
plp.show()
'''
