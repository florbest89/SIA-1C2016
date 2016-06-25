from selection import *
from cross import *
from mutation import *
from random import sample

def replacement_method_1(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4,
                         m, SP, T, cross_method, pc, mutation_method, pm):
    N = len(population)

    selected = select_mix(A,N, population,m,T,SP,selection_method1,selection_method2)

    new_generation = transform(selected,cross_method,pc,mutation_method,pm)

    return new_generation

def replacement_method_2(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, cross_method, pc, mutation_method, pm):

    N = len(population)

    selected = select_mix(A, N, population, m, T, SP, selection_method1, selection_method2)
    children = transform(selected,cross_method,pc,mutation_method,pm)

    new_generation = []
    index_individual_for_next_generation = sample(range(0, N), N - k)

    for i in index_individual_for_next_generation:
        new_generation.append(population[i].copy())

    # for i in range(0, len(children)):
    #     new_generation.append(children[i].copy())

    return new_generation + select_mix(B, k, children, m, T, SP, selection_method3, selection_method4)

def replacement_method_3(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, cross_method, pc, mutation_method, pm):

    N = len(population)

    new_generation = copy_population(population)

    selected = select_mix(A, k, population, m, T, SP, selection_method1, selection_method2)

    transformed = transform(selected,cross_method,pc,mutation_method,pm)

    return select_mix(B, N, new_generation + transformed,m,T,SP,selection_method3,selection_method4)

def replacement_mix(population, selection_method,selection_for_replacement_a, selection_for_replacement_b, a, G, m, SP, T, cross_method, pc, mutation_method, pm):

    selected_old = []
    selected_a = []
    selected_b = []

    N = len(population)

    k_old = int(N * (1 - G))

    k_a = int((G / a) * N)

    #To assure that the population keeps being of size N
    k_b = N - k_old - k_a

    selected_old = select(k_old,m,T,SP,population,selection_method)
    selected_a = select(k_a,m,T,SP,population,selection_for_replacement_a)
    selected_b = select(k_b,m,T,SP,population,selection_for_replacement_b)

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
def replacement_gengap(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, G,
                       m, SP, T, cross_method, pc, mutation_method, pm):

    parents_next_generation = []

    N = len(population)
    k = int((1 - G) * N)

    if G == 0:
        return copy_population(population)
    elif G == 1:
        return replacement_method_1(population, A, B, selection_method1, selection_method2, selection_method3,
                                    selection_method4, m, SP, T, cross_method, pc, mutation_method, pm)
    elif 0 < G and G < 1:

        selected = select_mix(A,k,population,m,T,SP,selection_method1,selection_method2)
        parents = sample(population,N-k)

        transformed = transform(selected, cross_method, pc, mutation_method, pm)

    return parents + transformed




def copy_population(population):
    pop_copy = []

    N = len(population)

    for p in range(0,N):
        pop_copy.append(population[p].copy())

    return pop_copy

def replace(population, A, B, replacement_method, selection_method1, selection_method2, selection_method3, selection_method4, a, G, m, SP, T, cross_method, pc, mutation_method, pm,k):

    if replacement_method == 'replacement_one':
        return replacement_method_1(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4,
                         m, SP, T, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_two':
        return replacement_method_2(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_three':
        return replacement_method_3(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, k, m, SP, T, cross_method, pc, mutation_method, pm)
    elif replacement_method == 'replacement_gengap':
        return replacement_gengap(population, A, B, selection_method1, selection_method2, selection_method3, selection_method4, G, m, SP, T, cross_method, pc, mutation_method, pm)
