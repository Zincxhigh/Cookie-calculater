import tkinter as tk
from tkinter import messagebox

def calculate_cookies():
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        total_minutes = hours * 60 + minutes
        cookies_per_minute = 53 / 615
        my_cookies = total_minutes * cookies_per_minute

        result_label.config(text=f"You earned {my_cookies:.1f} cookies! 🍪", fg="#8B4513")  # brown color
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
def on_enter(e):
    calc_button.config(bg="#FFD700")  
def on_leave(e):
    calc_button.config(bg="#FFA500") 
root = tk.Tk()
root.title("Hackpad Flavourtown Cookie Calculator")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#FFF5E1") 


title_label = tk.Label(root, text="🍪 Cookie Calculator 🍪", font=("Arial", 18, "bold"), bg="#FFF5E1", fg="#D2691E")
title_label.pack(pady=20)

hours_label = tk.Label(root, text="Hours worked:", font=("Arial", 12), bg="#FFF5E1", fg="#8B4513")
hours_label.pack()
hours_entry = tk.Entry(root, width=25, font=("Arial", 12))
hours_entry.pack(pady=5)

minutes_label = tk.Label(root, text="Minutes worked:", font=("Arial", 12), bg="#FFF5E1", fg="#8B4513")
minutes_label.pack()
minutes_entry = tk.Entry(root, width=25, font=("Arial", 12))
minutes_entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate Cookies", font=("Arial", 14), padx=10, pady=5,
      bg="#FFA500", fg="white", activebackground="#FFD700", command=calculate_cookies)
calc_button.pack(pady=20)

calc_button.bind("<Enter>", on_enter)
calc_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#FFF5E1")
result_label.pack(pady=10)
root.mainloop()


