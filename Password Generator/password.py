import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    if length <= 0:
        result_label.config(text="Invalid length. Please enter a positive number.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated password: " + password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")
length_label = ttk.Label(app, text="Enter the desired length of the password:")
length_label.pack()

length_entry = ttk.Entry(app)
length_entry.pack()


generate_button = ttk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()


result_label = ttk.Label(app, text="")
result_label.pack()

app.mainloop()
