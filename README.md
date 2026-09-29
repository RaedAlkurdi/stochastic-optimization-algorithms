# Stochastic Optimization Algorithms (FFR105)

This repository contains coursework from **Stochastic Optimization Algorithms**. The assignments explore how search algorithms find good solutions when checking every possibility is impractical.

## Homework 1: Function optimization

`Home_work_1/genetic_algorithm.py` implements a genetic algorithm for a function of two variables. It uses binary chromosomes, tournament selection, crossover, mutation, and elitism.

- `run_single.py` runs the genetic algorithm once.
- `run_batch.py` compares several mutation probabilities over repeated runs and prints the median fitness.
- `run_penalty_method.py` uses gradient descent with a penalty term to handle a circular constraint.

Run these from the repository's main folder:

```powershell
py Home_work_1/run_single.py
py Home_work_1/run_batch.py
py Home_work_1/run_penalty_method.py
```

The batch experiment performs many optimization runs and may take a while.

## Homework 2: Ant System for the travelling salesman problem

`Home_work_2/run_ant_system.py` uses an Ant System to search for a short route through the locations in `city_data.py`. Ants choose their next city using pheromone levels and distance. After each iteration, the program updates the pheromone levels and plots improvements to the best route.

Install Matplotlib and run the script:

```powershell
py -m pip install matplotlib
py Home_work_2/run_ant_system.py
```

The script writes its current best route to `Home_work_2/best_result_found.py`. [Figure_1.png](Figure_1.png) shows an example route.

## Notes on the results

These algorithms use randomness, so results can differ between runs. The Ant System script stops only when it finds a route below its target length; it has no maximum-iteration limit, so a run may take a long time. The example route is a result found by the algorithm, not proof of the shortest possible route.

Some files retain assignment scaffolding and data supplied for the course. The code and experiments in each homework show the work I completed for that assignment.
