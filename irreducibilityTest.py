import math
import numpy as np
import networkx as nx


def DFSrec(G,v,visited): 
    visited[v]= True

    for i in list(G.neighbors(v)): 
        if visited[i]==False: 
            DFSrec(G, i, visited) 

def DFS(G, startAt):
    visited = [False]*(G.number_of_nodes())
    DFSrec(G,startAt,visited)

    if any(i == False for i in visited): 
        return False

    return True

def isStronglyConnected(G):
    if DFS(G,0) == False:
        return False

    # returns a graph with the same set of nodes and edges of G but having all directions inverted
    T = G.reverse(True)
    return DFS(T,0)



def createGraphFromMC(P):
    # Create Directed Graph
    G=nx.DiGraph()

    # Add a list of nodes:
    G.add_nodes_from(range(0,len(P)))
    
    # Add a list of edges:
    for i in range(0,len(P)):
        for j in range(0,len(P)):
            if P[i,j]>0:
                G.add_edge(i,j)
    
    return G


def isIrreducibleMC(P):
    G = createGraphFromMC(P)
    print "MC is irreducible" if isStronglyConnected(G) else "MC is NOT irreducible"





#main
Pa = np.matrix( 
(
(0,0.5,0.5,0,0,0,), 
(1,0,0,0,0,0),
(0,0.9,0,0.1,0,0),
(0,0,0,0,1,0),
(0,0,0,0,0,1),
(0,0,0,1,0,0)
) 
)

Pb = np.matrix( 
(
(0,0.5,0.5,0,0,0,), 
(1,0,0,0,0,0),
(0,0.9,0,0.1,0,0),
(0,0,0,0,1,0),
(0,0,0,0,0,1),
(0.5,0,0,0.5,0,0)
) 
)

print "MC A:"
isIrreducibleMC(Pa)
print "MC B:"
isIrreducibleMC(Pb)
  

