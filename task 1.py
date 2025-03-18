import numpy as np # this imports NumPy library which supports arrays and matricies along with a large collection of mathematical functions
NULL=float("inf")#represents no direct path or infinite distance
#creating the Adjacent matrix
graph_of_cities=[
    [0,12,10,NULL,NULL,NULL,12],
    [12,0,8,12,NULL,NULL,NULL],
    [10,8,0,11,3,NULL,9],
    [NULL,12,11,0,11,10,NULL],
    [NULL,NULL,3,11,0,6,7],
    [NULL,NULL,NULL,10,6,0,9],
    [12,NULL,9,NULL,7,9,0]
]
#This creates a 2Dmatrix representing the adjacency of the graph. 
#Each element graph[i][j] represents the weight of the edge between the nodes of the cities
# if there is no direction, the value is NULL
print(np.array(graph_of_cities))