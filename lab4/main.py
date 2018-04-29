from utils.graphFromFile import graphFromFile
from heldKarp import HKTSP
from nearestNeighbor import nearestNeighbor
from TSP import *

for filename in os.listdir("graphs/"):

    if filename.endswith(".tsp"):
        print("City: ", filename)

        graph = graphFromFile("graphs/"+filename)

        #Held Karp algorithm
        '''tHeld = T.time()
        result_heldKarp = HKTSP(graph)
        print("Result Held Karp", result_heldKarp)
        print("Time heldKarp", T.time() - tHeld)'''

        #Nearest Neighbor algorithm
        tNN = T.time()
        insert = [1]
        toInsert = [x for x in range(2,graph.Dimension + 1)]
        result_NN = 0
        for i in range (1,graph.Dimension):
            result_NN = result_NN + nearestNeighbor(graph,insert,toInsert)

        result_NN = result_NN + graph.adj_list[insert[0] - 1][insert[-1] - 1]
        print("Result Nearest Neighbor", result_NN)
        print("Time Nearest Neighbor", T.time() - tNN)

        #2 approssimato algorithm
        tK = T.time()
        A = kruskal(graph)

        minimum_spanning_tree = MSP(A)

        result_K = 0
        for i in range(len(minimum_spanning_tree)-1):
            result_K = result_K + graph.adj_list[minimum_spanning_tree[i] - 1][minimum_spanning_tree[i+1] - 1]

        print("Time 2 approssimato", T.time() - tK)
        print("Result 2 approssimato", result_K)
