from utils.inDegree import inDegree
import numpy
import matplotlib.pyplot as pyp
import tkinter

def buildGraphAdjacencyMatrix(file_name):
    f = open(file_name)
    i = 0
    node_list = []
    for line in f:
        for word in line.split():
            if i == 0:
                from_node_id = word
                i = i + 1
            else:
                to_node_id = word
                print(to_node_id)
                j = 0
                trovato = False

                while (j < len(node_list) and not trovato):
                    if(to_node_id == node_list[j].id_node):
                        node_list[j].in_degree = node_list[j].in_degree + 1
                        trovato = True
                    j = j + 1

                if (not trovato):
                    x = inDegree(to_node_id)
                    node_list.append(x);

                i = 0
    return node_list

def buildGraphInDegreeDistribution(node_list):
    distribution = numpy.zeros(27770)
    for node in node_list:
        distribution[node.in_degree] = distribution[node.in_degree] + 1

    return distribution

def distributionInDegree(in_degree, totNodes):
    for grade in in_degree:
        grade = grade / totNodes



node_list = buildGraphAdjacencyMatrix("Cit-HepTh.txt")
in_degree = buildGraphInDegreeDistribution(node_list)
in_degree = list(map(lambda x: x/27770, in_degree))
pyp.loglog(in_degree)
pyp.show()
