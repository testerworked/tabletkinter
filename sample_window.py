import tkinter as tk

def open_portfolio_window():
    portfolio_window = tk.Toplevel(root)
    portfolio_window.title("Портфель")

    label = tk.Label(portfolio_window, text="Это окно портфель", padx=20, pady=20)
    label.pack()

    # Center the new window
    portfolio_window.update_idletasks() 
    width = portfolio_window.winfo_width()
    height = portfolio_window.winfo_height()
    screen_width = portfolio_window.winfo_screenwidth()
    screen_height = portfolio_window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    portfolio_window.geometry(f'{width}x{height}+{x}+{y}')

def open_trading_window():
    # Create a new window for Торговля
    trading_window = tk.Toplevel(root)
    trading_window.title("Торговля")

    # Create a label to display in the new window
    label = tk.Label(trading_window, text="Это окно торговли", padx=20, pady=20)
    label.pack()

    trading_window.update_idletasks() 
    width = trading_window.winfo_width()
    height = trading_window.winfo_height()
    screen_width = trading_window.winfo_screenwidth()
    screen_height = trading_window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    trading_window.geometry(f'{width}x{height}+{x}+{y}')

def open_reports_window():
    # Create a new window for Отчеты
    reports_window = tk.Toplevel(root)
    reports_window.title("Отчеты")

    # Create a label to display in the new window
    label = tk.Label(reports_window, text="Это окно отчеты", padx=20, pady=20)
    label.pack()

    # Center the new window
    reports_window.update_idletasks() 
    width = reports_window.winfo_width()
    height = reports_window.winfo_height()
    screen_width = reports_window.winfo_screenwidth()
    screen_height = reports_window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    reports_window.geometry(f'{width}x{height}+{x}+{y}')

def create_table(rows, columns):
    for i in range(rows):
        for j in range(columns):
            cell = tk.Frame(root, width=100, height=30, borderwidth=5, relief="solid", bg="white")
            cell.grid(row=i, column=j, padx=5, pady=5)

            if i == 0 and j == 0:  # (1, 1)
                # Button for Портфель
                button_portfolio = tk.Button(cell, text="Портфель", bg="lightblue", command=open_portfolio_window)
                button_portfolio.pack(expand=True)
            elif i == 0 and j == 1:  # (1, 2)
                # Button for Торговля
                button_trading = tk.Button(cell, text="Торговля", bg="lightgreen", command=open_trading_window)
                button_trading.pack(expand=True)
            elif i == 0 and j == 2:  # (1, 3)
                # Button for Отчеты
                button_reports = tk.Button(cell, text="Отчеты", bg="lightyellow", command=open_reports_window)
                button_reports.pack(expand=True)
            else:
                label = tk.Label(cell, text=f"Cell {i+1},{j+1}", bg="white")
                label.pack(expand=True)

root = tk.Tk()
root.title("Таблица с ячейками")

create_table(8, 6)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop()