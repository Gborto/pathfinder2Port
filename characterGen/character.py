#
from dices.statistics import atributeModifier, atributeStatistic


class Atributes:
    atribute = 0
    modifier = 0

    def __init__(self, atribute):
        self.atribute = atribute
        self.modifier = atributeModifier(atribute)

    def attributChange(self, newAtribute):
        self.atribute = newAtribute
        self.modifier = atributeModifier(newAtribute)



class Character:
    name = None
    ancestry = None
    charClass = None
    level = None
    maxHP = None
    currentHP = None

    strenght = None
    dexterity = None
    constitution = None
    inteligence = None
    wisdom = None
    charisma = None

    def __init__(self, name, ancestry, charClass, level=0, maxHP, currentHP):
        self.name = name
        self.ancestry = ancestry
        self.charClass = charClass
        self.level = level
        self.maxHP = maxHP
        self.currentHP = currentHP

        self.strenght = Atributes(atributeStatistic())
        self.dexterity = Atributes(atributeStatistic())
        self.constitution = Atributes(atributeStatistic())
        self.inteligence = Atributes(atributeStatistic())
        self.wisdom = Atributes(atributeStatistic())
        self.charisma = Atributes(atributeStatistic())

    def __repr__(self) -> str:
        strOut = f'Name: {self.name}\nRace: {self.ancestry}\n' + \
            f'Class: {self.charClass}\nLevel: {self.level}'
        strOut += f'Strenght:  {self.strenght.atribute}\n'
        strOut += f'Dexterity: {self.dexterity.atribute}\n'
        strOut += f'Constitution: {self.constitution.atribute}\n'
        strOut += f'Inteligence: {self.inteligence.atribute}\n'
        strOut += f'Wisdom: {self.wisdom.atribute}\n'
        strOut += f'Charisma: {self.charisma.atribute}\n'

        return strOut
