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
    epsilon = 0.0001

    # 0 - N , 1 - pm, 2 - pc, 3 - G, 4 - T, 5 - P, 6 - SP, 7 - m, 8 - a
    # 0 - selection, 1 - cross, 2 - mutation, 3 - replacement, 4 - rep_selection [if replacement == replacement_mixed, there is a 5 - rep_selection_2]

    new_generation = create_population(parameters[0],multipliers)

    # If 'structure' is stop condition
    previous_new_generation = copy_population(new_generation)
    similar_generation_counter = 0

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
    replace_sel_b = methods[5]

    print('Metodo de seleccion: ' + selection_method)
    print('Metodo de cruza: ' + cross_method)
    print('Metodo de mutacion: ' + mutation_method)
    print('Metodo de reemplazo: ' + replacement_method)

    if replacement_method == 'replacement_mixed':
        print('Metodos de seleccion para reemplazo: ' + replace_sel_a + ' + ' + replace_sel_b)
    else:
        print('Metodo de seleccion para reemplazo: ' + replace_sel_a)

    best_fitness = []
    fit_avg = []

    best = 0
    same = 0

    best_defender = max(new_generation, key=attrgetter('fitness'))
    best_fitness.append(best_defender.fitness)

    fitness_avg = sum(individual.fitness for individual in new_generation) / N
    fit_avg.append(fitness_avg)


    while continue_algorithm:
        new_generation = replace(new_generation, replacement_method, selection_method, replace_sel_a, replace_sel_b, a,
                                 G, m, SP, T, P, cross_method, pc, mutation_method, pm)
        best_defender = max(new_generation, key=attrgetter('fitness'))
        fitness_avg = sum(x.fitness for x in new_generation) / N
        best_fitness.append(best_defender.fitness)
        fit_avg.append(fitness_avg)

        if abs(best - best_defender.fitness) < epsilon:
            same += 1
        else:
            same = 0

            if best - best_defender.fitness < 0:
                best = best_defender.fitness

        if stop_criteria == 'generations':
            continue_algorithm = len(best_fitness) - 1 < stop_value
        elif stop_criteria == 'optimum':
            continue_algorithm = best_defender.fitness < stop_value
        elif stop_criteria == 'content':
            continue_algorithm = same < stop_value
        elif stop_criteria == 'structure':
            percentage_stop_condition = 0.10
            similar_generation = 3

            current_new_generation = new_generation
            number_of_people = len(current_new_generation)
            same_defender = 0

            for i in range(0, number_of_people):
                if previous_new_generation[i] == current_new_generation[i]:
                    same_defender += 1

            percentage = same_defender/number_of_people

            if percentage_stop_condition < percentage:
                similar_generation_counter = 0
                # continue_algorithm = False
            else:
                similar_generation_counter += 1
                previous_new_generation = copy_population(new_generation)
                # continue_algorithm = True

            if similar_generation == similar_generation_counter:
                print('HUBIERON ' + str(similar_generation) + ' SIMILARES.')
                continue_algorithm = False
            else:
                continue_algorithm = True

    print('------- MEJOR DEFENSOR -------')
    print(best_defender)

    print('Termino')

    plt.plot(best_fitness)
    plt.xlabel('Generación')
    plt.ylabel('Mejor fitness')

    plt.title('Mejor fitness por generacion')
    plt.show()

    plt.plot(fit_avg)
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
