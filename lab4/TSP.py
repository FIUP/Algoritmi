from utils.graphFromFile import graphFromFile
import bisect

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

    return A

graph = graphFromFile("graphs/burma14.tsp")
A = kruskal(graph)
print("A",A)
