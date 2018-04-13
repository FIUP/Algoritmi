import itertools
from collections import defaultdict
import time as T
from memory_profiler import memory_usage
from sys import getsizeof as memoryUsage
def dictGenerator(n):
    mem = 0
    dictionary = defaultdict(list)
    d = []
    pi = []
    #prendo 1 come nodo iniziale, con unica combinazione: tutti i nodi
    dictionary[1] = [x+1 for x in range(n)]
    #print(dictionary)
    #print("----")
    d.append(None)  #valore della soluzione
    pi.append(None)
    #lista da dove generare le combinazioni
    l = [x for x in range (2,n+1)]
    #print(l)
    #print("--------")
    #creo tutte le combinazioni
    combination = []
    for r in range (n):
        #print(list(itertools.combinations(l,r)))
        combination.extend(map(list,itertools.combinations(l,r)))

    for i in range(2,n+1):
        dictionary[i] = []
        comb = [x for x in combination if i in x]
        dictionary[i].extend(comb)
    print("This fun has used ",(memoryUsage(comb) + memoryUsage(dictionary) + memoryUsage(combination))/1024, " KB")
    return dictionary

def dictGenerator2(n): # più veloce di quella originale e utilizza un po meno memoria
    struct = defaultdict(list)
    d = []
    pi = []
    struct[1] = [x+1 for x in range(n)]
    for i in range(2,n+1):
        struct[i].append([i])
    #print(struct)
    #print("----")
    d.append(None)  #valore della soluzione
    pi.append(None)
    #lista da dove generare le combinazioni
    L = [x for x in range (2,n+1)]
    #print(l)
    #print("--------")
    #creo tutte le combinazioni
    combination = []
    for l in range (n-1):
        #print(list(itertools.combinations(l,r)))
        combination.extend(map(list,itertools.combinations(L,l+2)))
    #filtro le combinazioni che hanno i al loro interno
    #print("_______")
    
    #print(combination)
    #print("_____")
    #print("First part o dict generated in ", T.time() - Tp)
    Ts = T.time()
    for i in range(2,n+1):
        comb = [x for x in combination if i in x]
        struct[i].extend(comb)
    #print("FINAL: \n",struct)
    #print("Second part o dict generated in ", T.time() - Ts)
    print("This fun has used ",(memoryUsage(comb) + memoryUsage(struct) + memoryUsage(combination)) / 1024, " KB")
    return struct


''' molto lenta, ma usa il 30% in meno della memoria delle altre due'''
def dictGenerator3(n):
    struct = defaultdict(list)
    d = []
    pi = []
    struct[1] = [x+1 for x in range(n)]
    for i in range(2,n+1):
        struct[i].append([i])
    #print(struct)
    #print("----")
    d.append(None)  #valore della soluzione
    pi.append(None)
    #lista da dove generare le combinazioni
    L = [x for x in range (2,n+1)]
    #print(l)
    #print("--------")
    #creo tutte le combinazioni
    combination = []
    for l in range (n-1):
        #print(list(itertools.combinations(l,r)))
        combination.extend(map(list,itertools.combinations(L,l+2)))
    #filtro le combinazioni che hanno i al loro interno
    #print("_______")
    
    #print(combination)
    #print("_____")
    #print("First part o dict generated in ", T.time() - Tp)
    Ts = T.time()
    for i in range(2,n+1):
        for x in combination:
            find = False
            for el in x:
                if el == i:
                    struct[i].extend([x])
                    break
                if el > i: 
                    break

    #print("FINAL: \n",struct)
    #print("Second part o dict generated in ", T.time() - Ts)
    print("This fun has used ",(memoryUsage(struct) + memoryUsage(combination)) / 1024, " KB")
    return struct


n = 24

print("n = ",n,"\n")

print("dictGenerator2 computing ...\n")
t0 = T.time()
A = dictGenerator2(n)
second_version = T.time() - t0
print("=> dictGenerator2 has computed in ", second_version," <=\n")

print("dictGenerator computing ...\n")
t1 = T.time()
B = dictGenerator(n)
first_version = T.time() - t1
print("=> dictGenerator has computed in ", first_version," <=")

if first_version > second_version:
    print("Generator2 is faster")
else:
    print("Generator1 is faster")

if A == B:
    print("EQUALS")
else:
    print("DIFFERENT")


