import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")
        master.geometry("350x200")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=5)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(
                    text=f"Congratulations! You guessed it in {self.attempts} attempts."
                )
                self.guess_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()