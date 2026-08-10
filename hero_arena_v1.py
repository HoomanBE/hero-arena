import random

class Hero:
    def __init__(self):
        self.name = ""
        self.class_character = ""
        self.hp = 0
        self.damage = 0
        
    def hero_class(self):
        
        self.name = input("Enter your character name: ")
        while True:
            choose_class = input("\nChoose your hero class:\n"
                                 "1)Bandit\n"
                                 "2)Samurai\n"
                                 "3)Knight (1,2,3): Please enter number: ")
            if choose_class == '1':
                self.class_character = "Bandit"
                self.hp = 50
                self.damage = 50
                break
            elif choose_class == '2' :
                self.class_character = "Samurai"
                self.hp = 30
                self.damage = 70
                break
            elif choose_class == '3':
                self.class_character = "Knight"
                self.hp = 80
                self.damage = 20
                break
            else:
                print("Enter a valid number!")
                continue
            
    def show_status(self):
        print(f"\nYour character name is {self.name}\n"
              f"Your class is {self.class_character}\n"
              f"Your hp is {self.hp}\n"
              f"Your damage is {self.damage}")  

    def attack(self, enemy):
        enemy.hp -= self.damage
        if enemy.hp > 0 :
            print(f"\nEnemy hp is {enemy.hp}")
        else:
            return enemy.hp <= 0
        
class Enemy:
    def __init__(self):
        self.name = ""
        self.class_character = ""
        self.hp = 0
        self.damage = 0
        
    def enemy_class(self):
        choose_class = random.randint(1,3)
        if choose_class == 1:
            self.name = 'Billy the Kid'
            self.class_character = "Bandit"
            self.hp = 50
            self.damage = 50
               
        elif choose_class == 2:
            self.name = 'Miyamoto Musashi'
            self.class_character = "Samurai"
            self.hp = 30
            self.damage = 70
            
        elif choose_class == 3:
            self.name = 'Sir Thomas More'
            self.class_character = "Knight"
            self.hp = 80
            self.damage = 20 
            
    def show_status(self):
        print(f"\nYour enemy name is {self.name}\n"
              f"Your enemy class is {self.class_character}\n"
              f"Your enemy hp is {self.hp}\n"
              f"Your enemy damage is {self.damage}")     
    
    def attack(self, hero):
        hero.hp -= self.damage
        if hero.hp > 0 :
            print(f"\nYour hp is {hero.hp}")
        else:
            return hero.hp <= 0
            
                   
    
class HeroArena:
    def __init__(self):
        self.hero = Hero()
        self.enemy = Enemy()
    
    def run(self):
            self.hero.hero_class()
            self.enemy.enemy_class()
            self.hero.show_status() 
            self.enemy.show_status()
            
            while self.hero.hp > 0 and self.enemy.hp > 0:

                if self.hero.attack(self.enemy) :
                    print("\nYour enemy is dead\n"
                            "🏆 Hero Wins!"
                            "\nThe game finish") 
                    break
                elif self.enemy.attack(self.hero):
                    print("\nYour are dead\n"
                            "💀 Enemy Wins!"
                            "\nThe game finish") 
                    break
                
                        
c = HeroArena()
c.run()  


