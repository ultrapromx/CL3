import random
import numpy as np
from deap import base, creator, tools, algorithms

# Define the fitness criteria and individual structure
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # Maximize the fitness
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)  # Attribute generator (binary)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)  # Individual generator
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # Population generator

# Define the genetic operators
def evalOneMax(individual):
    """Objective function, to maximize the sum of individuals."""
    return (sum(individual),)  # Tuple return

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)  # Crossover operator
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)  # Mutation operator
toolbox.register("select", tools.selTournament, tournsize=3)  # Selection operator

# Genetic Algorithm flow
def main():
    random.seed(42)
    pop = toolbox.population(n=300)  # Create a population of 300 individuals
    hof = tools.HallOfFame(1)  # Hall of fame to store the best individual
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", min)
    stats.register("max", max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

# Running the GA
if __name__ == "__main__":
    pop, log, hof = main()
    print("Best individual is: %s\nWith fitness: %s" % (hof[0], hof[0].fitness))

