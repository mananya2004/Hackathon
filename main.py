import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from collections import Counter
from PIL import Image
import os


# Function to read questions from a text file
def load_questions_from_file(filename):
    """Reads questions from a given text file and returns a list of question dictionaries."""
    questions = []
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")
   
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        question = None
        options = []
       
        for line in lines:
            line = line.strip()
            if not line:  # Empty line, indicating end of a question
                if question:
                    questions.append({"question": question, "options": options})
                question = None
                options = []
            elif question is None:  # Start a new question
                question = line
            else:  # Options for the question
                options = line.split("|")
       
        # Add the last question if there were no trailing blank lines
        if question:
            questions.append({"question": question, "options": options})
   
    return questions


class MCQQuizGUI:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.answers = [None] * len(questions)
       
        self.question_label = ttk.Label(master, text="")
        self.question_label.pack(pady=10)
       
        self.options_frame = ttk.Frame(master)
        self.options_frame.pack(pady=5)
       
        self.next_button = ttk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(side=tk.RIGHT, padx=5)
       
        self.prev_button = ttk.Button(master, text="Previous", command=self.prev_question)
        self.prev_button.pack(side=tk.LEFT, padx=5)
       
        self.submit_button = ttk.Button(master, text="Submit", command=self.submit_quiz)
        self.submit_button.pack(pady=10)
       
        self.display_question()
   
    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=f"Question {self.current_question_index + 1}: {question['question']}")
       
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
       
        # Display new options
        answer_var = tk.IntVar()
        self.current_answer_var = answer_var
       
        for i, option in enumerate(question['options']):
            ttk.Radiobutton(self.options_frame, text=option, variable=answer_var, value=i, command=lambda value=i: self.store_answer(value)).pack(anchor=tk.W)

    def store_answer(self, value):
        self.answers[self.current_question_index] = value
   
    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question()
        else:
            messagebox.showinfo("End of Quiz", "You have reached the end of the quiz. Press SUBMIT to see your destination.")
   
    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.display_question()
        else:
            messagebox.showinfo("Beginning of Quiz", "You are at the beginning of the quiz.")

    def submit_quiz(self):
        if not any(answer is not None for answer in self.answers):
            messagebox.showwarning("Submit", "No answers to submit.")
            return
       
        counter = Counter(self.answers)
        most_common_answer = counter.most_common(1)[0][0]
       
        destinations = {
            0: "Jordan",
            1: "Tajikistan",
            2: "India"
        }
       
        destination = destinations.get(most_common_answer, "Unknown")
       
        message = f"Based on your answers, your travel destination is {destination}."
        messagebox.showinfo("Quiz Result", message)
       
        image_paths = {
            "Jordan": "jordan.jpg",
            "Tajikistan": "tajikistan.jpg",
            "India": "india.jpg"
        }
       
        img_path = image_paths.get(destination, "")
       
        if img_path:
            try:
                # Open the image file
                img = Image.open(img_path)
               
                # Show the image
                img.show()
            except FileNotFoundError:
                messagebox.showerror("Image Error", "Image file not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Unknown Destination", "No image available for the suggested destination.")


# Load questions from the text file
questions_file = "questions.txt"
questions = load_questions_from_file(questions_file)

# Create Tkinter window
root = tk.Tk()
root.title("Discovering Asia's Secrets")

# Create MCQQuizGUI instance with questions loaded from the file
quiz_gui = MCQQuizGUI(root, questions)

root.mainloop()