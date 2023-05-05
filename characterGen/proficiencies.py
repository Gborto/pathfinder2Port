level = 1

def proficiencyScores(profRank):
    if profRank == 'untrained':
       profBonus = 0
    elif profRank == 'trained':
        profBonus = 2 + level
    elif profRank == 'expert':
        profBonus = 4 + level
    elif profRank == 'master':
        profBonus = 6 + level
    elif profRank == 'Legendary':
        profBonus = 8 + level

        return profBonus

class Proficiency:
    profRank = None
    profBonus = proficiencyScores(profRank)

    def __init__ (self, profRank='untrained', profBonus):
        self.profRank = profRank
        self.profBonus = profBonus


class WeaponProficiencies:
    unarmed = None
    simpleWeapons = None
    uncommonSimpleWeapons = None
    martialWeapons = None
    uncommonMartialWeapons = None    

    def __init__(self, unarmed='untrained', simpleWeapons='untrained',
                  uncommonSimpleWeapons='untrained', martialWeapons='untrained',
                  uncommonMartialWeapons='untrained'):
        self.unarmed = unarmed
        self.simpleWeapons = simpleWeapons
        self.uncommonSimpleWeapons = uncommonSimpleWeapons
        self.martialWeapons = martialWeapons
        self.uncommonMartialWeapons = uncommonMartialWeapons