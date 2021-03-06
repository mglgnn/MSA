import math
import numpy as np
import networkx as nx
from fractions import gcd
from functools import reduce


# https://stackoverflow.com/questions/29194588/python-gcd-for-list
def find_gcd(list):
    x = reduce(gcd, list)
    return x

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

def isPeriodicVertex(id, cycles):
    L = []
    for period in cycles:
        if id in period:
            L.append(len(period))

    print "List of lengths of all periods containing vertex ", id, ":", L

    if find_gcd(L) == 1:
        return False
    return True

def isPeriodicMC(P):
    # Create Directed Graph from transition matrix
    G = createGraphFromMC(P)

    # create a list of cycles and sort them according to their length 
    cycles = list(nx.simple_cycles(G))
    cycles.sort(key=len)

    print cycles

    isMCperiodic = False

    for i in range(0, G.number_of_nodes()) :
        if isPeriodicVertex(i,cycles) == True:
            print "vertex ", i, " is periodic"
            isMCperiodic = True
    
    return isMCperiodic





# main
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

print "----test network A:"
if isPeriodicMC(Pa) == True:
    print "PERIODIC"
else:
    print "APERIODIC"
    
print "----test network B:"
if isPeriodicMC(Pb) == True:
    print "PERIODIC"
else:
    print "APERIODIC"

