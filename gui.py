# gui.py
import tkinter as tk
from tkinter import messagebox
from discount import calculate_discount

def calculate():
    try:
        price = float(entry_price.get())
        discount_percent = float(entry_discount.get())
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            messagebox.showinfo("Result", f"Discount applied! Final price: ${final_price}")
        else:
            messagebox.showinfo("Result", f"No discount applied. Original price: ${price}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("DiscountGenie GUI")

tk.Label(root, text="Original Price:").grid(row=0, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=0, column=1)

tk.Label(root, text="Discount %:").grid(row=1, column=0)
entry_discount = tk.Entry(root)
entry_discount.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2)

root.mainloop()
