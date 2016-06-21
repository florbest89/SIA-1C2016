from selection import *
from cross import *
from mutation import *
from random import sample
from math import floor

def replacement_method_1(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4,
                         m, SP, T, P, cross_method, pc, mutation_method, pm):
    # new_generation = []
    generation = []

    if selection_method == 'elite':
        # selected = select(len(population),m,T,P,SP,population,selection_method)
        # new_generation = transform(selected,cross_method,pc,mutation_method,pm)
        selected = select_mix(A, len(population), population,m,T,P,SP,selection_method1,selection_method2)
        generation = transform(selected, cross_method, pc, mutation_method, pm)
        new_generation = select_mix(B, len(generation), generation, m, T, P, SP, selection_method3, selection_method4)
    else:
        while len(new_generation) < len(population):
            # selected = select(2,m,T,P,SP,population,selection_method)
            selected = select_mix(A, population, m, T, P, SP, selection_method1, selection_method2)

            p1 = selected[0]
            p2 = selected[1]

            c1, c2 = cross(pc,p1,p2,cross_method)
            c1, c2 = mutation(c1,c2,pm,mutation_method)

            # new_generation.append(c1)
            # new_generation.append(c2)
            generation.append(c1)
            generation.append(c2)

        new_generation = select_mix(B, len(generation), generation, m, T, P, SP, selection_method3, selection_method4)

    return new_generation

def replacement_method_2(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    # selected = select(k,m,T,P,SP,population,selection_method)
    selected = select_mix(A, len(population), population,m,T,P,SP,selection_method1,selection_method2)
    children = transform(selected,cross_method,pc,mutation_method,pm)

    # Se crea la nueva generacion
    new_generation = []
    index_individual_for_next_generation = sample(range(0, len(population)), len(population) - k)

    for i in index_individual_for_next_generation:
        new_generation.append(population[i].copy())

    for i in range(0, len(children)):
        new_generation.append(children[i].copy())

    # Se devuelve la nuega generacion
    return select_mix(B, len(population), new_generation,m,T,P,SP,selection_method3,selection_method4)

def replacement_method_3(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, selection_for_replacement, k, m, SP, T, P, cross_method, pc, mutation_method, pm):

    new_generation = copy_population(population)

    # N = len(population)

    # selected = select(k,m,T,P,SP,population,selection_method)
    selected = select_mix(A, len(population), population,m,T,P,SP,selection_method1,selection_method2)

    transformed = transform(selected,cross_method,pc,mutation_method,pm)

    # return select(N, m, T, P, SP, new_generation + transformed, selection_for_replacement)
    return select_mix(B, len(population), new_generation + transformed,m,T,P,SP,selection_method3,selection_method4)

def replacement_mix(population, selection_method,selection_for_replacement_a, selection_for_replacement_b, a, G, m, SP, T, P, cross_method, pc, mutation_method, pm):

    selected_old = []
    selected_a = []
    selected_b = []

    N = len(population)

    k_old = floor(N * (1 - G))

    k_a = floor((G / a) * N)

    #To assure that the population keeps being of size N
    k_b = N - k_old - k_a

    selected_old = select(k_old,m,T,P,SP,population,selection_method)
    selected_a = select(k_a,m,T,P,SP,population,selection_for_replacement_a)
    selected_b = select(k_b,m,T,P,SP,population,selection_for_replacement_b)

    transformed_a = transform(selected_a,cross_method,pc,mutation_method,pm)
    transformed_b = transform(selected_b, cross_method, pc, mutation_method, pm)

    return selected_old + transformed_a + transformed_b

def transform(selected_population,cross_method, pc, mutation_method, pm):

    transformed = []

    while len(selected_population) > 0:

        if len(selected_population) >= 2:
            p1 = selected_population[0]
            p2 = selected_population[1]

            c1, c2 = cross(pc, p1, p2, cross_method)
            c1, c2 = mutation(c1, c2, pm, mutation_method)

            transformed.append(c1)
            transformed.append(c2)

            selected_population.pop(1)
            selected_population.pop(0)
        else:
            p1 = selected_population[0]

            c1,c2 = mutation(p1.copy(),None,pm,mutation_method)
            transformed.append(c1)

            selected_population.pop(0)

    return transformed

# G entre [0, 1]. Me indica cuantos padres de la generacion t pasan a t + 1
# Se pasa un selection_method0 para la seleccion de individuos que pasan de la generacion
# t a t+1 sin sufrir cambios
def generation_gap(G, population, selection_method, m, SP, T, P, cross_method, pc, mutation_method, pm):

    population_to_be_evaluated = []

    if G == 1:
        next_generation = population
    elif G == 0:
        # ninguno individuo de la genenracion t pasa a la proxima generacion
        next_generation = []
    elif 0 < G and G < 1:
        number_of_people = int((1 - G) * len(population))
        next_generation = select(number_of_people, m, T, P, SP, population, selection_method)

    for i in range(0, len(population)):
        if population[i] in next_generation:
            population_to_be_evaluated.append(population[i])

    children = transform(selected,cross_method,pc,mutation_method,pm)

    for i in range(0, len(children)):
        next_generation.append(children[i])

    return next_generation

def copy_population(population):
    pop_copy = []

    N = len(population)

    for p in range(0,N):
        pop_copy.append(population[p].copy())

    return pop_copy

def replace(population, A, B, replacement_method, selection_method1, selection_method2, selection_method3, selection_method4,selection_for_replacement_a, selection_for_replacement_b, a, G, m, SP, T, P, cross_method, pc, mutation_method, pm):

    k = floor(G * len(population))

    if replacement_method == 'replacement_one':
        return replacement_method_1(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4,
                         m, SP, T, P, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_two':
        return replacement_method_2(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, P, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_three':
        return replacement_method_3(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, selection_for_replacement, k, m, SP, T, P, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_mixed':
        return replacement_mix(population, selection_method, selection_for_replacement_a, selection_for_replacement_b, a, G, m, SP, T, P, cross_method, pc, mutation_method, pm)