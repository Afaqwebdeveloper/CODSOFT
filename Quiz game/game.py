import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is 7 multiplied by 8?",
        "options": ["42", "48", "56", "64"],
        "correct_answer": "56",
    },
]

current_question = 0
score = 0

# Create the main application window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")

# Welcome Screen
welcome_label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 18))
welcome_label.pack(pady=20)

# Instructions
instructions = """
Instructions:
1. Answer the following questions.
2. Click 'Next' to move to the next question.
3. Your score will be displayed at the end.
"""
instructions_label = tk.Label(root, text=instructions, font=("Helvetica", 12))
instructions_label.pack()

# Question Label
question_label = tk.Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=10)

# Radio Buttons for Options
selected_option = tk.StringVar()
option1 = tk.Radiobutton(root, text="", variable=selected_option, value="")
option2 = tk.Radiobutton(root, text="", variable=selected_option, value="")
option3 = tk.Radiobutton(root, text="", variable=selected_option, value="")
option4 = tk.Radiobutton(root, text="", variable=selected_option, value="")

option1.pack()
option2.pack()
option3.pack()
option4.pack()

# Next Button
def next_question():
    global current_question, score
    if current_question < len(questions):
        if selected_option.get() == questions[current_question]["correct_answer"]:
            score += 1
        current_question += 1
        load_question()

next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=10)

# Load a new question
def load_question():
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            if i == 0:
                option1.config(text=option, value=option)
            elif i == 1:
                option2.config(text=option, value=option)
            elif i == 2:
                option3.config(text=option, value=option)
            elif i == 3:
                option4.config(text=option, value=option)
        selected_option.set("")
    else:
        messagebox.showinfo("Quiz Over", f"Your score: {score}/{len(questions)}")

# Start the quiz
load_question()

root.mainloop()
