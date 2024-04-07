import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("300x150")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess the number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        self.attempts += 1
        guess = int(self.entry.get())
        if guess < self.target_number:
            messagebox.showinfo("Hint", "Too low!")
        elif guess > self.target_number:
            messagebox.showinfo("Hint", "Too high!")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right! It took you {self.attempts} attempts.")
            self.master.destroy()

def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
