import random
import math

# Initialize population:
# Uncomment the line below and implement the function
def initialize_population(population_size, number_of_genes):
  population = []

  for i in range (population_size):
    chromosome = []

    for j in range (number_of_genes):
      bit = random.randint(0,1)
    
      chromosome.append(bit)
    population.append(chromosome)

  return population

# Decode chromosome:
# Note: the variables should each take values in the range [-a,a], where a = maximum_variable_value
# Uncomment the line below and implement the function
def decode_chromosome(chromosome, number_of_variables, maximum_variable_value):
  decoded_variable_values = []
  chromosome_length = len(chromosome)
  bits_per_variable = int(chromosome_length / number_of_variables)

  for i in range(number_of_variables):
    start = i * bits_per_variable
    end = start + bits_per_variable

    bit_group = chromosome[start:end]

    integer_value = 0

    for bit in bit_group:
      integer_value = integer_value * 2 + bit

    x =  - maximum_variable_value + 2 * maximum_variable_value / (1 - 2 **(- bits_per_variable)) * integer_value / (2 ** bits_per_variable)
    decoded_variable_values.append(x)

  return decoded_variable_values





# Evaluate indviduals:
def evaluate_individual(x):
  x1 , x2 = x[0] , x[1]
  g_value = (
        (1.5 - x1 + x1 * x2) ** 2
        + (2.25 - x1 + x1 * x2 ** 2) ** 2
        + (2.625 - x1 +x1 * x2 ** 3) ** 2
    )

  fitness = 1 / (g_value + 1)

  return fitness


# Select individuals:
# Uncomment the line below and implement the function
def tournament_select(fitness_list, tournament_probability, tournament_size): 

  possible_indices = len(fitness_list)
  candidate_list = []

  for i in range (tournament_size):
    r = random.randint(0,possible_indices-1)
    candidate_list.append(r)


  ranking = sorted(candidate_list, key=lambda x: fitness_list[x], reverse=True)

  for i in range (len(candidate_list)-1):
    if random.random() < tournament_probability:
      return ranking[i]

  return ranking[-1]
    
                  
# Carry out crossover:
# Uncomment the line below and implement the function
def cross(chromosome1, chromosome2):
  length_1 = len(chromosome1)
  length_2 = len(chromosome2)

  if length_1 == length_2: 
    r = random.randint(1,length_2-1)
    child_1 = chromosome1[:r] + chromosome2[r:]
    child_2 = chromosome2[:r] + chromosome1[r:]

    return child_1, child_2


# Mutate individuals:
# Uncomment the line below and implement the function
def mutate(chromosome, mutation_probability):
  number_of_genes = len(chromosome)
  mutated_chromosome = chromosome.copy()
  for gene_index in range(number_of_genes):
      r = random.random()
      if r < mutation_probability:
        mutated_chromosome[gene_index] = 1 - chromosome[gene_index]

  return mutated_chromosome



# Genetic algorithm

def run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value, \
                              tournament_size, tournament_probability, crossover_probability,\
                              mutation_probability, number_of_generations):
 
 # This function should return the maximum fitness and the best individual (i.e., a vector with
 # two elements (x1,x2) containing the values corresponding to the maximum fitness found.
 
 # Note that some parameters have different names compared to the programming introduction

  population = initialize_population(population_size,number_of_genes)

  for generation_index in range(number_of_generations):
    maximum_fitness = 0
    best_chromosome = []
    best_individual = []
    fitness_list = []
    for chromosome in population:
      individual = decode_chromosome(chromosome,number_of_variables,maximum_variable_value)
      fitness = evaluate_individual(individual)
      if (fitness > maximum_fitness):
        maximum_fitness = fitness
        best_chromosome = chromosome.copy()  
        best_individual = individual.copy()
      fitness_list.append(fitness)

    temp_population = []
    for i in range(0,population_size,2):
      index_1 = tournament_select(fitness_list, tournament_probability, tournament_size)
      index_2 = tournament_select(fitness_list, tournament_probability, tournament_size)
      chromosome1 = population[index_1].copy()
      chromosome2 = population[index_2].copy()
      r = random.random()
      if r < crossover_probability:
        [new_chromosome_1, new_chromosome_2] = cross(chromosome1,chromosome2)
        temp_population.append(new_chromosome_1)
        temp_population.append(new_chromosome_2) 
      else:
        temp_population.append(chromosome1)
        temp_population.append(chromosome2)

    for i in range(population_size):
      original_chromosome = temp_population[i]

      mutated_chromosome = mutate(original_chromosome, mutation_probability)
      temp_population[i] = mutated_chromosome

    temp_population[0] = best_chromosome
    population = temp_population.copy()

  return [maximum_fitness, best_individual]
 

