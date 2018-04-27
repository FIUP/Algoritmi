from utils.graphFromFile import graphFromFile
import bisect
from collections import defaultdict
import os
import time as T


def buildGraphFromSet(A):
    final_graph = defaultdict(list)
    for pair in A:
        node1 = pair[0]
        node2 = pair[1]
        final_graph[node1].append(node2)
        final_graph[node2].append(node1)
    return final_graph

def union(u,v,dict_list):
    i = dict_list[u]
    j = dict_list[v]
    for el in dict_list:
        if (dict_list[el] == j):
            dict_list[el] = i

def kruskal(graph):
    A = set()

    dict_list = dict()
    for x in range(graph.Dimension):
        dict_list[x+1] = x+1
        #print(set_list)

    weight_order_list = [] #ordina matrice adiacenze
    arc_order_list = []
    for i in range(graph.Dimension):
        for j in range (i+1,graph.Dimension):
            p = bisect.bisect(weight_order_list, graph.adj_list[j][i])
            weight_order_list.insert(p, graph.adj_list[j][i])
            arc_order_list.insert(p, (j+1,i+1))

    #print("W",weight_order_list)
    #print("A",arc_order_list)
    #print("LEN",len(order_list))

    for el in arc_order_list:
        u = el[0]
        v = el[1]
        if dict_list[u] != dict_list[v]:
            A.add((u,v))
            union(u,v,dict_list)

    return buildGraphFromSet(A)


def DFSVisited(graph,u,visited,color):
    color[u] = "gray"
    visited.append(u)
    for v in graph[u]:
        if (color[v] == "white"):
            visited = DFSVisited(graph,v,visited,color)
    color[u] = "black"
    return visited

#find minimum spanning tree

def MSP(graph):
    color = dict()
    for i in graph.keys():
        color[i] = "white"

    starting_node = None
    for k in graph: # estraggo la prima chiave del dizionario -> sarà il nodo dal quale iniziare a costruire l'albero
        starting_node = k
        break
    path = DFSVisited(graph,starting_node,[],color)
    path.append(starting_node)
    return path


for filename in os.listdir("graphs/"):
    if filename.endswith(".tsp"):
        t0 = T.time()
        graph = graphFromFile("graphs/"+filename)
        A = kruskal(graph)
        minimum_spanning_tree = MSP(A)
        print("Time", T.time() - t0)
        print("City: ", filename)
        print("MIN SPANNING TREE: \n",minimum_spanning_tree,"\n")
