# character.py

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import json  # Добавлен импорт модуля json

class Character:
    def __init__(self, name, age, gender, balance=30000):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
        self.health = 100
        self.hunger = 100
        self.energy = 100
        self.portfolio = {"Bitcoin": 0.0, "Ethereum": 0.0}
        self.market_prices = {"Bitcoin": 40000, "Ethereum": 1500}

    def save_to_file(self):
        with open("character.json", "w") as file:
            json.dump(self.__dict__, file)  # Теперь json определен

    def load_from_file(self):
        with open("character.json", "r") as file:
            data = json.load(file)
            self.__dict__.update(data)