from random import randint
from models import Item

# TODO: PARSE ITEMS AND CONFIG DOCUMENT


def parse_helmets(lot):
    return parse_items(lot,'./items/cascos.tsv')

def parse_chestplates(lot):
    return parse_items(lot,'./items/pecheras.tsv')

def parse_gauntlets(lot):
    return parse_items(lot,'./items/guantes.tsv')

def parse_weapons(lot):
    return parse_items(lot,'./items/armas.tsv')

def parse_boots(lot):
    return parse_items(lot,'./items/botas.tsv')

def parse_items(lot,file):
    items = []

    with open(file,'r') as f:
        lines = f.readlines()
    f.close()

    while lot > 0:

        i = randint(1,len(lines) - 1)

        line = lines[i].replace('\n','')
        attributes = line.split('\t',5)

        print(attributes)

        items.append(Item(int(attributes[0]),float(attributes[1]),float(attributes[2]),float(attributes[3]),float(attributes[4]),float(attributes[5])))

        lot -= 1

    return items


parse_gauntlets(100)