from random import randint
from models import Item

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

def parse_config():
    # 0 - N , 1 - pm, 2 - pc, 3 - G
    parameters = [None] * 4
    # 0 - sm, 1 - dm, 2 - em, 3 - rm, 4 - hm
    multipliers = [None] * 5
    # 0 - selection, 1 - cross, 2 - mutation, 3 - replacement
    methods = [None] * 4

    file = './config.txt'

    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()

    L = len(lines)

    for l in range(0,L):

        first_char = lines[l][0]

        if first_char != '#' and first_char != '*' and first_char != '\n':
            line = lines[l].replace('\n', '')
            param = line.split(' ', 1)

            key = param[0]
            value = param[1]

            if key == 'N':
                parameters[0] = int(value)
            elif key == 'pm':
                parameters[1] = float(value)
            elif key == 'pc':
                parameters[2] = float(value)
            elif key == 'G':
                parameters[3] = float(value)
            elif key == 'sm':
                multipliers[0] = float(value)
            elif key == 'dm':
                multipliers[1] = float(value)
            elif key == 'em':
                multipliers[2] = float(value)
            elif key == 'rm':
                multipliers[3] = float(value)
            elif key == 'hm':
                multipliers[4] = float(value)
            elif key == 'selection':
                methods[0] = value
            elif key == 'cross':
                methods[1] = value
            elif key == 'mutation':
                methods[2] = value
            elif key == 'replacement':
                methods[3] = value
            elif key == 'replacement':
                methods[4] = value

    return parameters, multipliers, methods

parse_config()