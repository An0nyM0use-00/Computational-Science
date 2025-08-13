import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]


alpha = 0.1  # Prey growth rate
beta = 0.02  # Predation rate
delta = 0.01 # Predator growth rate
gamma = 0.1  # Predator death rate

# Initial conditions: 40 prey and 9 predators
z0 = [40, 9]

t = np.linspace(0, 200, 1000)

# Solve ODE
solution = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))
x, y = solution.T

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, x, label='Prey (Rabbits)', color='blue')
plt.plot(t, y, label='Predators (Foxes)', color='red')
plt.title('Predator-Prey Model (Lotka-Volterra)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid()
plt.show()
