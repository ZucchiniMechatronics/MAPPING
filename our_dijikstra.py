def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """    
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    graph = {'a1': {'b1': 1},
            'a2': {'a1': 1},
            'a3': {'b3': 1,'a2': 1},
            'a4': {'b4': 1},
            'b1': {'c1': 1},
            'b2': {'a2': 1},
            'b3': {'c3': 1},
            'b4': {'a4': 1},
            'c1': {'d1': 1, 'f1': 1},
            'c2': {'b2': 1},
            'c3': {'d3': 1, 'f3': 1},
            'c4': {'b4': 1},
            'd1': {'d2': 1, 'f1': 1},
            'd2': {'d3': 1, 'f3': 1},
            'd3': {'d4': 1},
            'd4': {'c4': 1},
            'e1': {'f1': 1},
            'e2': {'e1': 1},
            'e3': {'e2': 1, 'f3': 1, 'c2': 1},
            'e4': {'e3': 1},
            'f1': {'g1': 1},
            'f2': {'d3': 1, 'c2': 1, 'e2': 1},
            'f3': {'g3': 1},
            'f4': {'e4': 1, 'c4': 1},
            'g1': {'i1': 1},
            'g2': {'f2': 1},
            'g3': {'h2': 1, 'i3': 1},
            'g4': {'f4': 1},
            'h1': {'i4': 1},
            'h2': {'h1': 1},
            'h3': {'h2': 1, 'i3': 1},
            'h4': {'h3': 1},
            'i1': {'j1': 1},
            'i2': {'g2': 1, 'h2': 1},
            'i3': {'j3': 1},
            'i4': {'h4': 1, 'g4': 1},
            'j1': {'k1': 1},
            'j2': {'i2': 1},
            'j3': {'k3': 1},
            'j4': {'i4': 1},
            'k1': {'k2': 1},
            'k2': {'j2': 1, 'k3': 1},
            'k3': {'k4': 1},
            'k4': {'j4': 1}}
    
             
    dijkstra(graph,'a3','a1')
