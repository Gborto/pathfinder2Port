#
from dices.statistics import atributeModifier, atributeStatistic


class Atribut:
    atribut = 0
    modifier = 0

    def __init__(self, atribut):
        self.atribut = atribut
        self.modifier = atributeModifier(atribut)

    def attributChange(self, newAttribut):
        self.atribut = newAttribut
        self.modifier = atributeModifier(newAttribut)


class Player:
    name = None
    race = None
    charClass = None

    strenght = None
    dexterity = None
    constitution = None
    inteligence = None
    wisdom = None
    charisma = None

    def __init__(self, name, race, charClass):
        self.name = name
        self.race = race
        self.charClass = charClass

        self.strenght = Atribut(atributeStatistic())
        self.dexterity = Atribut(atributeStatistic())
        self.constitution = Atribut(atributeStatistic())
        self.inteligence = Atribut(atributeStatistic())
        self.wisdom = Atribut(atributeStatistic())
        self.charisma = Atribut(atributeStatistic())

    def __repr__(self) -> str:
        strOut = f'Name: {self.name}\nRace: {self.race}\n' + \
            f'Class: {self.charClass}\n'
        strOut += f'Strenght:  {self.strenght.atribut}\n'
        strOut += f'Dexterity: {self.dexterity.atribut}\n'
        strOut += f'Constitution: {self.constitution.atribut}\n'
        strOut += f'Inteligence: {self.inteligence.atribut}\n'
        strOut += f'Wisdom: {self.wisdom.atribut}\n'
        strOut += f'Charisma: {self.charisma.atribut}\n'

        return strOut
