from models import *
from random import uniform
from cross import *
from mutation import *
from selection import *
from replacement import *
from operator import attrgetter
import matplotlib.pyplot as plt

def genetic_algorithm():
    parameters, multipliers, methods, stop_criteria, stop_value = parse_config()

    continue_algorithm = True

    # 0 - N , 1 - pm, 2 - pc, 3 - G, 4 - T, 5 - P, 6 - SP, 7 - m, 8 - a
    # 0 - selection, 1 - cross, 2 - mutation, 3 - replacement, 4 - rep_selection [if replacement == replacement_mixed, there is a 5 - rep_selection_2]

    new_generation = create_population(parameters[0],multipliers)

    # Parameters
    N = parameters[0]
    pm = parameters[1]
    pc = parameters[2]
    G = parameters[3]
    T = parameters[4]
    P = parameters[5]
    SP = parameters[6]
    m = parameters[7]
    a = parameters[8]

    # Methods
    selection_method = methods[0]
    cross_method = methods[1]
    mutation_method = methods[2]
    replacement_method = methods[3]
    replace_sel_a = methods[4]
    replace_sel_b = None

    print('Metodo de seleccion: ' + selection_method)
    print('Metodo de cruza: ' + cross_method)
    print('Metodo de mutacion: ' + mutation_method)
    print('Metodo de reemplazo: ' + replacement_method)

    if replacement_method == 'replacement_mixed':
        print('Metodos de seleccion para reemplazo: ' + replace_sel_a + ' + ' + replace_sel_b)
    else:
        print('Metodo de seleccion para reemplazo: ' + replace_sel_a)

    if len(methods) == 6:
        replace_sel_b = methods[5]

    best_fitness = []
    fit_avg = []

    best_defender = max(new_generation, key=attrgetter('fitness'))
    best_fitness.append(best_defender.fitness)

    fitness_avg = sum(individual.fitness for individual in new_generation) / N
    fit_avg.append(fitness_avg)


    while continue_algorithm:
        new_generation = replace(new_generation, replacement_method, selection_method, replace_sel_a, replace_sel_b, a,
                                 G, m, SP, T, P, cross_method, pc, mutation_method, pm)
        best_defender = max(new_generation, key=attrgetter('fitness'))
        fitness_avg = sum(individual.fitness for individual in new_generation) / N
        best_fitness.append(best_defender.fitness)
        fit_avg.append(fitness_avg)

        if stop_criteria == 'generations':
            continue_algorithm = len(best_fitness) - 1 < stop_value
        elif stop_criteria == 'optimum':
            continue_algorithm = best_defender.fitness < stop_value

    plt.plot(range(1, len(best_fitness)), best_fitness)
    plt.xlabel('Generación')
    plt.ylabel('Mejor fitness')

    plt.title('Mejor fitness por generacion')
    plt.show()

    plt.plot(range(1, len(fit_avg)), fit_avg)
    plt.xlabel('Generación')
    plt.ylabel('Promedio de fitness')

    plt.title('Promedio de fitness por generacion')
    plt.show()

    return best_fitness, fitness_avg, best_defender


def create_population(N, multipliers):

    helmets = parse_helmets(N)
    chestplates = parse_chestplates(N)
    gauntlets = parse_gauntlets(N)
    weapons = parse_weapons(N)
    boots = parse_boots(N)

    population = []

    for i in range(0,N):
        height = uniform(1.3,2.0)
        population.append(Defender(helmets[i],chestplates[i],gauntlets[i],weapons[i],boots[i],height,multipliers[0],multipliers[3],multipliers[2],multipliers[1],multipliers[4]))

    return population

def copy_population(population):
    pop_copy = []

    N = len(population)

    for p in range(0,N):
        pop_copy.append(population[p].copy())

    return pop_copy
genetic_algorithm()
