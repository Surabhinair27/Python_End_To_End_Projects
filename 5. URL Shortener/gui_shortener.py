# 🔗 URL Shortener GUI using Tkinter
# ---------------------------------------------------

import tkinter as tk
import requests


# 🔍 Shorten function
def shorten_url():

    long_url = entry.get()

    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"

    response = requests.get(api_url)

    if response.status_code == 200:
        short_url = response.text

        result_entry.delete(0, tk.END)
        result_entry.insert(0, short_url)

    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error ❌")


# 📋 Copy to clipboard
def copy_to_clipboard():

    root.clipboard_clear()
    root.clipboard_append(result_entry.get())


# 🪟 Window
root = tk.Tk()
root.title("URL Shortener 🔗")
root.geometry("400x250")


# 🏷️ Label
tk.Label(root, text="Enter Long URL").pack(pady=5)


# 📝 Input box
entry = tk.Entry(root, width=40)
entry.pack(pady=5)


# 🔘 Shorten button
tk.Button(root, text="Shorten URL", command=shorten_url).pack(pady=10)


# 📦 Result
result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)


# 📋 Copy button
tk.Button(root, text="Copy", command=copy_to_clipboard).pack(pady=5)


root.mainloop()
