# 🧠 Quiz App GUI using Tkinter
# -----------------------------------

import tkinter as tk
from questions import questions


index = 0      # current question
score = 0      # score


# 🔄 Next question show karo
def show_question():

    global index

    if index < len(questions):
        q = questions[index]

        question_label.config(text=q["question"])

        for i in range(4):
            buttons[i].config(text=q["options"][i])
    else:
        question_label.config(text=f"🎉 Final Score: {score}/{len(questions)}")

        for btn in buttons:
            btn.config(state="disabled")


# ✅ Answer check
def check_answer(choice):

    global index, score

    if choice == questions[index]["answer"]:
        score += 1

    index += 1
    show_question()


# ================= GUI =================

root = tk.Tk()
root.title("Quiz App 🧠")
root.geometry("400x300")


question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
question_label.pack(pady=20)


buttons = []

for _ in range(4):
    btn = tk.Button(root, width=30)
    btn.pack(pady=5)
    buttons.append(btn)


# button commands set
for i, btn in enumerate(buttons):
    btn.config(command=lambda b=btn: check_answer(b.cget("text")))


show_question()

root.mainloop()
