import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os
import itertools
import random

# Загрузка данных из CSV
def load_data(csv_file):
    data = []
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'id': int(row['id']),
                'name': row['name'],
                'price': float(row['price']),
                'rating': int(row['rating']),
                'path': row['path']
            })
    return data

# Сохранение данных в CSV
def save_data(csv_file, data):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'price', 'rating', 'path']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

# Основной класс игры
class CoinComparisonGame:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.pairs = list(itertools.combinations(range(len(data)), 2))  # Все возможные пары
        random.shuffle(self.pairs)  # Перемешиваем пары
        self.current_pair_index = 0

        # Настройка интерфейса
        self.root.title("Выбери лучшую монету")
        self.root.geometry("600x400")

        # Заголовок
        self.label = tk.Label(root, text="Выбери лучшую монету:", font=("Arial", 16))
        self.label.pack(pady=10)

        # Фрейм для карточек
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Карточки (изображения монет)
        self.coin1_image = None
        self.coin2_image = None
        self.coin1_label = tk.Label(self.frame)
        self.coin1_label.pack(side=tk.LEFT, padx=20)
        self.coin2_label = tk.Label(self.frame)
        self.coin2_label.pack(side=tk.LEFT, padx=20)

        # Кнопки выбора
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.coin1_button = tk.Button(self.button_frame, text="Выбрать", command=lambda: self.choose_coin(0))
        self.coin1_button.pack(side=tk.LEFT, padx=20)

        self.coin2_button = tk.Button(self.button_frame, text="Выбрать", command=lambda: self.choose_coin(1))
        self.coin2_button.pack(side=tk.LEFT, padx=20)

        # Загрузка первой пары
        self.load_pair()

    # Загрузка пары монет
    def load_pair(self):
        if self.current_pair_index >= len(self.pairs):
            self.end_game()
            return

        pair = self.pairs[self.current_pair_index]
        coin1 = self.data[pair[0]]
        coin2 = self.data[pair[1]]

        # Загрузка изображений
        self.load_image(self.coin1_label, coin1['path'])
        self.load_image(self.coin2_label, coin2['path'])

        # Обновление текста кнопок
        self.coin1_button.config(text=f"Выбрать {coin1['name']}")
        self.coin2_button.config(text=f"Выбрать {coin2['name']}")

    # Загрузка изображения
    def load_image(self, label, path):
        if not os.path.exists(path):
            print(f"Файл не найден: {path}")
            return

        image = Image.open(path)
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Сохраняем ссылку, чтобы изображение не удалялось сборщиком мусора

    # Выбор монеты
    def choose_coin(self, choice):
        pair = self.pairs[self.current_pair_index]
        selected_coin_index = pair[choice]
        self.data[selected_coin_index]['rating'] += 1  # Увеличиваем рейтинг выбранной монеты

        # Переход к следующей паре
        self.current_pair_index += 1
        if self.current_pair_index < len(self.pairs):
            self.load_pair()
        else:
            self.end_game()

    # Завершение игры
    def end_game(self):
        save_data('coins.csv', self.data)  # Сохраняем результаты
        messagebox.showinfo("Игра завершена", "Вы молодец — проголосовали за все существующие токены!")
        self.root.quit()

# Запуск игры
if __name__ == "__main__":
    # Загрузка данных
    data = load_data('coins.csv')

    # Создание окна Tkinter
    root = tk.Tk()
    game = CoinComparisonGame(root, data)
    root.mainloop()