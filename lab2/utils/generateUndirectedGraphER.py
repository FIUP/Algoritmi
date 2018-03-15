from generateUndirectedGraphFromFile import generateUndirectedGraphFromFile
import itertools
import random
 
class generateUndirectedGraphER:
    # params
    # n: numero di nosi
    # p: probabilita che un certo nodo venga estratto
    def __init__(self,n,p):
        if p >= 0 and p <= 1:
            self.n = n
            self.p = p
            self.V = set(range(n))
            self.E = set()
            for pairs in itertools.combinations(self.V,2):
                if random.random() < p and pairs[0] != pairs[1]:
                    self.E.add(pairs)
            # print self.V
            # print self.E
        else:
            print "Error: p must be in [0,1]"

# generateUndirectedGraphER(4,0.3)