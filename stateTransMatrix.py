import math
import numpy as np
import networkx as nx


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

print "Transition matrix for MC A:"
print Pa
print "Transition matrix for MC B:"
print Pb