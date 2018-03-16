from generateUndirectedGraphFromFile import generateUndirectedGraphFromFile
from generateUndirectedGraphER import generateUndirectedGraphER

class graphGenerator:
    def __init__(self,path,n,p):
        self.graph_from_file = generateUndirectedGraphFromFile(path)
        self.ER_graph = generateUndirectedGraphER(n,p)