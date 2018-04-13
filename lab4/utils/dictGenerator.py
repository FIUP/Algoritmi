import itertools

def dictGenerator(n):
    dictionary = {}
    d = []
    pi = []
    #prendo 1 come nodo iniziale, con unica combinazione: tutti i nodi
    dictionary[1] = [x+1 for x in range(n)]
    d.append(None)  #valore della soluzione
    pi.append(None)
    #lista da dove generare le combinazioni
    l = [x for x in range (2,n+1)]
    #creo tutte le combinazioni
    combination = []
    for r in range (len(l)+1):
        combination.extend(map(list,itertools.combinations(l,r)))
    #filtro le combinazioni che hanno i al loro interno
    for i in range(2,n+1):
        dictionary[i] = []
        comb = [x for x in combination if i in x]
        dictionary[i].extend(comb)
    print(dictionary)
    return dictionary

#dictGenerator()
