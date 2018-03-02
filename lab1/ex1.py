from utils.inDegree import inDegree 

def buildGraphAdjacencyMatrix(file_name):
    f = open(file_name)
    i = 0
    node_list = []
    for line in f:
        for word in line.split():
           if i == 0:
               from_node_id = word
               i = i + 1
           else:
               to_node_id = word
               j = 0 
               if(isInTheList(to_node_id,node_list)):
                   node_list[j].inDegree = node_list[j].inDegree + 1
               else:
                    
               i = 0


def isInTheList(id,node_list):
    j = 0
    while j < len(node_list):
        if(id == node_list[j].id_node)
            return True
    return False 


    
buildGraphAdjacencyMatrix("Cit-HepTh.txt")

