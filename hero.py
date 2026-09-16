import random
class Hero:
    """The hero blueprint will be implemented later in the project."""


    def __init__(self, name): #name will come from code creating hero
        self.name = name #should be different for each hero
        self.health = 120 #Every hero will have same health unless their is a loop or you pass in as parameter
        self.attack_power = 15

    def attack(self):
        return random.randint(1, self.attack_power) 


    def take_damage(self, damage): 
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

        if self.health == 0:
            print(f"THE ALMIGHTY HERO {self.name} HAS FALLEN :(")
    

    def is_alive(self):
        return self.health > 0


