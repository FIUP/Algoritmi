from utils.readFromFile import *
from utils.closestPairAlgorithm import *
from utils.clusteringAlgorithm import *

#creazione data-set
minDataSet = readFromFile("data/unifiedCancerData_111.csv")
mediumDataSet = readFromFile("data/unifiedCancerData_290.csv")
maxDataSet = readFromFile("data/unifiedCancerData_896.csv")
completeDataSet = readFromFile("data/unifiedCancerData_3108.csv")

#domanda1
k = 15 #number of cluster
P = [(completeDataSet[x][0]) for x in completeDataSet.keys()]

clusters_dict = hierarchicalClustering(P,k)
print(clusters_dict)
