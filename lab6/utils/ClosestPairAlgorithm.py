import math

# calcola la distanza tra p1 e p2
def calcDistance(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return math.pow(math.pow(x2-x1,2) + math.pow(y2-y1,2),0.5)

# ritorna gli indici (cioè i centri) dei due cluster più vicini
# i due cluster più vicini sono quelli con la distanza minore tra i due centri
# in input vuole la lista dei centri
def slowClosestPair(center_list):
    inf = math.inf
    (d,i,j) = (inf,-1,-1)
    n = len(center_list)

    for w in range(n): # confronto ogni centro con tutti gli altri centri. (n*(n+1) / 2) iterazioni e non n*(n-1)
        c1 = center_list[w]
        for z in range(w+1,n): # controllo se w + 1 < n ? non dovrebbe servire
            c2 = center_list[z]
            (d,i,j) = min((d,i,j), (calcDistance(c1,c2),c1,c2))

    return (d,i,j)


def fastClosestPair(center_list):
    

    return (0,True, True)
