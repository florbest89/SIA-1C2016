from random import randint
from models import *

# TODO: IMPLEMENT CROSSES METHODS

def cross_1P(p1, p2):
    last = len(p1.items) + 1

    locus = randint(0,last)
    print('LOCUS : ' + str(locus))

    return cross(p1,p2,locus,last)


def cross_2P(p1,p2):

    max_locus = len(p1.items) + 1

    locus = randint(0, max_locus)
    locus2 = randint(0, max_locus)

    print('LOCUS 1 : ' + str(locus))
    print('LOCUS 2 : ' + str(locus2))

    if locus < locus2:
        return cross(p1,p2,locus,locus2 + 1)
    elif locus > locus2 :
        return cross(p1,p2,locus2,locus + 1)
    else:
        return cross_2P(p1,p2)


def cross(p1,p2,locus_from,locus_to):
    s1 = p1.copy()
    s2 = p2.copy()

    for l in range(locus_from, locus_to):
        allele1 = p1.get_allele(l)
        allele2 = p2.get_allele(l)

        s1.set_allele(l, allele2)
        s2.set_allele(l, allele1)

    return s1, s2



# TODO: UNIFORM CORSS (CROSSUNI)

# TODO: ANNULAR CORSS (CROSSANN)