import numpy as np
from collections import defaultdict
import itertools
import random
import sys

def dictGenerator():
    n = 200#len(matrix)
    dictionary = dict()
    d = []
    pi = []
    dictionary[1] = [x+1 for x in range(n)]
    d.append(None)  #valore della soluzione
    pi.append(None)
    for i in range(2,n+1):
        l = [x for x in range (1,n+1) if x!=1]
        dictionary[i] = []
        for r in range (len(l)+1):
            comb = map(list,itertools.combinations(l,r)) #migliorabile trovando il modo di generare le sole combinazioni con dentro i
            comb = [x for x in comb if i in x]
            dictionary[i].extend(comb)
    #print(dictionary)

dictGenerator()
