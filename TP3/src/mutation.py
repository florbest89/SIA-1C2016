from models import *
from random import randint, uniform
from custom_parser import *


def classic(individual,p):
    L = len(individual.items) + 1

    for l in range(0,L):
        r = uniform(0,1)

        if r < p:
            m = mutate_locus(l)
            individual.set_allele(l, m)

    return individual

def not_uniform(individual):

    L = len(individual.items)

    locus = randint(0,L)

    m = mutate_locus(locus)

    individual.set_allele(locus,m)

    return individual

def mutate_locus(locus):

    if locus == 0:
        return parse_helmets(1)[0]
    elif locus == 1:
        return parse_chestplates(1)[0]
    elif locus == 2:
        return parse_gauntlets(1)[0]
    elif locus == 3:
        return parse_weapons(1)[0]
    elif locus == 4:
        return parse_boots(1)[0]
    else:
        return uniform(1.3, 2.0)

def mutation(c1, c2, pm, mutation_method):

    p = uniform(0,1)

    if p < pm:
        c1 = mutate(c1, mutation_method)

    p = uniform(0,1)

    if p < pm:
        c2 = mutate(c2,mutation_method)

    return c1,c2

def mutate(individual, mutation_method):

    if mutation_method == 'classic':
        return classic(individual, 0.5)

    if mutation_method == 'not_uniform':
        return not_uniform(individual)