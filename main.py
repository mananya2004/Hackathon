def store_answer(self, value):
    	self.answers[self.current_question_index] = value
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    	for i, option in enumerate(question['options']):
        	answer_var = tk.IntVar()
        	ttk.Radiobutton(self.options_frame, text=option, variable=answer_var, value=i, command=lambda value=i: self.store_answer(value)).pack(anchor=tk.W)

	def store_answer(self, value):
    	self.answers[self.current_question_index] = value
    
	def next_question(self):
    	if self.current_question_index < len(self.questions) - 1:
        	self.current_question_index += 1
        	self.display_question()
    	else:
        	messagebox.showinfo("End of Quiz", "You have reached the end of the quiz.")
    
	def prev_question(self):
    	if self.current_question_index > 0:
        	self.current_question_index -= 1
        	self.display_question()
    	else:
        	messagebox.showinfo("Beginning of Quiz", "You are at the beginning of the quiz.")
    
	def submit_quiz(self):
    	total_questions = len(self.questions)
    	correct_answers = sum(1 for i, answer in enumerate(self.answers) if answer is not None and answer == self.questions[i]['answer'])
    	if total_questions == 0:
        	messagebox.showwarning("Submit", "No questions to submit.")
    	else:
        	score = f"You scored {correct_answers} out of {total_questions} questions correctly."
        	percentage = (correct_answers / total_questions) * 100
        	message = f"{score} Your percentage is: {percentage:.2f}%"
        	messagebox.showinfo("Quiz Result", message)

# Sample quiz questions
questions = [
	{
   	 'question': 'Which historical site intrigues you the most??',
   	 'options': ['Archeological sites in deserts', 'Historical Silk Road',  'Architectural wonder'],
   	 'answer': 1
    },
    {
   	 'question': 'What type of adventure are you seeking?',
   	 'options': [' Exploring ancient ruins in the desert ', ' Trekking in the rugged landscapes of the mountains', ' Experiencing the vibrant culture and bustling streets'],
   	 'answer': 1
    },
    {
   	 'question': 'What kind of cuisine are you most excited to try?',
   	 'options': ['Blend of grilled meats and flavourful mezze', ' Cuisine featuring hearty stews and savory breads ', 'Curries, biryanis, and street food delights like chaat '],
   	 'answer': 1
    },
	{
   	 'question': 'What type of adventure are you seeking?',
   	 'options': [' Exploring ancient ruins in the desert ', ' Trekking in the rugged landscapes of the mountains', ' Experiencing the vibrant culture and bustling streets'],
   	 'answer': 1
    },
	{
   	 'question': 'What type of cultural experience appeals to you?',

   	 'options': [' Bedouin hospitality and traditional music under the starry skies ', ' Exploring the ancient Silk Road history and vibrant bazaars', ' Immersing yourself in the colorful festivals and spiritual heritage'],
   	 'answer': 1
    },
    {
   	 'question': 'Which outdoor activity excites you the most? ',
   	 'options': ['Dune bashing and camel trekking in the vast deserts ', ' Whitewater rafting along the roaring rivers', 'Yoga retreats in the tranquil settings '],
   	 'answer': 1
    }

]

# Create Tkinter window
root = tk.Tk()
root.title("MCQ Quiz")

# Create MCQQuizGUI instance
quiz_gui = MCQQuizGUI(root, questions)

root.mainloop()


