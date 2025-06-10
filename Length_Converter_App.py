import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number!")

root = tk.Tk()
root.title("Length Converter (Inches to Centimeters)")

tk.Label(root, text="Enter length in inches:").grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Convert", command=convert_length).grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
