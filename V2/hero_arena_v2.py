import random

class Character():
    classes = {
                            1: {
                                "class": "Bandit",
                                "hp": 50,
                                "damage": 50},

                            2: {
                                "class": "Samurai",
                                "hp": 30,
                                "damage": 70
                            },

                            3: {
                                "class": "Knight",
                                "hp": 80,
                                "damage": 20
                            }
                        }
    def __init__(self):
        self.name = ""
        self.class_character = ""
        self.hp = 0
        self.damage = 0
    
    def character_class(self , number):
        data = self.classes[number]
        self.class_character = data["class"]
        self.hp = data["hp"]
        self.damage = data["damage"]    
        
    def attack(self, target):
        target.hp -= self.damage
        if target.hp > 0 :
            print(f"{target.name} HP: {target.hp}")
        else:
            return target.hp <= 0    
    
    def show_status(self):
        print(f"\nName: {self.name}\n"
              f"Class: {self.class_character}\n"
              f"HP: {self.hp}\n"
              f"Damage: {self.damage}\n") 
              
class Hero(Character):
    
    def hero_class(self):
        self.name = input("Enter your character name: ")
        while True:
            try:
                choose_class = int(input("\nChoose your hero class:\n"
                                    "1)Bandit\n"
                                    "2)Samurai\n"
                                    "3)Knight (1,2,3): Please enter number: "))
                if choose_class not in range(1,4):
                    print("Enter a valid number")
                    continue
                return choose_class    
            except ValueError:
                print("Enter a number please!!!\nTry again")
                continue                
                
class Enemy(Character):
    
    def enemy_class(self):
        choose_class = random.randint(1,3)
        enemy_names = {
                        1: 'Billy the Kid',
                        2: 'Miyamoto Musashi',
                        3: 'Sir Thomas More'
                      }
        self.name = enemy_names[choose_class]
        return choose_class

class HeroArena:
    def __init__(self):
        self.hero = Hero()
        self.enemy = Enemy()
    
        
    
    def run(self):
            self.hero.character_class(self.hero.hero_class())
            self.enemy.character_class(self.enemy.enemy_class())
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
                            "\nThe game has finished") 
                    break            

c = HeroArena()
c.run()                 