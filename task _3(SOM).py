from math import inf, pi, sin, cos, sqrt, exp
import random

# Set random seed for reproducibility
random.seed(42)

# The adjacency matrix from the problem
adjacency_matrix = [
    [0, 12, 10, inf, inf, inf, 12],  # Node 1-start (index 0)
    [12, 0, 8, 12, inf, inf, inf],   # Node 2 (index 1)
    [10, 8, 0, 11, 3, inf, 9],       # Node 3 (index 2)
    [inf, 12, 11, 0, 11, 10, inf],   # Node 4 (index 3)
    [inf, inf, 3, 11, 0, 6, 7],      # Node 5 (index 4)
    [inf, inf, inf, 10, 6, 0, 9],    # Node 6 (index 5)
    [12, inf, 9, inf, 7, 9, 0]       # Node 7 (index 6)
]

def convert_to_coordinates(adj_matrix):
    n = len(adj_matrix)
    coords = []
    for i in range(n):
        angle = 2 * pi * i / n
        coords.append([cos(angle), sin(angle)])
    
    for _ in range(100):
        for i in range(n):
            for j in range(i + 1, n):
                if adj_matrix[i][j] == inf:
                    target_dist = 2.0
                else:
                    target_dist = adj_matrix[i][j] / 12.0
                
                dx = coords[j][0] - coords[i][0]
                dy = coords[j][1] - coords[i][1]
                current_dist = sqrt(dx * dx + dy * dy)
                
                if current_dist > 0:
                    force = (target_dist - current_dist) / current_dist
                    factor = 0.1 * force
                    coords[i][0] -= dx * factor
                    coords[i][1] -= dy * factor
                    coords[j][0] += dx * factor
                    coords[j][1] += dy * factor
    
    return coords

class SOM_TSP:
    def __init__(self, city_coordinates, n_neurons=None, learning_rate=0.8):
        self.city_coordinates = city_coordinates
        self.n_cities = len(city_coordinates)
        
        if n_neurons is None:
            self.n_neurons = int(2.5 * self.n_cities)
        else:
            self.n_neurons = n_neurons
        
        self.neuron_coordinates = []
        center_x = sum(city[0] for city in city_coordinates) / self.n_cities
        center_y = sum(city[1] for city in city_coordinates) / self.n_cities
        max_x = max(city[0] for city in city_coordinates)
        min_x = min(city[0] for city in city_coordinates)
        max_y = max(city[1] for city in city_coordinates)
        min_y = min(city[1] for city in city_coordinates)
        r = 0.5 * ((max_x - min_x) + (max_y - min_y)) / 4
        
        for i in range(self.n_neurons):
            angle = 2 * pi * i / self.n_neurons
            x = center_x + r * cos(angle)
            y = center_y + r * sin(angle)
            self.neuron_coordinates.append([x, y])
        
        self.learning_rate = learning_rate
        self.n_iterations = 100 * self.n_cities
        
    def get_winner(self, city_idx):
        city = self.city_coordinates[city_idx]
        min_dist = float('inf')
        winner = 0
        for i, neuron in enumerate(self.neuron_coordinates):
            dist = (neuron[0] - city[0])**2 + (neuron[1] - city[1])**2
            if dist < min_dist:
                min_dist = dist
                winner = i
        return winner
        
    def get_neighborhood(self, winner, iteration):
        radius = self.n_neurons / 2 * (1 - iteration / self.n_iterations)
        if radius < 1:
            radius = 1
        neighborhood = []
        for i in range(self.n_neurons):
            dist = min(abs(i - winner), self.n_neurons - abs(i - winner))
            influence = exp(-(dist**2) / (2 * (radius**2)))
            neighborhood.append(influence)
        return neighborhood
        
    def train(self):
        for iteration in range(self.n_iterations):
            current_lr = self.learning_rate * (1 - iteration / self.n_iterations)
            city_idx = random.randint(0, self.n_cities - 1)
            winner = self.get_winner(city_idx)
            neighborhood = self.get_neighborhood(winner, iteration)
            for i in range(self.n_neurons):
                influence = neighborhood[i] * current_lr
                dx = self.city_coordinates[city_idx][0] - self.neuron_coordinates[i][0]
                dy = self.city_coordinates[city_idx][1] - self.neuron_coordinates[i][1]
                self.neuron_coordinates[i][0] += influence * dx
                self.neuron_coordinates[i][1] += influence * dy
                
    def get_route(self):
        route = []
        for city_idx in range(self.n_cities):
            winner = self.get_winner(city_idx)
            route.append((city_idx, winner))
        route.sort(key=lambda x: x[1])
        city_route = [x[0] for x in route]
        if 0 in city_route:
            start_idx = city_route.index(0)
            city_route = city_route[start_idx:] + city_route[:start_idx]
        else:
            city_route = [0] + city_route
        city_route.append(0)
        return city_route
        
    def calculate_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            from_city = route[i]
            to_city = route[i + 1]
            if adjacency_matrix[from_city][to_city] == inf:
                return inf
            distance += adjacency_matrix[from_city][to_city]
        return distance

city_coordinates = convert_to_coordinates(adjacency_matrix)
som = SOM_TSP(city_coordinates)
som.train()
route = som.get_route()
route_distance = som.calculate_distance(route)

print(f"SOM Route: {[city + 1 for city in route]}")
print("Path:", " > ".join(str(city + 1) for city in route))
print(f"SOM Route Distance: {route_distance}")

import matplotlib.pyplot as plt

def plot_som_graph(city_coords, neuron_coords, route):
    plt.figure(figsize=(10, 8))

    # Plot cities
    city_x = [city[0] for city in city_coords]
    city_y = [city[1] for city in city_coords]
    plt.scatter(city_x, city_y, color='blue', label='Cities', s=100)
    for i, (x, y) in enumerate(city_coords):
        plt.text(x, y, f'City {i+1}', fontsize=12, color='blue', ha='center')

    # Plot neurons
    neuron_x = [neuron[0] for neuron in neuron_coords]
    neuron_y = [neuron[1] for neuron in neuron_coords]
    plt.plot(neuron_x, neuron_y, color='orange', linestyle='-', marker='o', label='Neuron Route', markersize=5)

    # Plot the route
    route_x = [city_coords[city][0] for city in route]
    route_y = [city_coords[city][1] for city in route]
    plt.plot(route_x, route_y, color='green', linestyle='--', linewidth=2, label='Final Route')
    
    # Start and end point of the route
    plt.scatter(route_x[0], route_y[0], color='red', label='Start/End', s=150)

    plt.title('SOM TSP Visualization', fontsize=16)
    plt.xlabel('X Coordinate', fontsize=14)
    plt.ylabel('Y Coordinate', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the plotting function
plot_som_graph(city_coordinates, som.neuron_coordinates, route)

