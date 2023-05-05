from dices.roll import nDices


def atributeStatistic():
    dices = nDices(4, 6)

    return sum(dices) - min(dices)


def atributeModifier(attribute):
    return int((attribute - 10)/2)


def generateAttribut():
    atribut = atributeStatistic()
    modifier = atributeModifier(atribut)

    return atribut, modifier
