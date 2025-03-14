
# Create an adjacency matrix initialized to 0
# Define the number of cities
num_cities = 7

# Create an adjacency matrix initialized to the given distances
adjacency_matrix = [
    [0, 12, 10, float('inf'), float('inf'), float('inf'), 12],
    [12, 0, 8, 12, float('inf'), float('inf'), float('inf')],
    [10, 8, 0, 11, 3, float('inf'), float('inf')],
    [float('inf'), 12, 11, 0, 11, float('inf'), float('inf')],
    [float('inf'), float('inf'), 3, 11, 0, 10, 7],
    [float('inf'), float('inf'), float('inf'), float('inf'), 10, 0, 9],
    [12, float('inf'), float('inf'), float('inf'), 7, 9, 0]
]

# Print the adjacency matrix
for row in adjacency_matrix:
    print(row)