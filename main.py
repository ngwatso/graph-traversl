def csFindAllPathsFromAToB(graph):
    
    tar = len(graph) - 1
    visited = set()
    res = []
    traversalList = [0]
    currNode = traversalList[0]
    
    csFindAllPathsFromAToBHelper(graph, visited, res, traversalList, currNode, tar)
    return sorted(res)
        
def csFindAllPathsFromAToBHelper(graph, visited, res, traversalList, currNode, tar): 
    if currNode == tar: 
        res.append(traversalList)
        return
    neighbors = graph[currNode]
    for i in neighbors: 
        if i not in visited: 
            csFindAllPathsFromAToBHelper(graph, visited, res, traversalList + [i], i, tar)