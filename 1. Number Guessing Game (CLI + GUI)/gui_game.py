# 🎯 Number Guessing Game (GUI Version)
# --------------------------------------------------
# Tkinter use karke window based game
# Buttons + Entry + Labels
# --------------------------------------------------

import random              # Random number
import tkinter as tk       # GUI library


# 🎲 Secret number generate
secret_number = random.randint(1, 100)

# 🔁 Attempts count
attempts = 0


# 🧠 Guess check karne ka function
def check_guess():
    global attempts

    # 👤 Entry box se value lena
    guess = int(entry.get())

    # ➕ attempts badhao
    attempts += 1

    # 🎯 Compare logic
    if guess < secret_number:
        result_label.config(text="📉 Too Low!")

    elif guess > secret_number:
        result_label.config(text="📈 Too High!")

    else:
        result_label.config(
            text=f"🎉 Correct in {attempts} attempts!"
        )


# 🪟 Window create
root = tk.Tk()
root.title("Number Guessing Game 🎯")
root.geometry("350x250")


# 🏷️ Title label
title = tk.Label(root, text="Guess Number (1-100)", font=("Arial", 14))
title.pack(pady=10)


# 📝 Input box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)


# 🔘 Button
btn = tk.Button(root, text="Check Guess", command=check_guess)
btn.pack(pady=10)


# 📢 Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)


# ▶ Start GUI loop
root.mainloop()
