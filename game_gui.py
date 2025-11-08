import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        
        self.number = random.randint(1, 100)
        self.attempts = 0
        
        tk.Label(root, text="Number Guessing Game", font=("Arial", 16)).pack(pady=10)
        tk.Label(root, text="Guess a number between 1 and 100:").pack(pady=5)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        # Button with color and hover effect
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess, bg="#4CAF50", fg="white")
        self.guess_button.pack(pady=5)
        self.guess_button.bind("<Enter>", lambda e: self.guess_button.config(bg="#45a049"))
        self.guess_button.bind("<Leave>", lambda e: self.guess_button.config(bg="#4CAF50"))
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        self.attempts_label = tk.Label(root, text="Attempts: 0")
        self.attempts_label.pack(pady=5)
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            
            if guess < self.number:
                self.result_label.config(text="Too low! Try again.", fg="blue")
            elif guess > self.number:
                self.result_label.config(text="Too high! Try again.", fg="red")
            else:
                messagebox.showinfo("Winner!", f"Correct! You won in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
