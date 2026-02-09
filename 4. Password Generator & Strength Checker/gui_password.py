# 🔐 Password Generator GUI using Tkinter
# ------------------------------------------------

import tkinter as tk
import random
import string


# 🔑 Password generate function
def generate_password():

    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    strength_label.config(text=check_strength(password))


# 💪 Strength checker
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    levels = ["Weak 😢", "Medium 🙂", "Strong 💪", "Very Strong 🔥"]

    return "Strength: " + (levels[score-1] if score > 0 else "Very Weak")


# 🪟 Window
root = tk.Tk()
root.title("Password Generator 🔐")
root.geometry("350x250")


# 🔢 Length input
tk.Label(root, text="Password Length").pack(pady=5)

length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()


# 🔘 Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)


# 🔑 Password output
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)


# 💪 Strength label
strength_label = tk.Label(root, text="")
strength_label.pack(pady=5)


root.mainloop()
