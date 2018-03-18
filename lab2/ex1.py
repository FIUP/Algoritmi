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
from utils.resilienceCount import maxCC, DFSVisited
import random
import matplotlib.pyplot as plp
from sys import setrecursionlimit

n = 1476
p = 0.003#(n archi*100/n^2)
m = 3
path = "as19991212.txt"
setrecursionlimit(10000)

#elimina dalla lista delle adiacenze il nodo selezionato e i rispettivi archi
def calcResilience(graph):

    random_node = random.choice(list(graph.adj_list.keys()))

    for nodes in graph.adj_list[random_node]: #elimino tutti gli archi del nodo
        if random_node in graph.adj_list[nodes]:
            graph.adj_list[nodes].remove(random_node)
    graph.adj_list.pop(random_node) #elimino il nodo

    return maxCC(graph) #calcolo la nuova resilienza max


#creo i 3 grafi
all_graphs = graphGenerator(path,n,p,m)
ERgraph = all_graphs.ER_graph
generalGraph = all_graphs.graph_from_file
UPAgraph = all_graphs.UPA_graph


resilience_general = [maxCC(generalGraph)]
resilience_ER = [maxCC(ERgraph)]
resilience_UPA = []

#elimino gli n nodi
for i in range(n):
    resilience_general.append(calcResilience(generalGraph))
    resilience_ER.append(calcResilience(ERgraph))
    resilience_UPA.append(calcResilience(UPAgraph))

#print("RESILIENZA _____________________________",  resilience_ER)

plp.grid()
plp.plot(resilience_general,  label = "General Graph")
plp.plot(resilience_ER, label = "ER Graph p = " + str(p))
plp.plot(resilience_UPA, label = "UPA Graph m = " + str(m))
plp.xlabel('The number of nodes removed')
plp.ylabel('Size of largest connected component after node removal')
plp.title('The resilience of General, ER and UPA Graphs')
plp.legend()
plp.show()
