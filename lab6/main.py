from utils.readFromFile import *
from utils.closestPairAlgorithm import *
from utils.clusteringAlgorithm import *
from createGraph import *

def maxPopulation(k, dataSet):
    Cp, C = [], []
    for i in dataSet.keys():
        Cp.append((i,dataSet[i][0]))

    Cp = sorted(Cp,key = lambda people: people[1],reverse = True)
    Cp = Cp[:k]
    for el in Cp:
        C.append(el[0])

    return C

#creazione data-set
minDataSet = readFromFile("data/unifiedCancerData_111.csv")
mediumDataSet = readFromFile("data/unifiedCancerData_290.csv")
maxDataSet = readFromFile("data/unifiedCancerData_896.csv")
completeDataSet = readFromFile("data/unifiedCancerData_3108.csv")



'''#Domanda1
k = 15 #number of cluster
q = 5 # number of iteration in k-means clustering
P = completeDataSet.keys()

hierarchical_clusters_dict = hierarchicalClustering(P,k)
# print("Hierarchical: \n",hierarchical_clusters_dict)

ClusterGraph(hierarchical_clusters_dict)
#Domanda2
#Costruisco la lista dei centri = sono le 15 coordinate con la popolazione maggiore

C = maxPopulation(k,completeDataSet)

# Clustering K-means
kmeans_clusters_dict = KMeansClustering(P,C,k,q)

ClusterGraph(kmeans_clusters_dict)'''

'''#Domanda4
k = 9
q = 5
P = list(minDataSet.keys())


hierarchical_clusters_dict = hierarchicalClustering(P,k)
ClusterGraph(hierarchical_clusters_dict)

#Domanda5
C = maxPopulation(k, minDataSet)
#ClusterGrap(C)

kmeans_clusters_dict = KMeansClustering(P,C,k,q)

ClusterGraph(kmeans_clusters_dict)

#Domanda6
error_hierarchical = clusterDistortion(hierarchical_clusters_dict, minDataSet)
error_kmeans = clusterDistortion(kmeans_clusters_dict, minDataSet)

print(error_hierarchical, "hier")
print(error_kmeans, "kmeans")'''

#Domanda9
q = 5
pMin = list(minDataSet.keys())
pMed = list(mediumDataSet.keys())
pMax = list(maxDataSet.keys())

hMin = []
hMed = []
hMax = []
kMin = []
kMed = []
kMax = []

for k in range(6,21):
    hierarchical_clusters_dict1 = hierarchicalClustering(pMin,k)
    error_hierarchical1 = clusterDistortion(hierarchical_clusters_dict1, minDataSet)
    hMin.append(error_hierarchical1)
    print("K = ",k," Hierarchical min error ",error_hierarchical1)

    hierarchical_clusters_dict2 = hierarchicalClustering(pMed,k)
    error_hierarchical2 = clusterDistortion(hierarchical_clusters_dict2, mediumDataSet)
    hMed.append(error_hierarchical2)
    print("K = ",k," Hierarchical med error ",error_hierarchical2)

    hierarchical_clusters_dict3 = hierarchicalClustering(pMax,k)
    error_hierarchical3 = clusterDistortion(hierarchical_clusters_dict3, maxDataSet)
    hMax.append(error_hierarchical3)
    print("K = ",k," Hierarchical max error ",error_hierarchical3)

    C = maxPopulation(k, minDataSet)

    kmeans_clusters_dict1 = KMeansClustering(pMin,C,k,q)
    error_kmeans1 = clusterDistortion(kmeans_clusters_dict1, minDataSet)
    kMin.append(error_kmeans1)
    print("K = ",k," Kmeans min error ",error_kmeans1)

    C = maxPopulation(k, mediumDataSet)

    kmeans_clusters_dict2 = KMeansClustering(pMed,C,k,q)
    error_kmeans2 = clusterDistortion(kmeans_clusters_dict2, mediumDataSet)
    kMed.append(error_kmeans2)
    print("K = ",k," Kmeans med error ",error_kmeans2)

    C = maxPopulation(k, maxDataSet)

    kmeans_clusters_dict3 = KMeansClustering(pMax,C,k,q)
    error_kmeans3 = clusterDistortion(kmeans_clusters_dict3, maxDataSet)
    kMax.append(error_kmeans3)
    print("K = ",k," Kmeans max error ",error_kmeans3)

errorFunction(hMin,kMin)
errorFunction(hMed,kMed)
errorFunction(hMax,kMax)
