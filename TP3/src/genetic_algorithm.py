from models import *
from random import uniform
from cross import *
from mutation import *
from selection import *
from replacement import *

def genetic_algorithm():
    #(self, id, strength, resistance, expertise, dexterity, health)
    #(self, helmet, chestplate, gauntlets, weapons, boots, height,sm, rm, em, dm, hm)

    sm = 1.3
    dm = 0.6
    em = 0.6
    rm = 1.2
    hm = 1.1

    number = 100

    helmets = parse_helmets(number)
    chestplates = parse_chestplates(number)
    gauntlets = parse_gauntlets(number)
    weapons = parse_weapons(number)
    boots = parse_boots(number)

    parents = []

    for i in range(0,len(helmets)):
        parents.append(Defender(helmets[i],chestplates[i],gauntlets[i],weapons[i],boots[i],uniform(1.3,2.0),sm,rm,em,dm,hm))
        print('Parent - fitness : ' + str(parents[i].fitness))

    # selected = universal(2,parents)
    # selected = ranking(3, parents, 1.5)
    # selected = deterministicTournament(parents, 3, 2)
    # selected = probabilisticTournament(parents, 3)

    # def replacement_method_2(population, selection_method, k, m, SP, T, P, cross_method, pc,
    #                          mutation, pm):
    selected = replacement_method_2(parents, 'universal', 20, 0, 0, 0, 0, 'cross_1P', 0.5, 'not_uniform', 0.5)

    # selected = boltzmann(parents, 1, 2, 0.5)

    for p in range(0,len(selected)):
        print('Parent ' + str(p) + ' - fitness : ' + str(selected[p].fitness))

    #print('PARENT 2 HEIGHT: ' + str(height2))
    #son1, son2 = cross_annular(parent1,parent2)
    #son1, son2 = mutation(parent1, parent2, 0.5, 'classic')

    var = 2


genetic_algorithm()
