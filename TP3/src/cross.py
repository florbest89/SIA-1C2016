from random import randint
from models import *
import math as m

# TODO: IMPLEMENT CROSSES METHODS

def cross_1P(p1, p2):
    L = len(p1.items) + 1

    locus = randint(0,len(p1.items))
    print('LOCUS : ' + str(locus))

    return cross(p1,p2,locus,L)

def cross_2P(p1,p2):

    max_locus = len(p1.items)

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

def cross_annular(p1,p2):

    L = len(p1.items) + 1

    locus = randint(0,len(p1.items))
    l = randint(1, int(m.floor(L / 2)))

    print('LOCUS : ' + str(locus))
    print('l : ' + str(l))

    if locus + l <= L:
        return cross(p1,p2,locus,locus + l)
    else:
        s1, s2 = cross(p1,p2,locus,L)

        rest = locus + l - L
        for i in range(0, rest):
            allele1 = p1.get_allele(i)
            print('padre 1: alelo locus: ' + str(i))
            allele2 = p2.get_allele(i)
            print('padre 2 alelo locus: ' + str(i))

            s1.set_allele(i, allele2)
            s2.set_allele(i, allele1)

        return s1,s2

def cross(p1,p2,locus_from,locus_to):

    s1 = p1.copy()
    s2 = p2.copy()

    for l in range(locus_from, locus_to):
        allele1 = p1.get_allele(l)
        print('padre 1: alelo locus: ' + str(l))
        allele2 = p2.get_allele(l)
        print('padre 2 alelo locus: ' + str(l))

        s1.set_allele(l, allele2)
        s2.set_allele(l, allele1)

    return s1, s2

# TODO: UNIFORM CORSS (CROSSUNI)
