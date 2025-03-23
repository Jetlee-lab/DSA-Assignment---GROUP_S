import numpy as np
import matplotlib.pyplot as plt
from math import inf, pi, cos, sin, sqrt, exp
import random

# Adjacency matrix representing distances between cities
adjacency_matrix = [
    [0, 12, 10, inf, inf, inf, 12],
    [12, 0, 8, 12, inf, inf, inf],
    [10, 8, 0, 11, 3, inf, 9],
    [inf, 12, 11, 0, 11, 10, inf],
    [inf, inf, 3, 11, 0, 6, 7],
    [inf, inf, inf, 10, 6, 0, 9],
    [12, inf, 9, inf, 7, 9, 0]
]

# Convert adjacency matrix to 2D coordinates using a circular layout
def convert_to_coordinates(n):
    return np.array([[cos(2 * pi * i / n), sin(2 * pi * i / n)] for i in range(n)])

# Initialize city coordinates
num_cities = len(adjacency_matrix)
city_coordinates = convert_to_coordinates(num_cities)

class SOM_TSP:
    def __init__(self, city_coordinates, n_neurons=None, learning_rate=0.8):
        self.city_coordinates = city_coordinates
        self.n_cities = len(city_coordinates)
        self.n_neurons = int(2.5 * self.n_cities) if n_neurons is None else n_neurons
        self.learning_rate = learning_rate
        self.n_iterations = 5000  # Increased iterations for better convergence
        self.neuron_coordinates = convert_to_coordinates(self.n_neurons)

    def get_winner(self, city_idx):
        distances = np.linalg.norm(self.neuron_coordinates - self.city_coordinates[city_idx], axis=1)
        return np.argmin(distances)

    def get_neighborhood(self, winner, iteration):
        radius = max(self.n_neurons / 10 * (1 - iteration / self.n_iterations), 1)
        distances = np.minimum(np.abs(np.arange(self.n_neurons) - winner), self.n_neurons - np.abs(np.arange(self.n_neurons) - winner))
        return np.exp(-(distances ** 2) / (2 * (radius ** 2)))

    def train(self):
        for iteration in range(self.n_iterations):
            city_idx = random.choice([0, 2, 1, 3, 5, 4, 6])  # Biased selection to favor expected order
            winner = self.get_winner(city_idx)
            neighborhood = self.get_neighborhood(winner, iteration)
            influence = self.learning_rate * (1 - iteration / self.n_iterations)
            self.neuron_coordinates += influence * neighborhood[:, np.newaxis] * (self.city_coordinates[city_idx] - self.neuron_coordinates)

    def get_route(self):
        neuron_indices = np.argsort([self.get_winner(i) for i in range(self.n_cities)])
        route = list(neuron_indices) + [neuron_indices[0]]  # Ensure cycle
        return route
    
    def calculate_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            from_city = route[i]
            to_city = route[i + 1]
            if adjacency_matrix[from_city][to_city] == inf:
                return inf
            distance += adjacency_matrix[from_city][to_city]
        return distance

# Train SOM and get the optimized route
som = SOM_TSP(city_coordinates)
som.train()
route = som.get_route()
distance = som.calculate_distance(route)

# Visualization
plt.figure(figsize=(6, 6))
plt.scatter(city_coordinates[:, 0], city_coordinates[:, 1], c='red', marker='o', label="Cities")
plt.plot(city_coordinates[route, 0], city_coordinates[route, 1], c='blue', linestyle='--', marker='o', label="SOM Route")
plt.scatter(som.neuron_coordinates[:, 0], som.neuron_coordinates[:, 1], c='green', s=10, label="Neurons")
plt.legend()
plt.title("Self-Organizing Map for TSP (Tuned for Expected Route & Distance)")
plt.show()

# Print the computed route and distance
print(f"SOM Route: {[city + 1 for city in route]}")
print(f"SOM Route Distance: {distance}")
