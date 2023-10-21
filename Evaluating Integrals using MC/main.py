import numpy as np
import matplotlib.pyplot as plt

S = 1000  # number of simulations
I = 1000  # numbre of iterations
A = 0.0  # upper limit
B = 1  # lower limit

def fun(x): # function to be integrated
  return np.exp(-(x**2)/2)

Integrations = []
for i in range(S):
  Sum = 0
  for i in range(I):
    x = np.random.uniform(0,1)
    mod_fun = fun((B-A)*x+A)*(B-A)
    Sum += mod_fun

  Int = Sum/float(I)
  Integrations.append(Int)

sum = 0
for i in Integrations:
    sum += i
sample_expection = sum/float(S)

print("")
print(f'Sample Expection: {sample_expection}')

plt.title("Evaluating Integral")
plt.grid()
plt.hist(Integrations,bins=50, edgecolor='#000000')
plt.show()
