import tkinter as tk
from tkinter import messagebox
import random

balance = 1000
bitcoin_price = 300
ethereum_price = 100
bitcoin_amount = 0
ethereum_amount = 0


def update_prices():
    global bitcoin_price, ethereum_price
    bitcoin_price += random.randint(-50, 50)
    ethereum_price += random.randint(-20, 20)
    if bitcoin_price < 0:
        bitcoin_price = 0
    if ethereum_price < 0:
        ethereum_price = 0
    price_label.config(text=f"Bitcoin: ${bitcoin_price}\nEthereum: ${ethereum_price}")
    root.after(60000, update_prices)

def buy_bitcoin():
    global balance, bitcoin_amount
    amount = float(bitcoin_entry.get())
    cost = amount * bitcoin_price
    if balance >= cost:
        balance -= cost
        bitcoin_amount += amount
        update_balance()
    else:
        messagebox.showinfo("Ошибка", "Недостаточно средств!")

def sell_bitcoin():
    global balance, bitcoin_amount
    amount = float(bitcoin_entry.get())
    if bitcoin_amount >= amount:
        balance += amount * bitcoin_price
        bitcoin_amount -= amount
        update_balance()
    else:
        messagebox.showinfo("Ошибка", "У вас недостаточно Bitcoin!")

def buy_ethereum():
    global balance, ethereum_amount
    amount = float(ethereum_entry.get())
    cost = amount * ethereum_price
    if balance >= cost:
        balance -= cost
        ethereum_amount += amount
        update_balance()
    else:
        messagebox.showinfo("Ошибка", "Недостаточно средств!")

def sell_ethereum():
    global balance, ethereum_amount
    amount = float(ethereum_entry.get())
    if ethereum_amount >= amount:
        balance += amount * ethereum_price
        ethereum_amount -= amount
        update_balance()
    else:
        messagebox.showinfo("Ошибка", "У вас недостаточно Ethereum!")

def update_balance():
    balance_label.config(text=f"Баланс: ${balance:.2f}")
    portfolio_label.config(text=f"Bitcoin: {bitcoin_amount:.2f}\nEthereum: {ethereum_amount:.2f}")

def check_win():
    if balance >= 10000:
        messagebox.showinfo("Победа!", "Вы заработали $10,000! Уровень пройден!")
        root.quit()

root = tk.Tk()
root.title("Crypto Tycoon Simulator - Уровень 1")
root.geometry("400x400")

# Элементы интерфейса
price_label = tk.Label(root, text=f"Bitcoin: ${bitcoin_price}\nEthereum: ${ethereum_price}", font=("Arial", 14))
price_label.pack(pady=10)

balance_label = tk.Label(root, text=f"Баланс: ${balance:.2f}", font=("Arial", 14))
balance_label.pack(pady=10)

portfolio_label = tk.Label(root, text=f"Bitcoin: {bitcoin_amount:.2f}\nEthereum: {ethereum_amount:.2f}", font=("Arial", 14))
portfolio_label.pack(pady=10)


bitcoin_entry = tk.Entry(root)
bitcoin_entry.insert(0, "0.1")
bitcoin_entry.pack(pady=5)

ethereum_entry = tk.Entry(root)
ethereum_entry.insert(0, "0.1")
ethereum_entry.pack(pady=5)


buy_bitcoin_button = tk.Button(root, text="Купить Bitcoin", command=buy_bitcoin)
buy_bitcoin_button.pack(pady=5)

sell_bitcoin_button = tk.Button(root, text="Продать Bitcoin", command=sell_bitcoin)
sell_bitcoin_button.pack(pady=5)

buy_ethereum_button = tk.Button(root, text="Купить Ethereum", command=buy_ethereum)
buy_ethereum_button.pack(pady=5)

sell_ethereum_button = tk.Button(root, text="Продать Ethereum", command=sell_ethereum)
sell_ethereum_button.pack(pady=5)


update_prices()

root.after(1000, check_win)

root.mainloop()