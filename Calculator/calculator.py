import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            expression = display_var.get()
            result = eval(expression)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")

    elif button_text == "C":
        display_var.set("")
    else:
        current_text = display_var.get()
        current_text += button_text
        display_var.set(current_text)

root = tk.Tk()
root.title("Simple Calculator")

display_var = tk.StringVar()
display_var.set("")

entry = tk.Entry(root, textvar=display_var, font="lucida 20 bold")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font="lucida 15 bold")
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", on_button_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
