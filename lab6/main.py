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
q = 5 # number of iteration in k-means clustering
P = [(completeDataSet[x][0]) for x in completeDataSet.keys()]

hierarchical_clusters_dict = hierarchicalClustering(P,k)
print("Hierarchical: \n",hierarchical_clusters_dict)

for i in hierarchical_clusters_dict.keys():
    if not hierarchical_clusters_dict[i]:
        print("\n-- Cluster with center",i," is empty. --")

#Costruisco la lista dei centri = sono le 15 coordinate con la popolazione maggiore
Cp, C = [], []
for i in completeDataSet.keys():
    Cp.append((completeDataSet[i][0],completeDataSet[i][1]))

Cp = sorted(Cp,key = lambda people: people[1],reverse = True)
Cp = Cp[:k]
for el in Cp:
    C.append(el[0])

# Clustering K-means
kmeans_clusters_dict = KMeansClustering(P,C,k,q)
print("\nK-Means: \n",kmeans_clusters_dict)

for k in kmeans_clusters_dict.keys():
    if not kmeans_clusters_dict[k]:
        print("\n-- Cluster with center",k," is empty. --")


