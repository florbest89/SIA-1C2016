import math as m

class Item(object):
    def __init__(self, id, strength, dexterity, expertise,  resistance, health):
        self.id = id
        self.strength = strength
        self.resistance = resistance
        self.expertise = expertise
        self.dexterity = dexterity
        self.health = health

    def copy(self):
        return Item(self.id,self.strength,self.dexterity,self.expertise,self.resistance,self.health)


class Defender(object):
    def __init__(self, helmet, chestplate, gauntlets, weapons, boots, height,sm, rm, em, dm, hm):

        # Items [ index - description ]
        # [0 - helmet, 1 - chestplate, 2 - gauntlets, 3 - weapons, 4 - boots]
        self.items = []
        self.items.append(helmet)
        self.items.append(chestplate)
        self.items.append(gauntlets)
        self.items.append(weapons)
        self.items.append(boots)

        # For cross purposes height is in locus 5:
        # [0 - helmet, 1 - chestplate, 2 - gauntlets, 3 - weapons, 4 - boots, 5 - height]
        self.height = height

        # m = multiplier. Example: sm = Strength Multiplier
        self.sm = sm
        self.rm = rm
        self.em = em
        self.dm = dm
        self.hm = hm

        # Compute fitness of defender
        # TODO: CHECK FOR OTHER POSSIBILITIES
        self.fitness = self.compute_fitness()

    def copy(self):
        items = []

        for i in range(0,len(self.items)):
            items.append(self.items[i].copy())

        return Defender(self.items[0],self.items[1],self.items[2],self.items[3],self.items[4],self.height,self.sm,self.rm,self.em,self.dm,self.hm)


    def ATM(self):
        h = self.height
        return 0.5 - m.pow((3*h - 5),4) + m.pow((3*h - 5),2) + h/2

    def DEM(self):
        h = self.height
        return 2 + m.pow((3 * h - 5), 4) - m.pow((3 * h - 5), 2) - h / 2

    def strength_items(self):
        strength = 0.0

        for i in range(0, len(self.items)):
            strength = strength + self.items[i].strength

        return strength * self.sm

    def dexterity_items(self):
        dexterity = 0.0

        for i in range(0, len(self.items)):
            dexterity = dexterity + self.items[i].dexterity

        return dexterity * self.dm

    def expertise_items(self):
        expertise = 0.0

        for i in range(0,len(self.items)):
            expertise = expertise + self.items[i].expertise

        return expertise * self.em

    def resistance_items(self):
        resistance = 0.0

        for i in range(0, len(self.items)):
            resistance = resistance + self.items[i].resistance

        return resistance * self.rm

    def health_items(self):
        health = 0.0

        for i in range(0, len(self.items)):
            health = health + self.items[i].health

        return health * self.hm

    def strength(self):
        return 100 * m.tanh(0.01 * self.strength_items())

    def dexterity(self):
        return m.tanh(0.01 * self.dexterity_items())

    def expertise(self):
        return 0.6 * m.tanh(0.01 * self.expertise_items())

    def resistance(self):
        return m.tanh(0.01 * self.resistance_items())

    def health(self):
        return 100 * m.tanh(0.01 * self.health_items())

    def attack(self):
        return (self.dexterity() + self.expertise()) * self.strength() * self.ATM()

    def defense(self):
        return (self.resistance() + self.expertise()) * self.health() * self.DEM()

    def compute_fitness(self):
        return 0.1 * self.attack() + 0.9 * self.defense()

    def get_allele(self,locus):
        if locus >= 0 and locus <= 4:
            return self.items[locus]
        else:
            return self.height

    def set_allele(self,locus,allele):
        if locus >= 0 and locus <= 4:
            self.items[locus] = allele
        else:
            self.height = allele
