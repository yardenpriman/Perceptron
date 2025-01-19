#! python3

import numpy as np 
import matplotlib.pyplot as plt 
import time

def perceptron(x, w):
  O = np.dot(x, w)
  if O > 0:
    return (True, w)
  else:
    return (False, np.add(w, x))

def perceptron_convergence_probability(N, alpha):
  p = int(alpha * N)
  total_converged = 0

  for sys in range(100):
    w = -1 + (np.random.rand(N) * 2)
    x = -1 + (np.random.rand(p, N) * 2)
    num_converged = 0
    i = 0
    while num_converged < p and i < 10*N:
      num_converged = 0
      for cur_x in x:
        out, new_w = perceptron(cur_x, w)
        if out:
          num_converged += 1
        else:
          w = new_w
      i += 1
    
    if num_converged == p:
      total_converged += 1
    
  return total_converged / 100


for N in [100, 500, 1000]:
  t = time.time()
  values = []
  for alpha in [0.5*x for x in range(1, 6)]:
    values.append(perceptron_convergence_probability(N, alpha))
  print(N, values)
  print(time.time() - t)