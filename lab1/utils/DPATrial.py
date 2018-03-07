import numpy as np
import matplotlib.pyplot as pyp

class DPATrial:
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes
        self.node_numbers = self.buildCompleteGraph(num_nodes)
    
    def buildCompleteGraph2(self,num_nodes):
        graph = {}
        for i in range(num_nodes):
            graph[i] = set([])
            for j in range(num_nodes):
                if(i != j):
                    graph[i].add(j)
        return graph
    
    def buildCompleteGraph(self,num_nodes):
        V = set()
        E = set()

        for i in range(num_nodes):
            V.add(i)
            for j in range(num_nodes):
                if(i != j):
                    E.add((i,j))
        
        return (V,E)


    def computeTotalInDegree2(self,graph):
        total = 0
        # return a list of adj lists
        list_adj_lists = graph.values()

        # return a list of all IN nodes
        list_in_nodes = [node for adj_lists in list_adj_lists for node in adj_lists] 

         # return a list of all OUT nodes
        list_out_nodes = graph.keys()

        # Union of in-nodes and out-nodes = all the nodes in the graph
        list_all_nodes = set(list_in_nodes + list_out_nodes) 

        for node in list_all_nodes:
            total = total + list_in_nodes.count(node)
        return total

    def computeTotalInDegree(self,graph):
        return len(graph[1])

    def runTrial(self,tot_in_degree):
        in_degree = dict()
        for node in self.node_numbers[0]:
            in_degree[node] = 1
 
        for (_, n) in self.node_numbers[1]:
            in_degree[n] += 1

        list_probability = list(map(lambda x: float(x)/float(tot_in_degree + len(self.node_numbers[0])),in_degree.values()))
        return np.random.choice(list(self.node_numbers[0]),self.num_nodes,p = list_probability)



p = DPATrial(12)
n = 4470
tot_in_deg=0
for k in range (p.num_nodes,n):
    tot_in_deg = p.computeTotalInDegree(p.node_numbers)
    V_1 = p.runTrial(tot_in_deg)
    p.node_numbers[0].add(k)
    for node in V_1:
        p.node_numbers[1].add((k,node))
    print k
print tot_in_deg
in_degree = dict()
V = p.node_numbers[0]
E = p.node_numbers[1]
for node in V:
    in_degree[node] = 0

for (_, n) in E:
    in_degree[n] += 1

#Calcolo la distribuzione dell'in-degree
distribution = np.zeros(27770)
for node in in_degree:
    distribution[in_degree[node]] += 1

#Normalizzazione
distribution = list(map(lambda x : x/27770, distribution))

pyp.loglog(distribution)
pyp.show()