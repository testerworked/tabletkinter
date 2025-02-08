import tkinter as tk
from tkinter import messagebox
import subprocess

def new_game():
    messagebox.showinfo("New Game", "Starting a new game...")
    script_to_run = 'game_0.py'
    try:
        subprocess.run(['python', script_to_run], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error occurred while running the script: {e}')

def continue_playing():
    messagebox.showinfo("Continue Playing", "Continuing the last game...")

def screenshots():
    messagebox.showinfo("Screenshots", "Here you can view screenshots...")

def select_language():
    messagebox.showinfo("Select Language", "Selecting language...")

def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()

# Создаем главное окно
root = tk.Tk()
root.title("Game Menu")
# Получаем ширину и высоту экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Устанавливаем размеры окна
window_width = 300
window_height = 400

# Вычисляем позицию окна для центрирования
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Создаем фрейм для размещения кнопок
frame = tk.Frame(root)
frame.pack(expand=True)

# Создаем кнопки и добавляем их на фрейм
btn_new_game = tk.Button(frame, text="New Game", command=new_game)
btn_new_game.pack(pady=10)

btn_continue_playing = tk.Button(frame, text="Continue Playing", command=continue_playing)
btn_continue_playing.pack(pady=10)

btn_screenshots = tk.Button(frame, text="Screenshots", command=screenshots)
btn_screenshots.pack(pady=10)

btn_select_language = tk.Button(frame, text="Select Language", command=select_language)
btn_select_language.pack(pady=10)

btn_exit = tk.Button(frame, text="Exit", command=exit_game)
btn_exit.pack(pady=10)

# Запускаем главный цикл
root.mainloop()