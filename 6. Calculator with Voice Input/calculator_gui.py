# 🎤🧮 Voice Calculator using Tkinter + Speech Recognition
# -------------------------------------------------------
# Buttons se bhi calculate kar sakte ho
# Mic se bol ke bhi calculate kar sakte ho
# Example: "5 plus 3"
# -------------------------------------------------------

import tkinter as tk                 # GUI
import speech_recognition as sr      # Voice recognition


# 🎯 Expression store karne ke liye
expression = ""


# 🔘 Button click pe number/operator add karo
def press(value):
    global expression

    expression += str(value)     # value add
    entry_var.set(expression)    # screen update


# 🧮 Calculate result
def calculate():
    global expression

    try:
        result = str(eval(expression))   # expression evaluate
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error ❌")
        expression = ""


# 🗑 Clear screen
def clear():
    global expression
    expression = ""
    entry_var.set("")


# 🎤 Voice input function
def voice_input():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        result_label.config(text="🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()

        result_label.config(text=f"You said: {text}")

        # words → math operators
        text = text.replace("plus", "+")
        text = text.replace("minus", "-")
        text = text.replace("into", "*")
        text = text.replace("multiply", "*")
        text = text.replace("divide", "/")

        entry_var.set(text)

        global expression
        expression = text

        calculate()

    except:
        result_label.config(text="❌ Could not understand")


# ================= GUI =================

root = tk.Tk()
root.title("Voice Calculator 🎤🧮")
root.geometry("300x400")


# 📟 Display
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15)


# 🔘 Buttons layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]


# Grid buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        action = calculate if btn == '=' else lambda x=btn: press(x)

        tk.Button(frame, text=btn, command=action).pack(side="left", expand=True, fill="both")


# 🗑 Clear button
tk.Button(root, text="Clear", command=clear).pack(fill="both")

# 🎤 Voice button
tk.Button(root, text="🎤 Voice Input", command=voice_input).pack(fill="both")

# 📢 Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
