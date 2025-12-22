import numpy as np
from scipy.interpolate import lagrange
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

bg_color = '#800020'    # Burgundy
text_color = '#f5f5dc'  # Cream
entry_bg = '#f5f5dc'
entry_fg = '#000000'
font_style = ("Segoe UI", 12)

root = tk.Tk()
root.title("Lagrange Interpolation")
root.configure(bg=bg_color)
root.geometry("500x300")
root.minsize(400, 250)

def get_table():
    try:
        global entry_fields
        count = int(entry_count.get())
        entry_frame.destroy()
        show_table(count)
    except:
        pass

def show_table(count):
    global entry_fields, xp_entry, result_label
    entry_fields = []

    table_win = tk.Toplevel(root)
    table_win.title("Enter Data Points")
    table_win.configure(bg=bg_color)
    table_win.geometry("600x500")
    table_win.rowconfigure(tuple(range(count + 6)), weight=1)
    table_win.columnconfigure((0, 1), weight=1)

    header = tk.Label(table_win, text="Enter X and Y values:", bg=bg_color, fg=text_color, font=("Segoe UI", 14, "bold"))
    header.grid(row=0, column=0, columnspan=2, pady=5, sticky="ew")

    for i in range(count):
        x_entry = tk.Entry(table_win, bg=entry_bg, fg=entry_fg, font=font_style, relief='flat', justify='center')
        y_entry = tk.Entry(table_win, bg=entry_bg, fg=entry_fg, font=font_style, relief='flat', justify='center')
        x_entry.grid(row=i+1, column=0, padx=5, pady=2, sticky="nsew")
        y_entry.grid(row=i+1, column=1, padx=5, pady=2, sticky="nsew")
        x_label = tk.Label(table_win, text=f"X{i}", bg=bg_color, fg=text_color, font=font_style)
        y_label = tk.Label(table_win, text=f"Y{i}", bg=bg_color, fg=text_color, font=font_style)
        x_label.grid(row=i+1, column=0, sticky="w", padx=5)
        y_label.grid(row=i+1, column=1, sticky="w", padx=5)
        entry_fields.append((x_entry, y_entry))

    tk.Label(table_win, text="Enter Xp:", bg=bg_color, fg=text_color, font=font_style).grid(row=count+2, column=0, pady=5, sticky="e", padx=(0, 10))

    xp_entry = tk.Entry(table_win, bg=entry_bg, fg=entry_fg, font=font_style, relief='flat', justify='center')
    xp_entry.grid(row=count+2, column=1, pady=5, padx=(0, 10), sticky="w")

    calc_btn = tk.Button(table_win, text="Calculate", bg=entry_bg, fg=entry_fg, font=font_style, command=calculate)
    calc_btn.grid(row=count+3, column=0, columnspan=2, pady=10, sticky="ew")

    result_label = tk.Label(table_win, text="", bg=bg_color, fg=text_color, font=font_style)
    result_label.grid(row=count+4, column=0, columnspan=2, sticky="ew")

def calculate():
    try:
        xi = np.array([float(x.get()) for x, _ in entry_fields])
        yi = np.array([float(y.get()) for _, y in entry_fields])
        xp = float(xp_entry.get())

        poly = lagrange(xi, yi)
        yp = poly(xp)
        y_derivative = poly.deriv()(xp)

        result_label.config(text=f"Y({xp}) = {yp:.4f}   |   Y'({xp}) = {y_derivative:.4f}")

        plt.figure(figsize=(5, 4))
        xp_plot = np.linspace(min(xi), max(xi), 500)
        yp_plot = poly(xp_plot)
        plt.plot(xp_plot, yp_plot, label="Lagrange Polynomial", color='orange')
        plt.scatter(xi, yi, color='red', label='Data Points')
        plt.axvline(x=xp, linestyle='--', color='gray', label=f'Xp = {xp}')
        plt.title("Lagrange Interpolation")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        result_label.config(text="Error: " + str(e))

# ===> finally <3
entry_frame = tk.Frame(root, bg=bg_color)
entry_frame.pack(expand=True, fill='both', padx=20, pady=20)

tk.Label(entry_frame,
    text="How many items?", bg=bg_color, fg=text_color, font=("Segoe UI", 16, "bold")).pack(pady=10, fill='x')
entry_count = tk.Entry(entry_frame, bg=entry_bg, fg=entry_fg, font=font_style, relief='flat', justify='center')
entry_count.pack(pady=10, fill='x')

go_btn = tk.Button(entry_frame, text="Next", bg=entry_bg, fg=entry_fg, font=font_style, command=get_table)
go_btn.pack(pady=10, fill='x')

root.mainloop()