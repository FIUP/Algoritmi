def DFSVisited(graph,u,visited,color):
    color[u] = "gray"
    visited.append(u)
    for v in graph.adj_list[u]:
        if (color[v] == "white"):
            visited = DFSVisited(graph,v,visited,color)
    color[u] = "black"
    return visited


def maxCC(graph):
    color = dict()
    for i in graph.adj_list.keys():
        color[i] = "white"
    CC = []
    for i in graph.adj_list.keys():
        if (color[i] == "white"):
            comp = DFSVisited(graph,i,[],color)
            CC.append(comp)
    if not CC:
        return 0
    return max(len(l) for l in CC)
