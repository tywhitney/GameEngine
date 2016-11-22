# character.py
# Tyler Whitney
# 11/16/2016

''' Module that contains our game's Character base class
    CHANGELOG:
    11/17/2016
      added a combat_choice method for use by player
    11/17/2016
      changed the Character class. weapon, armor and potion attributes.
    These are all objects imported from the new items module. These
    attributes are all implemented as objects.  Potions are implemented
    additionally as a list of objects.  This leaves inventory currently
    empty. also, a new constructor parameter has been added:
        numberOfPotions = 2. this replaces the old inventory item
        ["potion", 2]...
    Additionally, a number of properties were added to the base class:
        strBonus, dexBonus, intBonus, potionCount, potionList, and AC.
        see the property docstrings for more information
    11/21/2016
      added constitution, wisdom, and charisma attributes. modified attack
    to do a minimum of 1 damage, as well as added the possibility of a
    critical fumble (roll of 1).
    11/21/2016
      added __str__ method to allow easy printing.
    

'''
from random import randint
from items import *

class Character(object):
    ''' Base Character Class '''
    def __init__(self,
                 name = "Average Joe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 10,
                 dexterity = 10,
                 constitution = 10,
                 intelligence = 10,
                 wisdom = 10,
                 charisma = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 weapon = "",
                 armor = ""):
        ''' All values represent the average score '''
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.speed = speed
        self.hunger = 100 # 100 = Full, 0 = starving
        self.stamina = stamina
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.inventory = []
        for item in inventory:
            self.inventory.append(item[:])
        self.potions = []
        for i in range(numberOfPotions):
            self.potions.append(Potion())
        if weapon == "":
            self.weapon = Weapon()
        else:
            self.weapon = weapon
        if armor == "":
            self.armor = Armor()
        else:
            self.armor = armor

    @property
    def strBonus(self):
        ''' calculates d20 OGL bonus for strength'''
        return (self.strength//2) - 5

    @property
    def dexBonus(self):
        ''' calculates d20 OGL bonus for dexterity'''
        return (self.dexterity//2) - 5

    @property
    def conBonus(self):
        ''' calculates d20 OGL bonus for dexterity'''
        return (self.constitution//2) - 5

    @property
    def intBonus(self):
        ''' calculates d20 OGL bonus for intelligence'''
        return (self.intelligence//2) - 5

    @property
    def wisBonus(self):
        ''' calculates d20 OGL bonus for dexterity'''
        return (self.wisdom//2) - 5

    @property
    def chaBonus(self):
        ''' calculates d20 OGL bonus for dexterity'''
        return (self.charisma//2) - 5


    @property
    def potionCount(self):
        ''' counts your potions... :/ <- david, that is an emoji'''
        return len(self.potions)

    @property
    def potionList(self):
        ''' produces a list of potions by name '''
        potionNames = ""
        for potion in self.potions:
            potionNames += potion.name + ", "
        potionNames = potionNames[:-2] #strip off the last ", "
        return potionNames

    @property
    def AC(self):
        ''' calculates the overall d20 OGL Armor Class (AC) value'''
        return 10 + self.dexBonus + self.armor.defense

    def get_damaged(self, damage):
        ''' inflicts damage from an outside source '''
        self.health -= damage

    def heal(self):
        ''' randomly heal 1d8+1 points

            this method, like the other action methods, returns two values
            which may or may not be used by the main program.  the first value
            is a Boolean: success.  Hopefully, that one is self-explanatory.
            message is just a text string that gives the game some descriptive
            text to give the user.'''
        
        success = False
        message = ""
        
        #first check if there is a potion in inventory
        if self.potionCount > 0:

            #if so, use the last one, then pop it off the list
            ''' NOTE: this is fine for now, since there's only one type of
                potion, but later the user should be given a choice of which
                to use...'''
            amount = self.potions[-1].use()  
            self.health += amount
            self.potions.pop()

            if self.health > self.maxHealth:
                self.health = self.maxHealth

            success = True
            message = self.name + " drinks a potion, and heals " +\
                      str(amount) + " points."
        if not success:
            message = self.name + " has no potions!"

        return success, message

    def flee(self):
        ''' attempt to flee the combat, based on speed.

            this method, like the other action methods, returns two values
            which may or may not be used by the main program.  the first value
            is a Boolean: success.  Hopefully, that one is self-explanatory.
            message is just a text string that gives the game some descriptive
            text to give the user.'''

        success = False
        message = ""
        
        chance = randint(1,100)
        if chance <= self.speed:
            success = True
            message = "When danger reared it's ugly head,\n" + self.name +\
                      " bravely turned and fled!"
        else:
            message = self.name + " tried to flee, but couldn't get away!"

        return success, message

    def attack(self, enemy):
        ''' attack another Character

            this method, like the other action methods, returns two values
            which may or may not be used by the main program.  the first value
            is a Boolean: success.  Hopefully, that one is self-explanatory.
            message is just a text string that gives the game some descriptive
            text to give the user.'''

        success = False
        message = ""
        roll = randint(1,20)
        if roll == 1:
            success = False
            message = self.name + "fumbles their attack!"

        else:
            attack = roll + self.strBonus + self.weapon.attack
            if attack >= enemy.AC:
                damage = self.weapon.damage + self.strBonus
                if damage < 1:
                    damage = 1
                enemy.get_damaged(damage)
                success = True
                message = self.name + " hits " + enemy.name + " and does " +\
                          str(damage) + " damage."
            else:
                message = self.name + " misses " + enemy.name + "."

        return success, message

    def combat_choice(self):
        ''' player's combat choices'''
        choice = input("""
                  YOU ARE IN COMBAT!
                  What do you want to do?
                  You can:
                     A)ttack
                     H)eal
                     F)lee
                   Your Choice [A/h/f]: """)
        return choice

    def __str__(self):
        info = "NAME:       " + self.name + "\n" +\
               "-----------------------------------\n" +\
               "|STR| "+str(self.strength)+"\t"+str(self.strBonus)+"\n"+\
               "|DEX| "+str(self.dexterity)+"\t"+str(self.dexBonus)+"\n"+\
               "|CON| "+str(self.constitution)+"\t"+str(self.conBonus)+"\n"+\
               "|INT| "+str(self.intelligence)+"\t"+str(self.intBonus)+"\n"+\
               "|WIS| "+str(self.wisdom)+"\t"+str(self.wisBonus)+"\n"+\
               "|CHA| "+str(self.charisma)+"\t"+str(self.chaBonus)+"\n"+\
               "-----------------------------------\n" +\
               "Potions: "+self.potionList+"\n"+\
               "AC:      "+str(self.AC)+"\n"+\
               "-----------------------------------\n"
        return info
    
if __name__ == "__main__":
    hero = Character(name = "Mr. Peebles")
    orc = Character(name = "Magilla")
    print(hero.potionCount)
    print(hero.potionList)
    hero.heal()
    print(hero.potionList)
    print(hero.attack(orc))
    print(hero)
    print(orc)

    













        
        
