def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    
    # start vertex to discovered
    discovered = {start: None}
    #Only vertex in start is the start vertex
    level = {start}
    while level:
        #prepare next_level for next
        next_level = []
        #Iterate the vertices in the level
        for u in level:
            #Iterate the adjacent of the vertex
            for v in graph.get_adjacent_vertices(u):
                #If adjacent not in discovered
                if v not in discovered:
                    #Add adjacent and edge between
                    discovered[v] = u
                    #add adjacent to next level
                    next_level.append(v)
        #advance to the next level
        level = next_level
    return discovered