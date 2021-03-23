# Genetic TSP Python
*My Python implementation of a genetic algorithm for solving the traveling salesman problem in Python.*



## How to run

Make sure you have a Python 3.6+ interpreter as well as the [matplotlib](https://matplotlib.org/) module installed, then simply run *main.py* !



## Understanding the code

The could should be self-explanatory with all the comments I wrote in the different files, however if you still don't get how it works, go check the external resources I linked below :wink:

If you just want to train yourself on the core principles of a genetic algorithm, feel free to download the code in the `gap-fill` branch of this repository and try to fill in the gaps I left in the following methods:

- `mutate` (in `individual.py`)
- `crossover` (in `functions.py`)
- `elitistSelection` (in `functions.py`)
- `selectMatingPool` (in `functions.py`)



## Improving the code

This code is far from perfect, so don't hesitate to tweak it to your liking, be it to optimize things, or to try new methods!
For example, you might want to change the value of parameters in `parameters.py`, or to re-write the body of the methods used in the algorithm to test alternatives to the one I propose here (like changing the breeding, mutating or selection methods).

Any feedback, so long as it is constructive, would be greatly appreciated :blush:



## External resources about this implementation

- [The slideshow I created](https://docs.google.com/presentation/d/1GV9fL76_BTHYUN9knwAncWSClhy0scuMF2aENe9Q9Bo/edit?usp=sharing) to explain my algorithm during my lecture at INSAlgo
- [Eric Stoltz's tutorial](https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35) that greatly inspired me