from models import *
from random import uniform
from cross import *
from mutation import *
from selection import *
from replacement import *

def genetic_algorithm():
    parameters, multipliers, methods, stop_criteria, stop_value = parse_config()

    population = create_population(parameters[0],multipliers)

    if stop_criteria == 'generations':
        result = genetic_algorithm_generations(parameters,multipliers,methods,population,stop_value)

def genetic_algorithm_generations(parameters,multipliers,methods,population,generations):
    # 0 - N , 1 - pm, 2 - pc, 3 - G
    # 0 - selection, 1 - cross, 2 - mutation, 3 - replacement

    generation = population

    # while generations > 0:

    for i in range(100000):
        # selected = select(2,0,0,0,0,generation,methods[0])
        generation = replacement_method_2(generation,'universal', 4, 0, 0, 0, 0, 'cross_1P', 0.5, 'not_uniform', 0.5)
        print("ITERACION " + str(i))

    for i in range(0, len(generation)):
        print('nro: '+ str(i) + ' fitness: ' + str(population[i].fitness))


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

genetic_algorithm()
