from utils.graphFromFile import graphFromFile
import bisect
from collections import defaultdict
import os


def buildGraphFromSet(A):
    final_graph = defaultdict(list)
    for pair in A:
        node1 = pair[0]
        node2 = pair[1]
        final_graph[node1].append(node2)
        final_graph[node2].append(node1)
    return final_graph
    
def findSet(node,set_list):
    for i in range (len(set_list)):
        if node in set_list[i]:
            return i

def union(u,v,set_list):
    i = findSet(u,set_list)
    j = findSet(v,set_list)
    set_list[i].extend(set_list[j])
    del set_list[j]

def kruskal(graph):
    A = set()
    set_list = [[x + 1] for x in range(graph.Dimension)]
    print(set_list)

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
        if findSet(u,set_list) != findSet(v,set_list):
            A.add((u,v))
            union(u,v,set_list)

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
    for k in graph:
        starting_node = k
        break
    return DFSVisited(graph,starting_node,[],color)


for filename in os.listdir("graphs/"):
    if filename.endswith(".tsp"):
        graph = graphFromFile("graphs/"+filename)
        A = kruskal(graph)
        minimum_spanning_tree = MSP(A)
        print("City: ", filename, "\n")
        print("MIN SPANNING TREE: \n",minimum_spanning_tree)