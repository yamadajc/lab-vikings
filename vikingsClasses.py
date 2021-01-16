
import random
# Soldier


class Soldier:
    def __init__(self,health, strength):
        self.health = health
        self.strength = strength
    def attack(self):        
        return self.strength 
    def receiveDamage(self,damage):
        self.health -= damage

    


# Viking


class Viking(Soldier):
    def __init__ (self,name,health,strength): 
        self.name = name
        super().__init__(health, strength)
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage 
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"     
    def battleCry(self):
        return f"A Saxon has died in combat"
    pass

# Saxon


class Saxon(Soldier):
    def __init__ (self,health,strength): 
        super().__init__(health, strength)
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):  
        self.health -= damage 
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    
    
    def vikingAttack(self):         
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        attack = vik.attack()
        clash = sax.receiveDamage(attack)
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        return clash
    def saxonAttack(self):         
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        attack = sax.attack()
        clash = vik.receiveDamage(attack)
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        return clash
    
    def showStatus(self):
        if not self.saxonArmy:
            return f"Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return f"Vikings and Saxons are still in the thick of battle."