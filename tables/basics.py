''' Este módulo possui tabelas de geração de características dos perssonagens '''

import csv
hpPerAncestry = {
    'dwarf': 10,
    'elf': 6,
    'gnome': 8,
    'goblin': 8,
    'halfling': 6,
    'human': 8
}

hpPerClass = {
    'alchemist': 8,
    'barbarian': 12,
    'bard': 8,
    'champion': 10,
    'cleric': 8,
    'druid': 8,
    'fighter': 10,
    'monk': 10,
    'ranger': 10,
    'rogue': 8,
    'sorcerer': 6,
    'wizard': 6
}


class Armor:
    name = None
    armorProficiency = None
    price = None
    acBonus = None
    dexCap = None
    checkPenalty = None
    speedPenalty = None
    strength = None
    bulk = None
    group = None
    armorTraits = None

    def __init__(self, name, armorProficiency, price, acBonus, dexCap, checkPenalty,
                 speedPenalty, strength, bulk, group, armorTraits):
        self.name = name
        self.armorProficiency = armorProficiency
        self.price = self.strToPrice(price)
        self.acBonus = int(acBonus)
        self.dexCap = int(dexCap)
        self.checkPenalty = checkPenalty
        self.speedPenalty = speedPenalty
        self.strength = strength
        self.bulk = bulk
        self.group = group
        self.armorTraits = armorTraits

    def strToPrice(self, string):
        value = 0
        if string.find('sp'):
            value = int(string.split()[0])*10
        elif string.find('gp'):
            value = int(string.split()[0])*100
        else:
            value = int(string()[0])
        return value

    def __repr__(self):
        return f'{self.name}\t{self.armorProficiency}\t{self.price}\t{self.acBonus}' +\
            f'{self.dexCap}\t{self.checkPenalty}\t{self.speedPenalty}\t{self.strength}' +\
            f'{self.bulk}\t{self.group}\t{self.armorTraits}'


class ArmorTable:
    ''' ArmorTable is a class meant for generating a class that loads an armor table '''
    listArmors = {}

    def loadArmors(self):
        ''' loadArmors loads armor.csv to generate diferent kinds of armor '''
        with open('armor.csv') as csvfile:
            skipLine = True
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                if skipLine:
                    skipLine = False
                    continue
                print(row)
                armor = Armor(*row)
                self.listArmors[armor.name] = armor
