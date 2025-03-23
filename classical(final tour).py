from functools import lru_cache

# Infinity to represent no direct path between cities
INF = float('inf')

# Adjacency matrix representing distances between cities
graph = [
    [0, 12, 10, INF, INF, INF, 12],  # City 1
    [12, 0, 8, 12, INF, INF, INF],   # City 2
    [10, 8, 0, 11, 3, INF, 9],       # City 3
    [INF, 12, 11, 0, 11, 10, INF],   # City 4
    [INF, INF, 3, 11, 0, 6, 7],      # City 5
    [INF, INF, INF, 10, 6, 0, 9],    # City 6
    [12, INF, 9, INF, 7, 9, 0]       # City 7
]

num_cities = len(graph)  # Total number of cities (7)cls


# Memoization table using Least Recently Used (LRU) Cache
@lru_cache(None)
def tsp(current_city, visited_mask):
    """
    Recursively computes the minimum cost and path of visiting all cities exactly once.
    
    Parameters:
    - current_city: The current city index
    - visited_mask: A bitmask representing visited cities
    
    Returns:
    - (min_cost, path): Minimum cost and the optimal path to complete the tour
    """
    # Base case: If all cities have been visited, return cost to start city
    if visited_mask == (1 << num_cities) - 1:
        return graph[current_city][0], [current_city]  # Return cost and path to start city
    
    min_cost = INF
    best_path = []

    # Try visiting every unvisited city
    for next_city in range(num_cities):
        if visited_mask & (1 << next_city):  # Skip already visited cities
            continue

        # Calculate new visited mask and cost
        new_visited_mask = visited_mask | (1 << next_city)
        cost_to_next, path_to_next = tsp(next_city, new_visited_mask)

        # Update minimum cost and path
        new_cost = graph[current_city][next_city] + cost_to_next
        if new_cost < min_cost:
            min_cost = new_cost
            best_path = [current_city] + path_to_next

    return min_cost, best_path

# Start TSP from city 0 (City 1), with only City 1 visited
min_tour_cost, optimal_path_indices = tsp(0, 1)

# Convert path indices to city names
optimal_path_names = [f"City {i+1}" for i in optimal_path_indices]

# Print the minimum cost and optimal route
print("Minimum TSP Tour Cost:", min_tour_cost)
print("Optimal Route:", " -> ".join(optimal_path_names))
