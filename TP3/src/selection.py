from models import Defender
from random import uniform
from random import sample
# TODO: IMPLEMENT SELECTION METHODS

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
        q = 0

        L = len(r)

        for i in range(0, L):

            qi = r[i][2]

            if q < rj < qi:
                ind = r.pop(i)
                selected.append(ind[3])
                k -= 1
                break
            else:
                q = r[i][2]

    return selected

def prepare_fitness_lineal(fitness_lineal,population):
    r = []
    total = sum(fitness_lineal)
    acum = 0.0

    for p in range(0,len(fitness_lineal)):
        relative = fitness_lineal[p] / total
        acum += relative
        r.append([fitness_lineal[p], relative, acum, population[p].copy()])
        print('order: ' + str(p) + ' fitness_lineal: ' + str(fitness_lineal[p]) + ' relative: ' + str(relative) + ' acum: ' +
              str(acum) + ' fitness: ' + str(population[p].fitness))

    return r

def prepare_population(population):

    r = []

    total_fitness = sum(p.fitness for p in population)
    acum = 0.0

    for p in range(0,len(population)):
        relative = population[p].fitness / total_fitness
        acum += relative
        r.append([population[p].fitness, relative, acum, population[p].copy()])
        print('fitness: ' + str(population[p].fitness) + 'relative: ' +  str(relative) + ' acum: ' + str(acum))

    return r


# TODO: UNIVERSAL

# TODO: BOLTZMANN

# TODO: DETERMINISTIC TOURNAMENT
def deterministicTournament(population, k, m):
    # k repeticiones, m individuos en torneo
    selected = []

    while k > 0:
        best_fitness = 0
        selected_ind = sample(range(0,len(population) - 1), m)
        for p in selected_ind:
            if best_fitness < population[p].fitness:
                best_fitness = population[p].fitness
                best_individual = population[p]
        selected.append(best_individual)
        k -= 1

    return selected

# TODO: PROBABILISTIC TOURNAMENT
def probabilisticTournament(population, k):
    # k repeticiones
    selected = []

    while k > 0:
        r = uniform(0, 1)

        # selecciono siempre de a 2
        selected_ind = sample(range(0,len(population) - 1), 2)

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
# TODO: RANKING

def elite(N, population):

    if N < len(population):
        population.sort(key=lambda p: p.fitness, reverse=True)
        return population[0:N]
    elif N == len(population):
        return population

