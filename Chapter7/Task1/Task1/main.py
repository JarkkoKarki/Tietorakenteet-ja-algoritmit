def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """
    
    # creating visited dict on first run
    if visited is None:
        visited = {u: None}
    # traverse all adjacents
    for v in graph.get_adjacent_vertices(u):
        #check if visited
        if v not in visited:
            #if not visited add the value to the dict
            visited[v] = u
            #recursice call on the vertex
            DFS(graph, v, visited)
    # when all nodes and edges have been visited return the list
    return visited