import random


def diceN(dice):
    return random.randint(1, dice)


def nDices(n, dice):
    dices = []
    for i in range(n):
        dices.append(diceN(dice))

    return dices
