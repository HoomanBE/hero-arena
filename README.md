# Hero Arena 🏆

A simple text-based RPG battle game built with Python and Object-Oriented Programming (OOP).

Hero Arena is a learning project that evolves through multiple versions, with each version introducing new programming concepts, mechanics, and improvements.

---

## 🎮 Current Version

**V2.0**

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

---

## 🧠 OOP Concepts Used

* Classes and Objects
* Inheritance
* Code Reusability
* Encapsulation
* Dictionaries
* Exception Handling
* Methods
* Object Interaction

---

## ⚔️ Character Classes

| Class   | HP | Damage |
| ------- | -: | -----: |
| Bandit  | 50 |     50 |
| Samurai | 30 |     70 |
| Knight  | 80 |     20 |

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
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python V2/hero_arena_v2.py
```

---

## 🚀 Version History

### V1.0

The first playable version of Hero Arena, featuring basic hero creation, enemy generation, and turn-based combat.

### V2.0

A major OOP refactor focused on inheritance, code reuse, cleaner class design, input validation, and better maintainability.

---

## 🔮 Future Versions

Future versions will introduce more gameplay mechanics and continue improving the project's architecture, such as:

* Weapons
* Potions
* Inventory system
* More advanced combat
* More character classes
* Better game flow
* Additional OOP concepts
* Further code refactoring

---

> This project is being developed step by step as a practical Python and OOP learning project.
