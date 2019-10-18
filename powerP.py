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



from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
#acknowledgement : https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
      
   
    #A function used by isSC() to perform DFS 
    def DFSUtil(self,v,visited): 
  
        # Mark the current node as visited  
        visited[v]= True
  
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
  
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
          
        return g 
  
          
    # The main function that returns true if graph is strongly connected 
    def isSC(self): 
  
        # Step 1: Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
          
        # Step 2: Do DFS traversal starting from first vertex. 
        self.DFSUtil(0,visited) 
  
        # If DFS traversal doesnt visit all vertices, then return false 
        if any(i == False for i in visited): 
            return False
  
        # Step 3: Create a reversed graph 
        gr = self.getTranspose() 
          
        # Step 4: Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
        # Step 5: Do DFS for reversed graph starting from first vertex. 
        # Staring Vertex must be same starting point of first DFS 
        gr.DFSUtil(0,visited) 
  
        # If all vertices are not visited in second DFS, then 
        # return false 
        if any(i == False for i in visited): 
            return False
  
        return True




def isIrreducible(P):
    g = Graph(len(P))
    
    for i in range(0,len(P)):
        for j in range(0,len(P)):
            if P[i,j] > 0:
                g.addEdge(i,j)

    print "MC is irreducible" if g.isSC() else "MC is NOT irreducible"




# https://stephens999.github.io/fiveMinuteStats/stationary_distribution.html
def findInvDistrib(P):

    I = np.identity(len(P))
    # add condition over pi all entries sum to 1
    newrow = np.ones(len(P))
    A = P
    A = A.transpose()
    A = np.vstack([A-I, newrow])
    print A



    
    B = np.zeros(len(P)+1)
    B[len(P)] = 1

    x, residuals, rank, s = np.linalg.lstsq(A, B)
    print "Solution: ", x
    print "Residuals: ", residuals
    print "Rank: ", rank
    print "Test: ", x*P



'''
    try:
        x = np.linalg.solve(A, B)
        print 'Invariant distribution found'
        print x 
    except np.linalg.LinAlgError as err:
        if 'Singular matrix' in str(err):
            print 'Singular matrix passed'
        else:
            raise
'''




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

