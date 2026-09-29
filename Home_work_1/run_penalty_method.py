import math
# ==============================
# run_gradient_descent function:
# ==============================

def run_gradient_descent(x_start, mu, eta, gradient_tolerance):
  current_point = [x_start[0],x_start[1]]

  while True:
    gradient = compute_gradient(current_point,mu)
    norm_check = math.sqrt(gradient[0] ** 2 + gradient[1] ** 2)

    if norm_check < gradient_tolerance:
      return current_point
    
    else: 
      next_x1 = current_point[0] - eta * gradient[0]
      next_x2 = current_point[1] - eta * gradient[1]
      current_point = [next_x1,next_x2]



# ==============================
# compute_gradient function:
# ==============================

def compute_gradient(x, mu):
  x1 , x2 = x[0], x[1]
  constraint_value = x1 ** 2 + x2 ** 2 - 1

  if constraint_value <= 0:
    partial_derivative_1 = 2 * (x1-1)
    partial_derivative_2 = 4 * (x2-2)
    gradient = [partial_derivative_1, partial_derivative_2]

  else:
    partial_derivative_1 = 2 * (x1-1) + 4 * mu * x1 * (x1 ** 2 + x2 ** 2 - 1)
    partial_derivative_2 = 4 * (x2-2) + 4 * mu * x2 * (x1 ** 2 + x2 ** 2 - 1)
    gradient = [partial_derivative_1, partial_derivative_2]
  
  return gradient
     

# ==============================
# Main program:
# ==============================

mu_values = [1, 10, 100, 1000]
eta = 0.0001
x_start = [1,2]
gradient_tolerance = 0.0000001

for mu in mu_values:
  x = run_gradient_descent(x_start, mu, eta, gradient_tolerance)
  output = f"x = ({x[0]:.4f}, {x[1]:.4f}), mu = {mu:.1f}"
  print(output)


