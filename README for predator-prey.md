# Predator-Prey Model (Lotka-Volterra Simulation)

A Python simulation of the Lotka-Volterra equations modeling the interaction between prey (e.g., rabbits) and predators (e.g., foxes).

## How It Works

1. Defines a set of differential equations representing prey-predator dynamics.
2. Uses `odeint` from SciPy to numerically solve the equations over time.
3. Plots the populations of prey and predators over a specified time period.

## How To Use

1. Run the program.
2. The simulation will automatically:
   - Solve the equations for given initial conditions and parameters.
   - Display a plot showing prey and predator populations over time.

### Example Parameters

- **alpha** (Prey growth rate): `0.1`
- **beta** (Predation rate): `0.02`
- **delta** (Predator growth rate): `0.01`
- **gamma** (Predator death rate): `0.1`
- **Initial populations**: 40 prey, 9 predators

### Example Output

A plot with:
- **Blue line**: Prey population over time.
- **Red line**: Predator population over time.
- Time on the X-axis, Population on the Y-axis.
