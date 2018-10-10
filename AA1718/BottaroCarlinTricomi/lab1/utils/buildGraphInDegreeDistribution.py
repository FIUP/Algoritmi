import numpy

def buildGraphInDegreeDistribution(node_list, totNodes):
    distribution = numpy.zeros(totNodes)
    for node in node_list:
        distribution[node.in_degree] = distribution[node.in_degree] + 1

    return distribution
