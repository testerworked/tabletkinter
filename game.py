import tkinter as tk
from tkinter import ttk
from datetime import datetime
from character import Character

# Функции для открытия окон
def open_portfolio_window():
    portfolio_window = tk.Toplevel(root)
    portfolio_window.title("Портфель")
    label = tk.Label(portfolio_window, text="Это окно портфель", padx=20, pady=20)
    label.pack()
    center_window(portfolio_window)

def open_trading_window():
    trading_window = tk.Toplevel(root)
    trading_window.title("Торговля")
    label = tk.Label(trading_window, text="Это окно торговли", padx=20, pady=20)
    label.pack()
    center_window(trading_window)

def open_reports_window():
    reports_window = tk.Toplevel(root)
    reports_window.title("Отчеты")
    label = tk.Label(reports_window, text="Это окно отчеты", padx=20, pady=20)
    label.pack()
    center_window(reports_window)

def center_window(window):
    window.update_idletasks() 
    width = window.winfo_width() if window.winfo_width() > 0 else 500  # Заполняем ширину
    height = window.winfo_height() if window.winfo_height() > 0 else 300  # Заполняем высоту
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

class CryptoInvestorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Симулятор жизни криптоинвестора")
        self.character = None
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.master)
        self.welcome_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=5)
        self.welcome_frame.configure(width=500, height=300)

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
        self.character = Character(name, age, gender)
        self.character.save_to_file()
        
        self.welcome_frame.grid_forget()
        self.create_game_screen()

    def create_game_screen(self):
        self.game_frame = tk.Frame(self.master)
        self.game_frame.grid(row=0, column=0)

        self.indicators_frame = tk.Frame(self.master)
        self.indicators_frame.grid(row=0, column=1, padx=20)

        self.status_label = tk.Label(self.indicators_frame, text="")
        self.status_label.pack(pady=10)

        # Создаем таблицу
        self.create_table(8, 8)

    def create_table(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                cell = tk.Frame(root, width=80, height=30, borderwidth=5, relief="solid", bg="white")
                cell.grid(row=i, column=j, padx=5, pady=5)

                if i == 0 and j == 0:  # Портфель
                    button_portfolio = tk.Button(cell, text="Портфель", bg="lightblue", command=open_portfolio_window)
                    button_portfolio.pack(expand=True)
                elif i == 0 and j == 1:  # Торговля
                    button_trading = tk.Button(cell, text="Торговля", bg="lightgreen", command=open_trading_window)
                    button_trading.pack(expand=True)
                elif i == 0 and j == 2:  # Отчеты
                    button_reports = tk.Button(cell, text="Отчеты", bg="lightyellow", command=open_reports_window)
                    button_reports.pack(expand=True)
                elif i == 0 and j == 3:  # Анализ
                    button_analysis = tk.Button(cell, text="Анализ", bg="lightgray", command=lambda: print("Анализ"))
                    button_analysis.pack(expand=True)
                elif i == 0 and j == 4:  # Курсы монет
                    button_currency_rates = tk.Button(cell, text="Курсы монет", bg="lightgray", command=lambda: print("Курсы монет"))
                    button_currency_rates.pack(expand=True)
                elif i == 0 and j == 7:  # Время в ячейке (1,8)
                    self.time_label = tk.Label(cell, text="", font=("Arial", 15))
                    self.time_label.pack(expand=True)
                    self.update_time()  # Начинаем обновление времени в этом месте
                elif i == 7 and j == 7:  # Имя, возраст и пол в ячейке (8,8)
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
                else:
                    label = tk.Label(cell, text=f"Cell {i + 1},{j + 1}", bg="white")
                    label.pack(expand=True)

        self.update_bars()  # Начинаем обновление индикаторов

    def update_bars(self):
        if self.character:
            self.health_bar['value'] = self.character.health
            self.hunger_bar['value'] = self.character.hunger
            self.energy_bar['value'] = self.character.energy
            
            # Уменьшаем показатели со временем
            self.character.health -= 0.1
            self.character.hunger -= 0.2
            self.character.energy -= 0.15
            
            # Убедимся, что значения не становятся отрицательными
            self.character.health = max(0, self.character.health)
            self.character.hunger = max(0, self.character.hunger)
            self.character.energy = max(0, self.character.energy)

        self.master.after(1000, self.update_bars)  # Обновляем каждые 1000 мс

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

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
    root.geometry(f'1000x500+{x}+{y}')  # Задаем фиксированные размеры для главного окна
    game = CryptoInvestorGame(root)
    root.mainloop()