import numpy as np
import matplotlib.pyplot as plt 



def objective_function (x_1,x_2):
    result = (x_1 ** 2 + x_2 - 11) ** 2 + (x_1 + x_2 ** 2 - 7) ** 2 
    return result 

x_1 = np.linspace(-5,5,200)
x_2 = np.linspace(-5,5,200)

x_1_grid, x_2_grid = np.meshgrid(x_1, x_2)


resulting_grid = objective_function(x_1_grid,x_2_grid)

new_grid = np.log(0.01 + resulting_grid)

minima = np.array([
    [-2.80511809,  3.13131252],
    [ 3.00000000,  2.00000000],
    [-3.77931025, -3.28318599],
    [ 3.58442834, -1.84812653]
])

plt.contour(x_1_grid, x_2_grid, new_grid, levels=30)
plt.scatter(minima[:, 0], minima[:, 1], color="red", marker="x", s=80, zorder=5)
plt.show()

def run_pso ():
    inertia_weight = 1.4
    inertia_decay = 0.99
    minimum_inertia_weight = 0.4

    number_of_particles = 30
    position = np.random.uniform(-5,5, size=(number_of_particles,2))
    velocity = np.zeros(shape=(number_of_particles,2))

    value = objective_function(position[:,0], position[:, 1])

    personal_best_position = position.copy()
    personal_best_value = value.copy()

    best_index = np.argmin(personal_best_value)

    global_best_position = personal_best_position[best_index].copy()
    global_best_value = personal_best_value[best_index]

    number_of_iterations = 200

    time_step = 1.0
    c1 = 2.0
    c2 = 2.0

    for i in range (number_of_iterations):
        q = np.random.uniform(0,1, size=(number_of_particles,2))
        r = np.random.uniform(0,1, size=(number_of_particles,2))

        personal_pull = ((personal_best_position - position) / time_step) * c1 * q
        swarm_pull = ((global_best_position - position) / time_step) * c2 * r

        velocity = (inertia_weight * velocity) + personal_pull + swarm_pull
        position = position + velocity * time_step

        value = objective_function(position[:,0], position[:, 1])

        improved = value < personal_best_value

        personal_best_position[improved] = position[improved] 
        personal_best_value[improved]= value[improved] 

        best_index = np.argmin(personal_best_value)
        if personal_best_value[best_index] < global_best_value:
            global_best_value = personal_best_value[best_index].copy()
            global_best_position = personal_best_position[best_index].copy()


        inertia_weight = max(minimum_inertia_weight, inertia_weight * inertia_decay)

    return global_best_position, global_best_value


for j in range (20):
    best_position, best_value = run_pso()
    print("Best position:", best_position)
    print("Function value:", best_value)
