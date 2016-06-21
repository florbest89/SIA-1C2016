from random import randint, uniform
from models import *
import math as m

def cross_1P(p1, p2):
    L = len(p1.items) + 1

    locus = randint(0,len(p1.items))

    return do_cross(p1,p2,locus,L,2)

def cross_2P(p1,p2):

    max_locus = len(p1.items)

    locus = randint(0, max_locus)
    locus2 = randint(0, max_locus)
    
    if locus < locus2:
        return do_cross(p1,p2,locus,locus2 + 1,2)
    elif locus > locus2 :
        return do_cross(p1,p2,locus2,locus + 1,2)
    else:
        return cross_2P(p1,p2)

def cross_annular(p1,p2):

    L = len(p1.items) + 1

    locus = randint(0,len(p1.items))
    l = randint(1, int(m.floor(L / 2)))

    if locus + l <= L:
        return do_cross(p1,p2,locus,locus + l,2)
    else:
        s1, s2 = do_cross(p1,p2,locus,L,2)

        rest = locus + l - L
        for i in range(0, rest):
            allele1 = p1.get_allele(i)
            allele2 = p2.get_allele(i)

            s1.set_allele(i, allele2)
            s2.set_allele(i, allele1)

        return s1,s2

def cross_uniform(p1,p2):
    L = len(p1.items) + 1

    return do_cross(p1,p2,0,L,0.5)

def do_cross(p1,p2,locus_from,locus_to,pc):

    s1 = p1.copy()
    s2 = p2.copy()

    for l in range(locus_from, locus_to):
        p = uniform(0, 1)

        if p < pc:
            allele1 = p1.get_allele(l)
            allele2 = p2.get_allele(l)

            s1.set_allele(l, allele2)
            s2.set_allele(l, allele1)

    return s1, s2

def cross(pc,p1,p2,cross_method):
    p = uniform(0, 1)

    if p < pc:
        if cross_method == 'cross_1P':
            return cross_1P(p1,p2)

        if cross_method == 'cross_2P':
            return cross_2P(p1,p2)

        if cross_method == 'cross_annular':
            return cross_annular(p1,p2)

        if cross_method == 'cross_uniform':
            return cross_uniform(p1,p2)
    else:
        return p1.copy(),p2.copy()



