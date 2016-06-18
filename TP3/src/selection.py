from models import Defender
from random import uniform
# TODO: IMPLEMENT SELECTION METHODS

def roulette(k,population):
    # 0 - fitness , 1 - relative , 2 - acum, 3 - individual
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

# TODO: PROBABILISTIC TOURNAMENT

# TODO: RANKING

def elite(N, population):

    if N < len(population):
        population.sort(key=lambda p: p.fitness, reverse=True)
        return population[0:N]
    elif N == len(population):
        return population

