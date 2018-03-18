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
            self.adj_list = defaultdict(set)

            for i in range(n):
                self.adj_list[i] = set()

            for i in range(n):
                for j in range(i,n):

                    if random.random() < p and i != j:
                        self.adj_list[i].add(j)
                        self.adj_list[j].add(i)

        else:
            print ("Error: p must be in [0,1]")

# generateUndirectedGraphER(3,1).adj_list
