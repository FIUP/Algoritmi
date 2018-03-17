import itertools
import random
from collections import defaultdict

class generateUndirectedGraphER:
    # params
    # n: numero di nosi
    # p: probabilita che un certo nodo venga estratto
    def __init__(self,n,p):
        if p >= 0 and p <= 1:
            self.n = n
            self.p = p
            self.V = set(range(n))
            self.adj_list = defaultdict(set)

            # Sia V = {0,1,2}. Questo ciclo itera solo sulle coppie (0,1), (0,2) e (1,2)
            # e non sulle stesse coppie invertite (1,0), (2,0), (2,1), dimezzando cosi le iterazioni
            for pairs in itertools.combinations(self.V,2):
                # print("Coppie: ",pairs)
                if random.random() < p and pairs[0] != pairs[1]:
                    self.adj_list[pairs[0]].add(pairs[1])
                    self.adj_list[pairs[1]].add(pairs[0])
            # print self.V
            # print self.E
        else:
            print ("Error: p must be in [0,1]")

# generateUndirectedGraphER(3,1).adj_list
