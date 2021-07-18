from random import choices, randint, uniform
from math import sqrt
import sys

#SETTINGS
population_size = 10
number_of_generations = 10
mutation_chance = 0.2
crossover_chance = 0.8
roulette_type = "linear"  #options:: linear :: root :: square ::


def adaptation(x):
    return 2 * (x * x + 1)

def get_random_population(quantity):
    for i in range(quantity):
        population.append(randint(min_x, max_x))
    return population

def roulette(roulette_type):
    #print("start roulette")
    total_value = 0
    population_values = []
    if roulette_type == "linear":
        for individual in population:
            population_values.append(adaptation(individual))
        total_value = sum(population_values)
        
    elif roulette_type == "root":
        for individual in population:
            population_values.append(adaptation(individual * individual))
        total_value = sum(population_values)

    elif roulette_type == "square":
        for individual in population:
            population_values.append(adaptation(sqrt(individual)))
        total_value = sum(population_values)
    population_chance = [value / total_value for value in population_values]
    survivors = choices(population, population_chance, k=len(population)//2)
    #print("stop roulette")
    survivors += survivors
    return survivors

def mutation(individual, chance):
    if chance > uniform(0, 1):
        #print(f"mutation: {individual}")
        mutate_bit = randint(0, 6)
        genotype = "{0:b}".format(individual).zfill(7)
        if genotype[mutate_bit] == '1':
            genotype = genotype[:mutate_bit] + '0' + genotype[mutate_bit+1:]
        else:
            genotype = genotype[:mutate_bit] + '1' + genotype[mutate_bit+1:]
        individual = int(genotype, 2)
    #print(individual)
    return individual

def crossover(parents, chance):
    if len(parents) != 2:
        return
    parent1_genotype = "{0:b}".format(parents[0]).zfill(7)
    parent2_genotype = "{0:b}".format(parents[1]).zfill(7)
    if chance > uniform(0, 1):
        genotype_range = randint(1,6)
        #print(f"start crossover: {parents[0]} - {parent1_genotype} :: {parents[1]} - {parent1_genotype}")
        child1_genotype = parent1_genotype[:genotype_range] + parent2_genotype[genotype_range:]
        child2_genotype = parent2_genotype[:genotype_range] + parent1_genotype[genotype_range:]
        #print(f"end crossover: child1: {child1_genotype} :: child2: {child2_genotype}")
        child1 = int(child1_genotype, 2)
        child2 = int(child2_genotype, 2)
        #print(f"               child1: {child1}      :: child2: {child2}")
        return(child1, child2)


min_x = 1
max_x = 127
max_val = adaptation(max_x)

population = []
population = get_random_population(population_size)
generation = 1
print("start simulation")
print(f"generation: {generation} || population size: {len(population)}\nindividuals: {population}")

while generation < number_of_generations:
    print("==============================================================================")
    population = roulette(roulette_type)
    for individual in population:
        mutation(individual, mutation_chance)
    children = []
    for i in range(0, len(population), 2):
        parents = population[i:i+2]
        children_pair = crossover(parents, crossover_chance)
        if children_pair is not None:
            for child in children_pair:
                children.append(child)
    population += children
    generation += 1
    print(f"generation: {generation} || population size: {len(population)}\nindividuals: {population}")

    print("==============================================================================")
    print("end simulation")
    if len(population) < 1:
        print("all dead")
        break
    else:
        best_individual = population[0]
        for individual in population:
            if best_individual <= individual:
                best_individual = individual
        print(f"the best individual: {best_individual} :: score: {adaptation(best_individual)}")