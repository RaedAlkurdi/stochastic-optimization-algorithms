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
