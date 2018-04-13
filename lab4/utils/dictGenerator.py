import itertools
from collections import defaultdict
import time as T

def dictGenerator(n):
    dictionary = {}
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
    Tp = T.time()
    combination = []
    for r in range (len(l)+1):
        #print(list(itertools.combinations(l,r)))
        combination.extend(map(list,itertools.combinations(l,r)))
    #filtro le combinazioni che hanno i al loro interno
    #print("_______")
    #print(combination)
    #print("_____")
    #print("First part o dict generated in ", T.time() - Tp)
    Ts = T.time()
    for i in range(2,n+1):
        dictionary[i] = []
        comb = [x for x in combination if i in x]
        dictionary[i].extend(comb)
    #print("FINAL: \n",dictionary)
    #print("Second part o dict generated in ", T.time() - Ts)

    return dictionary

def dictGenerator2(n):
    struct = defaultdict(list)
    struct[1] = [i+1 for i in range(n)]

    d = []
    pi = []
    d.append(None)  #valore della soluzione
    pi.append(None)

    for i in range(2,n+1):
        struct[i].extend([[i]]) # prima combinazione di lunghezza 1
        for j in range(1,n):
            struct[i].extend(generateSpecialComb(struct,j,i,n))
    #print ("FINAL: \n", struct)
    
  
    

# genera le combinazioni di lunghezza l che non contengono il nodo di partenza 
# e che contengono il nodo node
def generateSpecialComb(struct,l,node,n):
    L = [i+1 for i in range(n)]
   # print("lunghezza L", len(L),"List: ",L,"£ deleting", node)
    L.pop(node-1)
    L.pop(0)
    #print("Lista di appoggio per il nodo ",node," = ",L)
    #print("COMB DI LUNGHEZZA ",l," per il nodo ", node," fino a ",n)
    #print ("Lista di aiuto",L)
    list_of_lists = list()
    list_to_append = list()
    for comb in itertools.combinations(L,l):
        list_to_append = [node]
        list_to_append.extend(list(comb))
        list_of_lists.append(list_to_append)
        #list_to_append.extend(list(comb))
        #list_to_append.append(node)
        #list_to_append.extend(list(comb).append(node))
    #print("Final list: ",list_of_lists,"\n")
    return list_of_lists
            



n = 18
print("n = ",n,"\n")

print("dictGenerator1 computing ...\n")
t0 = T.time()
dictGenerator(n)
print("=> dictGenerator1 has computed in ", T.time() - t0," <=\n")

#print("dictGenerator2 computing ...\n")
t1 = T.time()
dictGenerator2(n)
print("=> dictGenerator2 has computed in ", T.time() - t1," <=")