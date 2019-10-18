import math
import numpy as np
import networkx as nx

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
    print "Test1: ", x*P
    print "Test2: ", P**1000



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

findInvDistrib(Pa)
findInvDistrib(Pb)

