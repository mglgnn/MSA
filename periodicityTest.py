import math
import numpy as np
import networkx as nx


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





# a subcycle is a cycle entirely contained in some other cycle with len(longer) mod len(shorter) != 0
def isSubcycle(shortCycle, longCycle):
    print "test isSubcycle"

    j = 0
    for i in range(0, len(longCycle)):
        if shortCycle[j] == longCycle[i]:
            j += 1
            if j == len(shortCycle):
                print shortCycle, " in ", longCycle
                return True

    print shortCycle, " not in ", longCycle
    return False


# cycles is already sorted so comparisons are required from id upwards only
def isPeriodic(id, cycles):
    print "test isPeriodic"

    for i in range(id+1, len(cycles)):
        if isSubcycle(cycles[id], cycles[i]) == True:
            print "cycle ", id, " is subcycle of ", i
            return False
    print "cycle ", id, " is subcycle of none"
    return True

def testNetwork(P):
    # Create Directed Graph
    G=nx.DiGraph()

    


    # Add a list of nodes:
    G.add_nodes_from(range(0,len(P)))
    
    # Add a list of edges:
    for i in range(0,len(P)):
        for j in range(0,len(P)):
            if P[i,j]>0:
                G.add_edge(i,j)

    #Return a list of cycles sorted according to their length 
    cycles = list(nx.simple_cycles(G))
    cycles.sort(key=len)

    for i in range(0,len(cycles)) :
        isPeriodic(i,cycles)
    
    print cycles





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
isIrreducible(Pa)
isIrreducibleMC(Pa)
isIrreducible(Pb)
isIrreducibleMC(Pb)
    
'''
print "test network A:"
testNetwork(Pa)
print "test network B:"
testNetwork(Pb)
'''

