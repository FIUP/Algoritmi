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

            for first in self.adj_list.keys():
                for second in self.adj_list.keys():

                    if random.random() < p and first != second:
                        self.adj_list[first].add(second)
                        self.adj_list[second].add(first)

        else:
            print ("Error: p must be in [0,1]")

# generateUndirectedGraphER(3,1).adj_list
