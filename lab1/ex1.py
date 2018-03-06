
import utils.buildGraphInDegreeDistribution as bG
from utils.inDegree import inDegree
import numpy
import matplotlib.pyplot as pyp

def buildGraphAdjacencyMatrix(file_name):
    f = open(file_name)
    i = 0
    node_list = []
    for line in f:
        for word in line.split():
            if i == 0:
                from_node_id = word
                
                k = 0
                trovato = False

                while (k < len(node_list) and not trovato):
                    if(from_node_id == node_list[k].id_node):
                        trovato = True
                    k = k + 1

                if (not trovato):
                    x = inDegree(from_node_id,0)
                    node_list.append(x);

                i = i + 1
            else:
                to_node_id = word
                #print(to_node_id)
                j = 0
                trovato = False

                while (j < len(node_list) and not trovato):
                    if(to_node_id == node_list[j].id_node):
                        node_list[j].in_degree = node_list[j].in_degree + 1
                        trovato = True
                    j = j + 1

                if (not trovato):
                    x = inDegree(to_node_id,1)
                    node_list.append(x);

                i = 0
    return node_list


node_list = buildGraphAdjacencyMatrix("Cit-HepTh.txt")
in_degree = bG.buildGraphInDegreeDistribution(node_list,27770)
in_degree = list(map(lambda x: x/27770, in_degree))
pyp.loglog(in_degree)
pyp.show()
