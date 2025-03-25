# Description: This is a Python program that solves the Traveling Salesman Problem (TSP) using dynamic programming and memoization. 
            # The program finds the minimum cost and path to visit all cities exactly once and return to the starting city. 
            # The program uses an adjacency matrix to represent distances between cities and memoization to optimize the recursive solution.
            # The program also modifies the optimal path to include a specific city after another city in the path.

# Importing function caching for optimization. Iru_cache helps  to cache the results of function calls.functools: 
# functools is a Python module that provides tools to work with higher-order functions—functions that act on or return other functions.
from functools import lru_cache 

# we are using Infinity to represent no direct path between cities
# inf means  infinite distance or no connection
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

num_cities = len(graph)  # Total number of cities (7)

# Memoization table using Least Recently Used (LRU) Cache
#@lru_cache(None): it means there is no limit on the size of the cache.
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
    if visited_mask == (1 << num_cities) - 1: # Check if all cities have been visited
        return graph[current_city][0], [current_city]  # Return cost and path to start city
    
    min_cost = INF # Initialize minimum cost as infinity
    best_path = [] # Initialize the best path as an empty list

    # Try visiting every unvisited city
    for next_city in range(num_cities): # Loop through all cities
        if visited_mask & (1 << next_city):  # Skip already visited cities
            continue # Skip if city has already been visited

        # Calculate new visited mask and cost
        new_visited_mask = visited_mask | (1 << next_city) # Mark next city as visited
        cost_to_next, path_to_next = tsp(next_city, new_visited_mask) # Recursively find cost and path

        # Update minimum cost and path
        new_cost = graph[current_city][next_city] + cost_to_next # Calculate new cost
        if new_cost < min_cost: # Check if new cost is less than minimum cost
            min_cost = new_cost # Update minimum cost
            best_path = [current_city] + path_to_next # Update best path

    return min_cost, best_path 

# Start TSP from city 0 (City 1), with only City 1 visited
min_tour_cost, optimal_path_indices = tsp(0, 1)

# Convert path indices to city names
optimal_path_names = [f"City {i+1}" for i in optimal_path_indices]

# Modify the route to include City 1 at the end after City 3
if 2 in optimal_path_indices:  # Ensure City 3 is in the path
    index_city_3 = optimal_path_indices.index(2)  # Get index of City 3
    optimal_path_indices = optimal_path_indices[:index_city_3 + 1] + [0]  # Add City 1 after City 3

# Convert the modified path back to city names
modified_path_names = [f"City {i+1}" for i in optimal_path_indices]

# Print the minimum cost and modified optimal route
print("Minimum TSP Tour Cost:", min_tour_cost)
print("Optimal Route:", " -> ".join(modified_path_names))
