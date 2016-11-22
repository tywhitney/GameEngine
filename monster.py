# Monster.py
# Tyler Whitney
# 11/18/2016

''' Monster Package '''
from character import *
from random import randint, choice

class Monster(Character):
    ''' generic monster class '''
    def __init__(self,
                 name = "Generic Foe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 10,
                 intelligence = 10,
                 dexterity = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 50):
        super(Monster, self).__init__(name, maxHealth, speed, stamina,
                                      strength, intelligence, dexterity,
                                      numberOfPotions, inventory)
        self.aggression = aggression
        self.awareness = awareness
        self.fear = fear  #indicates cowardice level

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale
            
            '''
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            return "h"
        elif fleeValue >= attackValue and fleeValue >= healValue:
            return "f"
        else:
            return "AI_error"

class Orc(Monster):
    ''' generic Orc class '''
    def __init__(self,
                 name = "Dorque da Orc",
                 maxHealth = 100,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 intelligence = 8,
                 dexterity = 8,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 80,
                 awareness = 30,
                 fear = 20):
        super(Orc, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class Skunk(Monster):
    ''' Skunk class '''
    def __init__(self,
                 name = "Pepe LePew",
                 maxHealth = 2,
                 speed = 15,
                 stamina = 5,
                 strength = 4,
                 intelligence = 2,
                 dexterity = 15,
                 numberOfPotions = 0,
                 inventory = [],
                 aggression = 15,
                 awareness = randint(1,9),
                 fear = 60):
        super(Skunk, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
class Hunter(Monster):
    ''' Hunter class '''
    def __init__(self,
                 name = "Shadow Hunter",
                 maxHealth = 100,
                 speed = 50,
                 stamina = 50,
                 strength = 20,
                 intelligence = 30,
                 dexterity = 15,
                 numberOfPotions = 11,
                 inventory = [],
                 aggression = 40,
                 awareness = randint(10,30),
                 fear = 10):
        super(Hunter, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)
class Dragon(Monster):
    ''' Dragon class '''
    def __init__(self,
                 name = "Mag’ladroth",
                 maxHealth = 200,
                 speed = 70,
                 stamina = 45,
                 strength = 94,
                 intelligence = 2,
                 dexterity = 56,
                 numberOfPotions = 0,
                 inventory = [],
                 aggression = 80,
                 awareness = randint(40, 70),
                 fear = 6):
        super(Dragon, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

class King(Monster):
    ''' King class '''
    def __init__(self,
                 name = "Deposed King",
                 maxHealth = 1000,
                 speed = 500,
                 stamina = 600,
                 strength = 9000,
                 intelligence = 654,
                 dexterity = 349,
                 numberOfPotions = 13,
                 inventory = [],
                 aggression = 167,
                 awareness = randint(50,590),
                 fear = 6):
        super(King, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)




def random_monster():
    '''generate a monster at random

    create an instance of each monster here, then add that instance to
    the listOfMonsters.  The function will pick a random instance out of
    the list, then return it to the caller.'''
    
    monster = Monster()
    orc = Orc()
    
    listOfMonsters = [monster, orc]
    return choice(listOfMonsters)


if __name__ == "__main__":

    Grr = Monster(name = "Freddy")
    Randy = random_monster()
    print(Randy.name)


    
