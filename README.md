# Hero Arena 🏆

A simple text-based RPG battle game built with Python and Object-Oriented Programming (OOP).

Hero Arena is a learning project that evolves through multiple versions, with each version introducing new programming concepts, mechanics, and improvements.

---

## 🎮 Current Version

**V3.0**

---

## 📌 Features

### V1

* Choose your hero name
* Choose between 3 hero classes:

  * Bandit
  * Samurai
  * Knight
* Each class has different HP and Damage
* Random enemy class selection
* Turn-based combat
* Hero and enemy status display
* Win/Lose conditions

### V2 — OOP Refactor

V2 focuses mainly on improving the code structure and applying better Object-Oriented Programming concepts.

#### Improvements over V1:

* Added a base `Character` class
* `Hero` and `Enemy` now inherit from `Character`
* Removed duplicated code between `Hero` and `Enemy`
* Centralized class statistics using a dictionary
* Separated class selection from character setup
* Added `try/except` input validation
* Improved enemy name selection using a dictionary
* Made `attack()` reusable with a generic `target`
* Made `show_status()` reusable for both Hero and Enemy
* Improved code organization and maintainability

### V3 — Item & Combat System

V3 introduces a more advanced item and combat system, making the game more modular and expandable.

#### Improvements over V2:

* Added a **Weapon system** with different weapons and damage values
* Added a **Potion system** that can restore HP and increase weapon damage
* Added an **Inventory system** for managing items
* Added the ability to **use potions** from the inventory
* Added **weapon selection** for the Hero
* Added **random weapon and potion generation** for enemies
* Added an **item looting system** when an enemy is defeated
* Changed the combat system so character damage is determined by their **equipped weapon**
* Added an `is_dead()` method to handle death and game-ending conditions
* Improved OOP design by separating responsibilities into `Character`, `Weapon`, `Potion`, and `Inventory` classes
* Used **composition** by giving each character their own inventory
* Improved code reusability and maintainability
* Made the game structure more **modular and scalable**, allowing new weapons, potions, and items to be added more easily

#### V2 → V3

**V2:**

Characters had fixed damage values and a basic combat system.

**V3:**

Characters can now equip weapons, use potions, manage inventories, and loot items from defeated enemies, creating a more complete and flexible combat system.

---

## 🧠 OOP Concepts Used

* Classes and Objects
* Inheritance
* Composition
* Code Reusability
* Encapsulation
* Dictionaries
* Exception Handling
* Methods
* Object Interaction
* Separation of Responsibilities

---

## ⚔️ Character Classes

| Class   | HP | Damage |
| ------- | -: | -----: |
| Bandit  | 50 |     50 |
| Samurai | 30 |     70 |
| Knight  | 80 |     20 |

> In V3, character damage is primarily determined by the equipped weapon rather than only by the character class.

---

## 📂 Project Structure

```text
Hero Arena/
│
├── V1/
│   └── hero_arena_v1.py
│
├── V2/
│   └── hero_arena_v2.py
│
├── V3/
│   └── hero_arena_v3.py
│
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

Make sure Python is installed, then run the latest version:

```bash
python V3/hero_arena_v3.py
```

---

## 🚀 Version History

### V1.0

The first playable version of Hero Arena, featuring basic hero creation, enemy generation, and turn-based combat.

### V2.0

A major OOP refactor focused on inheritance, code reuse, cleaner class design, input validation, and better maintainability.

### V3.0

Introduced a complete item and inventory system with weapons, potions, looting, weapon-based damage, and a more modular combat system.

---

## 🔮 Future Versions

Future versions will introduce more gameplay mechanics and continue improving the project's architecture, such as:

* More weapons
* More potions and item types
* More advanced combat mechanics
* More character classes
* Better enemy AI
* Improved game flow
* Additional OOP concepts
* Further code refactoring
* Save/Load system
* More advanced game architecture

---

> This project is being developed step by step as a practical Python and OOP learning project.
