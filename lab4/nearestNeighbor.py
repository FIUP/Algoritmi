from utils.graphFromFile import graphFromFile
import math
import os
import time as T

def nearestNeighbor(graph, insert, toInsert):
    min = math.inf
    n = None

    for node in toInsert:
        if graph.adj_list[insert[-1] - 1][node - 1] < min:
            min = graph.adj_list[insert[-1] - 1][node - 1]
            n = node

    insert.append(n)
    toInsert.remove(n)

    return min

for filename in os.listdir("graphs/"):
    if filename.endswith(".tsp"):
        t0 = T.time()
        graph = graphFromFile("graphs/"+filename)
        insert = [1]
        toInsert = [x for x in range(2,graph.Dimension + 1)]
        result = 0
        for i in range (1,graph.Dimension):
            result = result + nearestNeighbor(graph,insert,toInsert)

        result = result + graph.adj_list[insert[0] - 1][insert[-1] - 1]
        print("FileName ", filename)
        print("Result ", result)
        print("Tempo di esecuzione ",T.time() - t0)
