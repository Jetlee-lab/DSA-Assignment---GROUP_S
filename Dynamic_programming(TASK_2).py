from itertools import permutations

# Define the Cities/Nodes of the graph
nodes = ('1', '2', '3', '4', '5', '6', '7')

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

# Create an adjacency matrix initialized to infinity
adjacency_matrix = [
    [0 if i == j else float('inf') for i in range(num_nodes)]
    for j in range(num_nodes)
]
# Populate the adjacency matrix with the weights of the edges
for edge in edges:
    i = nodes.index(edge[0])
    j = nodes.index(edge[1])
    weight = edge[2]
    adjacency_matrix[i][j] = weight
    adjacency_matrix[j][i] = weight # Since it's bidirectional

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

# Classical TSP solution using dynamic programming (Held-Karp algorithm)
def tsp_dp(graph,n):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0 # Start at City 1.

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i): # If City i is visited.
                for j in range(n):
                    if mask & (1 << j) and i != j: # If City j is visited and i is not equal to j.
                        dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + graph[j][i])

    # Returning to start
    last_mask = (1 << n) - 1
    return min(dp[last_mask][i] + graph[i][0] for i in range(1, n))

# Solve the TSP problem using the constructed adjacency matrix
print("\nMinimium cost of TSP:", tsp_dp(adjacency_matrix,num_nodes))