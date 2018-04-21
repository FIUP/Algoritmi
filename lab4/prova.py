from utils.graphFromFile import *

path= "graphs/burma14.tsp"

graph = graphFromFile(path)
print(graph.adj_list)
