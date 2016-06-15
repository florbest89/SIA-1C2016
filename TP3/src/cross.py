from random import randint
from models import *

# TODO: IMPLEMENT CROSSES METHODS

# TODO: CROSS ONE POINT (CROSS1P)

def cross_1P(p1, p2):
    s1 = p1.copy()
    s2 = p2.copy()

    last = len(p1.items) + 1

    locus = randint(0,last)

    for l in range(locus,last):
        allele1 = p1.get_allele(l)
        allele2 = p2.get_allele(l)

        s1.set_allele(l,allele2)
        s2.set_allele(l,allele1)

    return s1, s2

# TODO: CROSS TWO POINTS (CROSS2P)

# TODO: UNIFORM CORSS (CROSSUNI)

# TODO: ANNULAR CORSS (CROSSANN)