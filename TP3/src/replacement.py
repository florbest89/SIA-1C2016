from selection import selection
from cross import *
from mutation import *
from random import sample

# TODO: REPLACEMENT METHODS

# REPLACEMENT METHODS 2
# k padres
def replacement_method_2(population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    print ("valor de k: " + str(k))

    # Se realiza la seleccion
    selected_result = selection(population, selection_method, k, m, SP, T, P)

    print ("tamano de selected: " + str(len(selected_result)))

    cross_result = []

    # Se realiza el cross
    for i in range(0, int(len(selected_result)/2)):
        s1, s2 = cross(pc, selected_result[i], selected_result[len(selected_result) - 1 - i], cross_method)
        cross_result.append(s1)
        cross_result.append(s2)

    print ("tamano de cross: " + str(len(cross_result)))

    # Se realiza la mutacion
    children_result = []
    children = 0
    while children != k:
        idx = sample(range(0, len(selected_result)), 2)
        children_result.append(mutation(selected_result[idx[0]], selected_result[idx[1]], pm, mutation_method))
        children += 1

    # Se crea la nueva generacion
    new_generation = []
    index_individual_for_next_generation = sample(range(0, len(population)), len(population) - k)

    for i in index_individual_for_next_generation:
        new_generation.append(population[i])

    for i in range(0, len(cross_result)):
        new_generation.append(cross_result[i])

    # Se devuelve la nuega generacion
    return new_generation
