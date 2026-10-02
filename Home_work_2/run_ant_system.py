###########################
#
# Ant System (AS) for TSP
#
###########################

import math
# import numpy as np
import matplotlib.pyplot as plt
import random
from pathlib import Path


###############################################################
## To do: Write the initialize_pheromone_levels function:
###############################################################
def initialize_pheromone_levels(number_of_cities, tau_0):
  entry = []
  for i in range(number_of_cities):
      entry.append([tau_0] * number_of_cities)
  return entry 
  
###############################################################
## To do: Write the get_visibility function:
###############################################################

def get_visibility(city_locations):
    visibility = []

    for i in range (len(city_locations)):
        row = []
        for j in range (len(city_locations)):
            if i == j:
                row.append(0)
            else: 
                distance = math.dist(city_locations[i], city_locations[j])
                row.append( 1 / distance)
        visibility.append(row)
    return visibility





#################################################################
## To do: Write the generate_path function (Note: You may wish
##       to add more functions, e.g., get_node. That is allowed).
#################################################################

def generate_path(pheromone_levels, visibility, alpha, beta):
    cities = len(visibility)
    starting_city = random.randrange(cities)
    path = [starting_city]

    while len(path) < cities: 
        available = []
        weights = []

        for i in range (cities):
            if i not in path:
                available.append(i)

        current_city = path[-1]
        for j in (available):
            weight = pheromone_levels[current_city][j]  ** alpha * visibility[current_city][j] ** beta
            weights.append(weight)

        chosen_city = random.choices(available, weights=weights, k = 1)[0]
        path.append(chosen_city)
    return path



###############################################################
## To do: Write the get_path_length function:
###############################################################

def get_path_length(path, city_locations):
    running_total = 0
    for i in range(len(path)):
        current_city = path[i]
        next_city = path[(i + 1) % len(path)]
        point_a = city_locations[current_city]
        point_b = city_locations[next_city]
        distance = math.dist(point_a,point_b)
        running_total += distance
    return running_total
###############################################################
## To do: Write the compute_delta_pheromone_levels function:
###############################################################

def compute_delta_pheromone_levels(path_collection, path_length_collection):
    city_numbers = len(path_collection[0])
    matrix = [[0 for _ in range(city_numbers)] for _ in range(city_numbers)]

    for path, path_length in zip(path_collection, path_length_collection):
        contribution = 1 / path_length
        for i in range (len(path)):
            starting_city = path[i]
            destination = path[(i + 1) % len(path)]
            matrix[starting_city][destination] += contribution
    return matrix

###############################################################
## To do: Write the update_pheromone_levels function:
###############################################################

def update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho):
    result = []
    for i in range (len(pheromone_levels)):
        row = []

        for j in range (len(pheromone_levels)):
            new = (1 - rho) * pheromone_levels[i][j] + delta_pheromone_levels[i][j] 
            row.append(new)
        result.append(row)
    return result

##################################################
#  Plots the cities (nodes):
##################################################

# Add plot code here (can be more than one function)

#####################################
# Main program:
#####################################

###########################
# Data:
###########################
from city_data import city_locations
number_of_cities = len(city_locations)

###########################
# Parameters:
###########################
number_of_ants = 50 ## Changes allowed.
alpha = 1.0         ## Changes allowed.
beta = 5.0          ## Changes allowed.
rho = 0.5           ## Changes allowed.
tau_0 = 0.1         ## Changes allowed.

target_path_length = 99.9999999

#################################
# Initialization:
#################################

## To do: Add plot initialization here


pheromone_levels = initialize_pheromone_levels(number_of_cities, tau_0)
visibility = get_visibility(city_locations)

#################################
# Main loop:
#################################

iteration_index = 0
minimum_path_length = math.inf
best_path = None

path_length = math.inf

plt.ion()
fig, ax = plt.subplots()
while (minimum_path_length > target_path_length):
  iteration_index += 1
  path_collection = []
  path_length_collection = []
  for ant_index in range(number_of_ants):  
    # Generate paths:
    path = generate_path(pheromone_levels, visibility, alpha, beta) # Uncomment after writing the function
    path_length = get_path_length(path, city_locations) # Uncomment after writing the function
    if (path_length < minimum_path_length):
      minimum_path_length = path_length
      best_path = path.copy()
      with open(Path(__file__).with_name("best_result_found.py"), "w", encoding="utf-8") as result_file:
          result_file.write(f"best_path = {best_path}\n")
      print(minimum_path_length)

      plot_path = best_path + [best_path[0]]
      x_values , y_values = [], []
      for city_index in plot_path:
        x_values.append(city_locations[city_index][0]) 
        y_values.append(city_locations[city_index][1])
      ax.clear()
      ax.plot(x_values,y_values)
      fig.canvas.draw()
      plt.pause(0.01)
      
      # To do: Add code for plotting here

    path_collection.append(path)
    path_length_collection.append(path_length)
  # Update pheromone levels:
  delta_pheromone_levels = compute_delta_pheromone_levels(path_collection,path_length_collection) # Uncomment after writing the function
  pheromone_levels = update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho) # Uncomment after writing the function

input(f'Press return to exit')