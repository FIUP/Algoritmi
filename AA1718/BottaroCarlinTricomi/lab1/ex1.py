import numpy as np
import matplotlib.pyplot as pyp

f = np.loadtxt("Cit-HepTh.txt", delimiter="\t")

E = set()
V = set()

# Creo E e V
for line in f:
    V.add(line[0])
    V.add(line[1])
    E.add(tuple(line))

#Calcolo l'in-degree di ogni nodo
in_degree = dict()
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
