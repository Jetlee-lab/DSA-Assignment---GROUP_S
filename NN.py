import numpy as np
# Define the distance matrix based on Figure 1
# use comments to explain the code

distances = np.array([
    [0, 10, 15, 20, 25, 30, 35],  # City 1
    [10, 0, 12, 18, 22, 28, 32],  # City 2
    [15, 12, 0, 10, 14, 20, 25],  # City 3
    [20, 18, 10, 0, 8, 15, 20],   # City 4
    [25, 22, 14, 8, 0, 10, 12],  # City 5
    [30, 28, 20, 15, 10, 0, 8],   # City 6
    [35, 32, 25, 20, 12, 8, 0]    # City 7
])

# Function to find the shortest path using NearestNeighbors algorithm
def nearest_neighbor_path(distance,start_city):
    # Initialize the visited array with False values
    num_cities = len(distances)
    visited = np.full(num_cities, False)
    tour =[start_city]
    current_city = start_city
    visited[start_city] = True
    total_distance =0
    
    current_city =start_city
    for _ in range(num_cities - 1):
        nearest_city = np.argmin(distance[current_city][visited == False])
        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += distance[current_city][nearest_city]
        current_city = nearest_city

# return to the starting city
    tour.append(start_city)
    total_distance += distance[current_city][start_city]
    
    return tour, total_distance

# find the shortest route

start_city = 0  # City 1
tour, total_distance = nearest_neighbor_path(distances, start_city)
tour, total_distance

# start at the beginning

start_city = 0
tour, total_distance = nearest_neighbor_path(distances, start_city)
tour, total_distance

print("Tour: ", [city+1 for city in tour])

print("Total Distance: ", total_distance)

# usage information

print("Usage: Call nearest_neighbor_path(distances, start_city) where distances is the distance matrix and start_city is the starting city index.")






        
        
        
