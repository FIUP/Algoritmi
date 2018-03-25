from .generateUndirectedGraphFromFile import generateUndirectedGraphFromFile
from .generateUndirectedGraphER import generateUndirectedGraphER
from .generateUPAGraph import generateUPAGraph

class graphGenerator:
    def __init__(self,path,n,p,m):
        self.graph_from_file = generateUndirectedGraphFromFile(path)
        self.ER_graph = generateUndirectedGraphER(n,p)
        self.UPA_graph = generateUPAGraph(n,m)
