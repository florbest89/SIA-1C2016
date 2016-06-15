from models import *
from random import uniform
from cross import *


def genetic_algorithm():
    #(self, id, strength, resistance, expertise, dexterity, health)
    #(self, helmet, chestplate, gauntlets, weapons, boots, height,sm, rm, em, dm, hm)

    sm = 1.3
    dm = 0.6
    em = 0.6
    rm = 1.2
    hm = 1.1

    helmet1 = Item(0,1.51,3.17,6.41,13.96,4.93)
    chestplate1 = Item(0,6.08,9.29,13.03,10.46,1.12)
    gauntlets1 = Item(0,1.11,0.55,2.85,3.31,2.16)
    weapons1 = Item(0,5.05,5.11,6.11,10.55,23.15)
    boots1 = Item(0,2.13,3.23,2.34,1.97,0.31)
    height1 = uniform(1.3,2.0)

    print('PARENT 1 HEIGHT: ' + str(height1))

    parent1 = Defender(helmet1,chestplate1,gauntlets1,weapons1,boots1,height1,sm,rm,em,dm,hm)

    helmet2 = Item(1,5.37,1.37,9.58,7.52,6.13)
    chestplate2 = Item(1,13.68,1.75,16.33,0.34,7.87)
    gauntlets2 = Item(1,2.22,2.49,1.01,1.16,3.10)
    weapons2 = Item(1,8.91,12.37,8.90,4.22,15.57)
    boots2 = Item(1,0.46,1.89,5.13,1.14,1.36)
    height2 = uniform(1.3,2.0)

    parent2 = Defender(helmet2,chestplate2,gauntlets2,weapons2,boots2,height2,sm,rm,em,dm,hm)

    print('PARENT 2 HEIGHT: ' + str(height2))

    son1, son2 = cross_annular(parent1,parent2)

    print(son1)
    print(son2)


genetic_algorithm()
