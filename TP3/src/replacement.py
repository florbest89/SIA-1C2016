from selection import *
from cross import *
from mutation import *
from random import sample
from math import floor


def replacement_method_1(population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    new_generation = []

    if selection_method == 'elite':
        selected = select(len(population),m,T,P,SP,population,selection_method)
        new_generation = transform(selected,cross_method,pc,mutation_method,pm)
    else:
        while len(new_generation) < len(population):
            selected = select(2,m,T,P,SP,population,selection_method)

            p1 = selected[0]
            p2 = selected[1]

            c1, c2 = cross(pc,p1,p2,cross_method)
            c1, c2 = mutation(c1,c2,pm,mutation_method)

            new_generation.append(c1)
            new_generation.append(c2)

    return new_generation

def replacement_method_2(population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    print ("valor de k: " + str(k))

    children = do_replacement_method_2(population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm)

    # Se crea la nueva generacion
    new_generation = []
    index_individual_for_next_generation = sample(range(0, len(population)), len(population) - k)

    for i in index_individual_for_next_generation:
        new_generation.append(population[i])

    for i in range(0, len(children)):
        new_generation.append(children[i])

    # Se devuelve la nuega generacion
    return new_generation

def replacement_method_3(population, selection_method, selection_for_replacement, k, m, SP, T, P, cross_method, pc, mutation_method, pm):

    new_generation = copy_population(population)

    N = len(population)

    selected = select(k,m,T,P,SP,population,selection_method)
    transformed = transform(selected,cross_method,pc,mutation_method,pm)

    return select(N, m, T, P, SP, new_generation + transformed, selection_for_replacement)

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

            selected_population.pop(0)
            selected_population.pop(1)
        else:
            p1 = selected_population[0]

            c1,c2 = mutation(p1.copy(),None,pm,mutation_method)
            transformed.append(c1)

            selected_population.pop(0)

    return transformed


# metodo de reemplazo 2 con generation gap
# para este metodo, el valor de G = k/N
def replacement_method_2_GG(selection_method0, k0, m0, SP0, T0, P0, population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    print ("valor de k: " + str(k))

    N = len(population)
    G = k0/N

    population_to_next_generation, population_to_be_evaluated = generation_gap(G, selection_method0, m0, SP0, T0, P0, population)
    children = do_replacement_method_2(population_to_be_evaluated, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm)

    # Se crea la nueva generacion
    for i in range(0, len(children)):
        population_to_next_generation.append(children[i])

    # Se devuelve la nuega generacion
    return population_to_next_generation

# retorna los hijos mutados
def do_replacement_method_2(population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
    # Se realiza la seleccion
    selected_result = select(population, selection_method, k, m, SP, T, P)

    print ("tamano de selected: " + str(len(selected_result)))

    cross_result = []

    # Se realiza el cross
    for i in range(0, int(len(selected_result) / 2)):
        s1, s2 = cross(pc, selected_result[i], selected_result[len(selected_result) - 1 - i], cross_method)
        cross_result.append(s1)
        cross_result.append(s2)

    print ("tamano de cross: " + str(len(cross_result)))

    # Se realiza la mutacion
    children_result = []
    children = 0
    while children != k:
        idx = sample(range(0, len(cross_result)), 2)
        c1, c2 = mutation(cross_result[idx[0]], cross_result[idx[1]], pm, mutation_method)
        children_result.append(c1)
        children_result.append(c2)
        children += 2

    return children_result

# G entre [0, 1]. Me indica cuantos padres de la generacion t pasan a t + 1
# Se pasa un selection_method0 para la seleccion de individuos que pasan de la generacion
# t a t+1 sin sufrir cambios
# def generation_gap(G, selection_method0, m0, SP0, T0, P0, population, selection_method, k, m, SP, T, P, cross_method, pc, mutation_method, pm):
def generation_gap(G, selection_method0, m0, SP0, T0, P0, population):

    population_to_be_evaluated = []

    if G == 1:
        next_generation = population
    elif G == 0:
        # ninguno individuo de la genenracion t pasa a la proxima generacion
        next_generation = []
    elif 0 < G and G < 1:
        number_of_people = int((1 - G) * len(population))

        # Se realiza la seleccion
        next_generation = selection(population, selection_method0, number_of_people, m0, SP0, T0, P0)

    for i in range(0, len(population)):
        if population[i] in next_generation:
            population_to_be_evaluated.append(population[i])

    return next_generation, population_to_be_evaluated

def copy_population(population):
    pop_copy = []

    N = len(population)

    for p in range(0,N):
        pop_copy.append(population[p].copy())

    return pop_copy