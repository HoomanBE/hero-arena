import random

class Character():
    classes = {
                            1: {
                                "class": "Bandit",
                                "hp": 50,
                            },

                            2: {
                                "class": "Samurai",
                                "hp": 30,
                            },

                            3: {
                                "class": "Knight",
                                "hp": 80,
                            }
                        }
    def __init__(self):
        self.name = ""
        self.class_character = ""
        self.hp = 0
        self.weapon = None
        self.inventory = Inventory()
        
    def character_class(self , number):
        data = self.classes[number]
        self.class_character = data["class"]
        self.hp = data["hp"]     
        
    def attack(self, target):
        target.hp -= self.weapon.damage
        print(f"{target.name} get damage by the {self.weapon.name}\n")
            
    def is_dead(self):
        
        if self.hp <= 0 :
            print(f"The {self.name} has died\n")
            return "The game is ended"
        else:
            print(f'The {self.name} has {self.hp} hp')
                
    def show_status(self):
        
        print(f"\nName: {self.name}\n"
              f"Class: {self.class_character}\n"
              f"HP: {self.hp}\n"
              f"Damage: {self.weapon.damage}\n"                            
              f"Inventory:" , end=" ")
        self.inventory.show_items() 
        
        
class Potion:
    
    def __init__(self, name, hp, power_weapon):
        self.name = name
        self.hp = hp
        self.power_weapon = power_weapon
                   

class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):

        if not self.items:
            print("Inventory is Empty")
            return

        for i, item in enumerate(self.items, start=1):
            print(f"{i}) {item.name} | HP +{item.hp} | Power +{item.power_weapon}")

    def use_potion(self, index):

        return self.items.pop(index)
            
             
class Weapon:
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
         
class Hero(Character):

    def __init__(self):
        super().__init__()
    
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
            
    def hero_weapon(self):
        while True:
            try:
                choose_weapon = int(input("\nChoose your hero wepon:\n"
                                    "1)The Rivers of Blood \n"
                                    "2)Moghwyn's Sacred Spear\n"
                                    "3)Bolt of Gransax (1,2,3): Please enter number: "))
                if choose_weapon not in range(1,4):
                    print("Enter a valid number")
                    continue
                return choose_weapon    
                 
            except ValueError:
                print("Enter a number please!!!\nTry again")
                continue
            
    def hero_potion(self):

        self.inventory.show_items()

        while True:

            try:
                choose = int(input("Choose potion number: "))

                if choose < 1 or choose > len(self.inventory.items):
                    print("Invalid choice")
                    continue

                potion = self.inventory.use_potion(choose-1)

                self.hp += potion.hp
                self.weapon.damage += potion.power_weapon

                print(f"\nYou used {potion.name}")
                print(f"+{potion.hp} HP")
                print(f"+{potion.power_weapon} Weapon Damage")

                break

            except ValueError:
                print("Invalid choice") 
        
                
class Enemy(Character):
    
    def __init__(self):
            super().__init__()
            
            
    def enemy_class(self):
        choose_class = random.randint(1,3)
        enemy_names = {
                        1: 'Billy the Kid',
                        2: 'Miyamoto Musashi',
                        3: 'Sir Thomas More'
                      }
        self.name = enemy_names[choose_class]
        return choose_class
    
    def enemy_weapon(self):
        choose_weapon = random.randint(1,3)
        return choose_weapon
    
    def enemy_potion(self):
        choose_potion = random.randint(1,3)
        return choose_potion
    
    
class HeroArena:
    weapons = {
                1: ("The Rivers of Blood", 20),
                2: ("Moghwyn's Sacred Spear", 10),
                3: ("Bolt of Gransax", 30)
                
            }
    potions = {
                1: ("Swallow", 50 , 10),
                2: ("Shrike", 30 , 20),
                3: ("Blizzard", 20 , 40),
            }
    
    def __init__(self):
        self.hero = Hero()
        self.enemy = Enemy()
        
    
    def create_weapon(self , value):
        name, damage = self.weapons[value]
        return  Weapon(name, damage)
    
    def create_potion(self, value):
        name , hp , power_weapon = self.potions[value]
        return Potion(name , hp , power_weapon) 
                
                
    def run(self):
            self.hero.character_class(self.hero.hero_class())
            self.hero.weapon = self.create_weapon(self.hero.hero_weapon())
            self.hero.show_status() 
            self.enemy.character_class(self.enemy.enemy_class())
            self.enemy.weapon = self.create_weapon(self.enemy.enemy_weapon())
            enemy_potion = self.create_potion(self.enemy.enemy_potion())
            self.enemy.inventory.add_item(enemy_potion)
            self.enemy.show_status()
            
            
            while self.hero.hp > 0 and self.enemy.hp > 0:
                self.hero.attack(self.enemy)
                if self.enemy.is_dead():
                    for item in self.enemy.inventory.items:
                        self.hero.inventory.add_item(item)
                        print(f"Your enemy has dropped {item.name} and you loot that!")
                    print("\nYour enemy is dead\n"
                            "🏆 Hero Wins!"
                            "\nThe game finish")
                    while True:
                        answer = input("Use potion? (y/n): ")
                        if answer.lower() == "y":
                            self.hero.hero_potion()
                            print("\nQuitting the game....")
                            break
                        elif answer.lower() == "n":
                            print("\nQuitting the game....")
                            break
                        else:
                            print("Invalid input! Try again")    

                    break 
                
                self.enemy.attack(self.hero)
                if self.hero.is_dead():
                    print("\nYour are dead\n"
                            "💀 Enemy Wins!"
                            "\nThe game has finished") 
                    break
                              

c = HeroArena()
c.run()                 
