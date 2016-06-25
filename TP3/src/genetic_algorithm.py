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
    epsilon = 0.001

    temperature_reduction = 0.05

    new_generation = create_population(parameters[0],multipliers)

    # If 'structure' is stop condition
    previous_new_generation = copy_population(new_generation)
    similar_generation_counter = 0

    # Parameters
    # 0 - N , 1 - pm, 2 - pc, 3 - G, 4 - T, 5 - SP, 6 - m, 7 - a, 8 - A, 9 - B
    N = parameters[0]
    pm = parameters[1]
    pc = parameters[2]
    G = parameters[3]
    T = parameters[4]
    SP = parameters[5]
    m = parameters[6]
    a = parameters[7]
    A = parameters[8]
    B = parameters[9]
    k = parameters[10]

    # Methods
    # 0 - selection_a, 1 - selection_b, 2 - cross, 3 - mutation, 4 - replacement, 5 - rep_selection_a, 6 - rep_selection_b
    selection_method_a = methods[0]
    selection_method_b = methods[1]
    cross_method = methods[2]
    mutation_method = methods[3]
    replacement_method = methods[4]
    replace_sel_a = methods[5]
    replace_sel_b = methods[6]

    print('Metodos de seleccion: ' + selection_method_a + ' + ' + selection_method_b)
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

        print('TEMPERATURA :' + str(T))
        new_generation = replace(new_generation, A, B, replacement_method, selection_method_a, selection_method_b, replace_sel_a,
                    replace_sel_b,a, G, m, SP, T,cross_method, pc, mutation_method, pm,k)

        print('GENERACION : ' + str(len(best_fitness)))

        if T > 1 :
            T = T * (1 - temperature_reduction)
        else:
            T = 1

        best_defender = max(new_generation, key=attrgetter('fitness'))
        fitness_avg = sum(x.fitness for x in new_generation) / N
        best_fitness.append(best_defender.fitness)
        fit_avg.append(fitness_avg)

        print('Best fitness of all: ' + str(best))

        if abs(best - best_defender.fitness) < epsilon:
            same += 1
        else:
            same = 0
            best = best_defender.fitness

        print('same ' + str(same))

        if stop_criteria == 'generations':
            continue_algorithm = len(best_fitness) - 1 < stop_value
        elif stop_criteria == 'optimum':
            continue_algorithm = best_defender.fitness < stop_value
        elif stop_criteria == 'content':
            continue_algorithm = same < stop_value
        elif stop_criteria == 'structure':
            percentage_stop_condition = stop_value
            similar_generation = 20

            current_new_generation = new_generation
            number_of_people = len(current_new_generation)
            same_defender = 0

            for i in range(0, number_of_people):
                if previous_new_generation[i] == current_new_generation[i]:
                    same_defender += 1

            percentage_similar = same_defender / number_of_people

            if percentage_stop_condition > percentage_similar:
                similar_generation_counter = 0
            else:
                similar_generation_counter += 1

            previous_new_generation = copy_population(current_new_generation)

            continue_algorithm = not (similar_generation == similar_generation_counter)


    print('CANTIDAD DE GENERACIONES : ' + str(len(new_generation)))
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
