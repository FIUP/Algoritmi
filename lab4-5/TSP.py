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
    #dizionario con chiave il nodo e valore il testimone
    for x in range(graph.Dimension):
        dict_list[x+1] = x+1


    arc_order_list = []
    for i in range(graph.Dimension):
        for j in range (i+1,graph.Dimension):
            arc_order_list.append((graph.adj_list[j][i],j+1,i+1))
    arc_order_list.sort(key=lambda tup: tup[0])


    #print("W",weight_order_list)
    #print("A",arc_order_list)
    #print("LEN",len(order_list))
    for el in arc_order_list:
        u = el[1]
        v = el[2]
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

'''tTot = T.time()
for filename in os.listdir("graphs/"):

    if filename.endswith(".tsp"):
        print("City: ", filename)
        t0 = T.time()
        graph = graphFromFile("graphs/"+filename)

        A = kruskal(graph)

        minimum_spanning_tree = MSP(A)

        result = 0
        for i in range(len(minimum_spanning_tree)-1):
            result = result + graph.adj_list[minimum_spanning_tree[i] - 1][minimum_spanning_tree[i+1] - 1]

        print("Time", T.time() - t0)
        print("RESULT", result)
        print("MIN SPANNING TREE: \n",minimum_spanning_tree,"\n")

print("TEMPO FINALE", T.time() - tTot)'''
