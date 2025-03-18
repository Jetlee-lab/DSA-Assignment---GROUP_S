
 # Importing function caching for optimization. Iru_cache helps  to cache the results of function calls.functools: 
# functools is a Python module that provides tools to work with higher-order functions—functions that act on or return other functions.
from functools import lru_cache 

# we are using Infinity to represent no direct path between cities
# inf means  infinite distance or no connection
INF = float('inf')

# Adjacency matrix representing the distances between cities
graph = [
    [0, 12, 10, INF, INF, INF, 12],  # City 1
    [12, 0, 8, 12, INF, INF, INF],   # City 2
    [10, 8, 0, 11, 3, INF, 9],     # City 3
    [INF, 12, 11, 0, 11, 10, INF],  # City 4
    [INF, INF, 3, 11, 0, 6, 7],     # City 5
    [INF, INF, INF, 10, 6, 0, 9],  # City 6
    [12, INF, 9, INF, 7, 9, 0]     # City 7
]

num_cities = len(graph)  # Total number of cities (7)

# Memoization table using Least Recently Used (LRU) Cache
#@lru_cache(None): it means there is no limit on the size of the cache.
@lru_cache(None)
def tsp(current_city, visited_mask):
    """
    Recursively computes the minimum cost of visiting all cities exactly once
    and returning to the starting city.
    
    Parameters:
    - current_city: The current city index
    - visited_mask: A bitmask representing visited cities
    
    Returns:
    - Minimum cost to complete the tour
    """
    
    # Base case: If all cities have been visited (bitmask is full), return cost to start city
    if visited_mask == (1 << num_cities) - 1:
        return graph[current_city][0]  # Return cost to return to the start city (City 1)

    min_cost = INF  # Initialize minimum cost as infinity

    # Try visiting every unvisited city next
    for next_city in range(num_cities):
        # Checking if next_city is already visited
        if visited_mask & (1 << next_city):#it checks if this city is already visited
            continue  # Skip already visited cities

        # Calculating cost if we go to next_city
        new_visited_mask = visited_mask | (1 << next_city)  # Marking next_city as visited
        cost = graph[current_city][next_city] + tsp(next_city, new_visited_mask)

        # Updating minimum cost if we found a better path
        min_cost = min(min_cost, cost)

    return min_cost  # Returns the minimum travel cost

# Starting TSP from city 0 (City 1), with only City 1 visited
min_tour_cost = tsp(0, 1)

# Print the minimum cost to complete the TSP tour
print("Minimum TSP Tour Cost:", min_tour_cost)
