import tkinter as tk
from tkinter import ttk
from datetime import datetime
from character import Character
from tkinter import messagebox, scrolledtext
import pandas as pd
import json
import random
from tkinter import ttk, messagebox
from datetime import datetime
import random
import subprocess 

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
            json.dump(self.__dict__, file)

    def load_from_file(self):
        with open("character.json", "r") as file:
            data = json.load(file)
            self.__dict__.update(data)

class CryptoInvestorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Симулятор жизни криптоинвестора")
        self.character = None
        self.step_count = 0
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.master)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=5)

        tk.Label(self.welcome_frame, text="Введите ваше имя:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.welcome_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.welcome_frame, text="Введите ваш возраст:").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.welcome_frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.welcome_frame, text="Выберите пол:").grid(row=2, column=0)
        self.gender_var = tk.StringVar(value="Мужской")
        tk.Radiobutton(self.welcome_frame, text='Мужской', variable=self.gender_var, value='Мужской').grid(row=2, column=1)
        tk.Radiobutton(self.welcome_frame, text='Женский', variable=self.gender_var, value='Женский').grid(row=2, column=2)

        tk.Button(self.welcome_frame, text="Войти", command=self.start_game).grid(row=3, column=0, columnspan=3)

    def start_game(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        self.character = Character(name, age, gender, balance=30000)
        self.character.save_to_file()
        
        self.welcome_frame.grid_forget()
        self.create_game_screen()
        self.next_step()  # Начинаем первый шаг

    def create_game_screen(self):
        self.game_frame = tk.Frame(self.master)
        self.game_frame.grid(row=0, column=0)

        self.indicators_frame = tk.Frame(self.master)
        self.indicators_frame.grid(row=0, column=1, padx=20)

        self.create_table(8, 8)
        self.status_label = tk.Label(self.master, text="", borderwidth=2, relief="groove", width=40, height=4)
        self.status_label.grid(row=4, column=4, padx=5, pady=5)

        self.update_bars()

    def create_table(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                cell = tk.Frame(self.master, width=80, height=30, borderwidth=5, relief="solid", bg="white")
                cell.grid(row=i, column=j, padx=5, pady=5)

                if i == 0 and j == 0:  # Портфель
                    button_portfolio = tk.Button(cell, text="Портфель", bg="lightblue", command=self.open_portfolio_window)
                    button_portfolio.pack(expand=True)
                elif i == 0 and j == 1:  # Торговля
                    button_trading = tk.Button(cell, text="Торговля", bg="lightgreen", command=self.open_trading_window)
                    button_trading.pack(expand=True)
                elif i == 0 and j == 2:  # Отчеты
                    button_reports = tk.Button(cell, text="Отчеты", bg="lightyellow", command=self.open_reports_window)
                    button_reports.pack(expand=True)
                elif i == 0 and j == 7:
                    self.time_label = tk.Label(cell, text="", font=("Arial", 15))
                    self.time_label.pack(expand=True)
                    self.update_time()
                elif i == 1 and j == 0:  # New Button to Run game_coin.py
                    run_game_button = tk.Button(cell, text="Запустить Game", command=self.run_game_coin)
                    run_game_button.pack(expand=True)
                elif i == 1 and j == 7:  # Кнопка выхода
                    exit_button = tk.Button(self.master, text="Выход", command=self.master.quit)
                    exit_button.grid(row=1, column=7, padx=5, pady=5)
                elif i == 7 and j == 7:  # Имя, возраст и пол
                    self.name_label = tk.Label(cell, text=f"Имя: {self.character.name}")
                    self.age_label = tk.Label(cell, text=f"Возраст: {self.character.age}")
                    self.gender_label = tk.Label(cell, text=f"Пол: {self.character.gender}")
                    self.name_label.pack(expand=True)
                    self.age_label.pack(expand=True)
                    self.gender_label.pack(expand=True)
                elif i == 7 and j == 1:  # Здоровье
                    tk.Label(cell, text="Здоровье:").pack()
                    self.health_bar = ttk.Progressbar(cell, length=200, mode='determinate')
                    self.health_bar['value'] = self.character.health
                    self.health_bar.pack()
                elif i == 7 and j == 2:  # Сытость
                    tk.Label(cell, text="Сытость:").pack()
                    self.hunger_bar = ttk.Progressbar(cell, length=200, mode='determinate')
                    self.hunger_bar['value'] = self.character.hunger
                    self.hunger_bar.pack()
                elif i == 7 and j == 3:  # Энергия
                    tk.Label(cell, text="Энергия:").pack()
                    self.energy_bar = ttk.Progressbar(cell, length=200, mode='determinate')
                    self.energy_bar['value'] = self.character.energy
                    self.energy_bar.pack()
                elif i == 0 and j == 6:  # Баланс
                    self.balance_label = tk.Label(cell, text=f"Баланс: {self.character.balance:.2f} USDT")
                    self.balance_label.pack(expand=True)
                else:
                    label = tk.Label(cell, text=f"Cell {i + 1},{j + 1}", bg="white")
                    label.pack(expand=True)

        self.create_buttons()

    def create_buttons(self):
        tk.Button(self.master, text="Изучить", command=self.study_activity).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Читать новости", command=self.read_news).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Покушать хорошо!", command=self.buy_food).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Арендовать сервер для стейкинга", command=self.buy_computer).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Изучить книгу\nоб инвестициях", command=self.study_investment_book).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.master, text="Поспать", command=self.sleep).grid(row=6, column=1, padx=5, pady=5)

    def run_game_coin(self):
        try:
            # This will run the game_coin.py script using the Python interpreter
            subprocess.Popen(["python", "game_coin.py"])
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось запустить игру: {e}")

    def open_portfolio_window(self):
        portfolio_window = tk.Toplevel(self.master)
        portfolio_window.title("Портфель")
        label = tk.Label(portfolio_window, text="Монеты в Вашем Портфеле", padx=20, pady=20)
        label.pack()

        for coin, amount in self.character.portfolio.items():
            tk.Label(portfolio_window, text=f"{coin}: {amount}").pack()

        center_window(portfolio_window)

    def open_reports_window(self):
        reports_window = tk.Toplevel(self.master)
        reports_window.title("Отчеты")
        label = tk.Label(reports_window, text="Изучите последние отчеты по Вашему портфелю", padx=20, pady=20)
        label.pack()

        # Пример отображения отчета
        report_text = f"Текущий баланс: {self.character.balance:.2f} USDT\n"
        report_text += f"Стоимость портфеля: {sum(amount * self.character.market_prices[coin] for coin, amount in self.character.portfolio.items()):.2f} USDT\n"
        report_text += f"Здоровье: {self.character.health:.1f}%\n"
        report_text += f"Сытость: {self.character.hunger:.1f}%\n"
        report_text += f"Энергия: {self.character.energy:.1f}%"

        report_label = tk.Label(reports_window, text=report_text, justify=tk.LEFT)
        report_label.pack(padx=20, pady=20)

        center_window(reports_window)

    def open_trading_window(self):
        trading_window = tk.Toplevel(self.master)
        trading_window.title("Торговля")

        label = tk.Label(trading_window, text="Настало время торговли...", padx=20, pady=20)
        label.pack()

        start_button = tk.Button(trading_window, text="Начать торговлю", command=self.start_trading)
        start_button.pack(pady=10)

        end_button = tk.Button(trading_window, text="Завершить торговлю", command=self.end_trading)
        end_button.pack(pady=10)

        center_window(trading_window)

    def start_trading(self):
        self.status_label.config(text="Торговля началась! Анализируем рынок...")

    def end_trading(self):
        result = random.choice(["success", "failure"])
        amount = random.randint(1, 1000)

        if result == "success":
            self.character.balance += amount
            message = f"Торговля прошла успешно! Вы заработали {amount}. Новый баланс: {self.character.balance:.2f} USDT."
        else:
            self.character.balance -= amount
            message = f"Торговля прошла не успешно. Вы потеряли {amount}. Новый баланс: {self.character.balance:.2f} USDT."

        messagebox.showinfo("Результат торговли", message)
        self.status_label.config(text="Торговля завершена.")
        self.balance_label.config(text=f"Баланс: {self.character.balance:.2f} USDT")
        self.character.save_to_file()

    def next_step(self):
        self.step_count += 1
        self.update_market()
        self.update_portfolio()
        self.life_event()
        self.update_bars()

        # Вознаграждение за завершение шага
        reward = random.randint(100, 1000)
        self.character.balance += reward
        self.status_label.config(text=f"Шаг {self.step_count} завершен! Вы получили {reward} USDT в качестве вознаграждения.")
        self.balance_label.config(text=f"Баланс: {self.character.balance:.2f} USDT")

        # Планируем следующий шаг через 5 секунд (имитация времени)
        self.master.after(5000, self.next_step)

    def update_market(self):
        for coin in self.character.market_prices:
            change = random.uniform(-0.05, 0.05)  # Случайное изменение цены на ±5%
            self.character.market_prices[coin] *= (1 + change)

    def update_portfolio(self):
        total_value = 0
        for coin, amount in self.character.portfolio.items():
            total_value += amount * self.character.market_prices[coin]
        self.status_label.config(text=f"Стоимость портфеля: {total_value:.2f} USDT")

    def life_event(self):
        events = [
            {"description": "Вы получили премию на работе: +$2,000.", "effect": 2000},
            {"description": "Вы заболели и потратили $1,000 на лечение.", "effect": -1000}
        ]
        event = random.choice(events)
        self.character.balance += event['effect']
        self.status_label.config(text=event['description'])

    def update_bars(self):
        if self.character:
            self.health_bar['value'] = self.character.health
            self.hunger_bar['value'] = self.character.hunger
            self.energy_bar['value'] = self.character.energy

            if self.character.hunger > 0:
                self.character.hunger -= 0.2
            if self.character.energy > 0:
                self.character.energy -= 0.15

            self.character.hunger = max(0, self.character.hunger)
            self.character.energy = max(0, self.character.energy)

            if self.character.hunger == 0 or self.character.energy == 0:
                self.character.health -= 0.1

            self.character.health = max(0, self.character.health)

            if self.character.hunger == 0 and self.character.energy == 0:
                self.status_label.config(text="Ваш персонаж голоден и устал, здоровье уменьшается.")
            elif self.character.hunger == 0:
                self.status_label.config(text="Ваш персонаж голоден, здоровье уменьшается.")
            elif self.character.energy == 0:
                self.status_label.config(text="Ваш персонаж устал, здоровье уменьшается.")
            else:
                self.status_label.config(text="Ваш персонаж в норме.")

        self.master.after(1000, self.update_bars)

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

    def study_activity(self):
        self.status_label.config(text="Вы изучаете новый материал...")

    def read_news(self):
        self.status_label.config(text="Вы читаете новости о криптовалюте...")

    def buy_food(self):
        if self.character.balance >= 100:
            self.character.balance -= 100
            self.character.hunger += 20
            self.status_label.config(text="Вы купили еду!")
            self.balance_label.config(text=f"Баланс: {self.character.balance:.2f} USDT")
        else:
            self.status_label.config(text="Недостаточно средств для покупки еды.")

    def buy_computer(self):
        if self.character.balance >= 1500:
            self.character.balance -= 1500
            self.status_label.config(text="Вы купили компьютер!")
            self.balance_label.config(text=f"Баланс: {self.character.balance:.2f} USDT")
        else:
            self.status_label.config(text="Недостаточно средств для покупки компьютера.")

    def study_investment_book(self):
        self.status_label.config(text="Вы изучаете книгу об инвестициях...")

    def sleep(self):
        self.character.energy += 30
        self.status_label.config(text="Вы поспали и восстановили энергию.")
        if self.character.energy > 100:
            self.character.energy = 100

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Симулятор жизни криптоинвестора")
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'1000x500+{x}+{y}')  
    game = CryptoInvestorGame(root)
    root.mainloop()