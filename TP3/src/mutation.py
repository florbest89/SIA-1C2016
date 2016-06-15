from models import *
from random import randint, uniform
from custom_parser import *

# TODO: CLASSIC


def not_uniform(individual):

    L = len(individual.items)

    locus = randint(0,L)

    if locus == 0:
        mutation = parse_helmets(1)[0]
    elif locus == 1 :
        mutation = parse_chestplates(1)[0]
    elif locus == 2:
        mutation = parse_gauntlets(1)[0]
    elif locus == 3:
        mutation = parse_weapons(1)[0]
    elif locus == 4:
        mutation = parse_boots(1)[0]
    else:
        mutation = uniform(1.3,2.0)

    individual.set_allele(locus,mutation)

    return individual
