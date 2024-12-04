import tkinter as tk

def create_table(rows, columns):
    for i in range(rows):
        for j in range(columns):
            cell = tk.Frame(root, width=100, height=30, borderwidth=5, relief="solid", bg="white")
            cell.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(cell, text=f"Cell {i+1},{j+1}", bg="white")
            label.pack(expand=True)

# Создание основного окна
root = tk.Tk()
root.title("Таблица с ячейками")

# Создание таблицы
create_table(8, 6)

# Центрирование окна
root.update_idletasks()  # Обновить размеры виджетов
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Рассчитываем новое положение окна
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# Устанавливаем новое положение окна
root.geometry(f'{width}x{height}+{x}+{y}')

# Запуск основного цикла приложения
root.mainloop()