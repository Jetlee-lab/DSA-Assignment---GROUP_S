
# Define the nodes  of the graph
nodes = ('1', '2', '3', '4', '5', '6', '7')

# edges = (
#     ('1', '2'), ('1', '3'), ('1', '7'),
#     ('2', '1'), ('2', '3'), ('2', '4'),
#     ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('3', '7'),
#     ('4', '2'), ('4', '3'), ('4', '5'), ('4', '6'),
#     ('5', '3'), ('5', '4'), ('5', '6'), ('5', '7'),
#     ('6', '4'), ('6', '5'), ('6', '7'),
#     ('7', '1'), ('7', '3'), ('7', '5'), ('7', '6'),
# )

# Define the edges and corresponding weights of the graph
edges = (
    ('1', '2', 12), ('1', '3', 10), ('1', '7', 12),
    ('2', '3', 8), ('2', '4', 12),
    ('3', '4', 11), ('3', '5', 3), ('3', '7', 9),
    ('4', '5', 11), ('4', '6', 10),
    ('5', '6', 6), ('5', '7', 7),
    ('6', '7', 9),
)

# Get the number of nodes
num_nodes = len(nodes)

# Create an adjacency matrix initialized to 0
adjacency_matrix = [
    [0 if i == j else float('inf') for i in range(num_nodes)]
    for j in range(num_nodes)
]

for edge in edges:
    # Get the source and destination node
    i = nodes.index(edge[0])
    j = nodes.index(edge[1])
    weight = edge[2]

    # Add the edge to the adjacency matrix
    adjacency_matrix[i][j] = weight
    adjacency_matrix[j][i] = weight


# Print the adjacency matrix
for row in adjacency_matrix:
    print(row)