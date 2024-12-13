# character.py

import json

class Character:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.health = 100
        self.hunger = 100
        self.energy = 100

    def save_to_file(self, filename="dataBase.json"):
        data = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "health": self.health,
            "hunger": self.hunger,
            "energy": self.energy
        }
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)