from models import Defender
from random import uniform
from random import sample
from math import exp

def roulette(k,population):
    # 0 - fitness , 1 - relative , 2 - acum, 3 - individual

    if k == len(population):
        return population

    r = prepare_population(population)

    selected = []

    while k > 0:
        rj = uniform(0,1)
        q = 0

        L = len(r)

        for i in range(0,L):

            qi = r[i][2]

            if q < rj < qi :
                ind = r.pop(i)
                selected.append(ind[3])
                k -=1
                break
            else:
                q = r[i][2]

    return selected

# linear ranking selection
# SP entre [1.0-2.0]
def ranking(k,population, SP):
    # 0 - fitness , 1 - relative , 2 - acum, 3 - individual

    population.sort(key=lambda p: p.fitness, reverse=False)

    n = len(population)
    fitness_lineal = [0]*n

    for i in range(0, n):
        fitness_lineal[i] = 2 - SP + (2*(SP - 1)*(i - 1)/(n - 1))

    r = prepare_fitness_lineal(fitness_lineal, population)
    selected = []

    while k > 0:
        rj = uniform(0, 1)

        L = len(r)

        for i in range(0, L):

            qi = r[i][2]

            if rj < qi:
                ind = r.pop(i)
                selected.append(ind[3])
                k -= 1
                break

    return selected

def prepare_fitness_lineal(fitness_lineal,population):
    r = []
    total = sum(fitness_lineal)
    acum = 0.0

    for p in range(0,len(fitness_lineal)):
        relative = fitness_lineal[p] / total
        acum += relative
        r.append([fitness_lineal[p], relative, acum, population[p].copy()])

    return r

def prepare_population(population):

    r = []

    total_fitness = sum(p.fitness for p in population)
    acum = 0.0

    for p in range(0,len(population)):
        relative = population[p].fitness / total_fitness
        acum += relative
        r.append([population[p].fitness, relative, acum, population[p].copy()])
        # print('fitness: ' + str(population[p].fitness) + 'relative: ' +  str(relative) + ' acum: ' + str(acum))

    return r

def universal(k,population):
    pop_fit = prepare_population(population)
    r = uniform(0,1)

    rjs = universal_r(r,k)

    selected = []

    while k > 0:

        q = 0

        L = len(pop_fit)

        for j in range(0,len(rjs)):

            rj = rjs[j]

            for i in range(0, L):

                qi = pop_fit[i][2]

                if q < rj < qi:
                    #ind = pop_fit.pop(i)
                    selected.append(pop_fit[i][3])
                    k -= 1
                    break
                else:
                    q = pop_fit[i][2]

    return selected

def universal_r(r,k):
    rj = []

    for j in range(1,k + 1):
        rj.append((r + j - 1)/k)

    return rj

# Cada vez que se ingresa, el valor de temperatura T debe ser menor
# para el correcto funcionamiento del metodo.
# k cant de individuos
# T temperatura
def boltzmann(population, k, T):

    N = len(population)

    # Si la cantidad de individuos a buscar en mayor a la poblacion
    if k >= N:
        return population

    r = prepare_botlzmann(population, T)
    selected = []

    while k > 0:
        q = 0
        rj = uniform(0, 1)

        L = len(r)
        for i in range(0,L):
            qi = r[i][1]

            if q < rj < qi:
                ind = r.pop(i)
                selected.append(ind)
                k -= 1
                break
            else:
                q = r[i][1]

    return selected

def prepare_botlzmann(population, T):
    # 0 - exp_val, 1 - acum, 2 - individual
    r = []
    acum = 0.0

    for i in range(0, len(population)):
        acum = acum + exp(population[i].fitness / T);

    for i in range(0, len(population)):
        exp_val = exp(population[i].fitness / T) / acum;
        r.append([exp_val, acum, population[i].copy()])
        print('exp_val: ' + str(exp_val) + ' acum: ' + str(acum) + ' fitness: ' + str(population[i].fitness))

    return r

def deterministic_Tournament(population, k, m):
    # k repeticiones, m individuos en torneo
    selected = []

    while k > 0:
        best_fitness = 0

        selected_ind = sample(range(0, len(population) - 1), m)
        for p in selected_ind:
            if best_fitness < population[p].fitness:
                best_fitness = population[p].fitness
                best_individual = population[p]
        selected.append(best_individual)
        k -= 1

    return selected

def probabilistic_Tournament(population, k):
    # k repeticiones
    selected = []

    while k > 0:
        r = uniform(0, 1)

        # selecciono siempre de a 2

        selected_ind = sample(range(0, len(population) - 1), 2)

        if population[selected_ind[0]].fitness < population[selected_ind[1]].fitness:
            best_fitness = population[selected_ind[1]]
            worst_fitness = population[selected_ind[0]]
        else:
            best_fitness = population[selected_ind[0]]
            worst_fitness = population[selected_ind[1]]

        if r >= 0.75:
            selected.append(best_fitness)
        else:
            selected.append(worst_fitness)

        k -= 1

    return selected

def elite(k, population):
    population.sort(key=lambda p: p.fitness, reverse=True)

    if k < len(population):
        return population[0:k]
    elif k == len(population):
        return population

def select(k,m,T,SP,population,selection_method):

    if selection_method == 'elite':
        return elite(k,population)
    elif selection_method == 'universal':
        return universal(k,population)
    elif selection_method == 'roulette':
        return roulette(k,population)
    elif selection_method == 'ranking':
        return ranking(k,population,SP)
    elif selection_method == 'boltzmann':
        return boltzmann(population,k,T)
    elif selection_method == 'deterministic_tournament':
        return deterministic_Tournament(population,k,m)
    else:
        return probabilistic_Tournament(population,k)

def select_mix(A,N, population,m,T,SP,selection_method_a,selection_method_b):

    N_a = int(A * N)
    N_b = N - N_a

    selected_a = select(N_a, m, T, SP, population, selection_method_a)
    selected_b = select(N_b, m, T, SP, population, selection_method_b)

    return selected_a + selected_b

