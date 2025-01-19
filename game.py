import random
import tkinter as tk
from tkinter import messagebox


class BettingGame:
    def __init__(self, root):
        self.balance = 100
        self.root = root
        self.root.title("Betting Game")

        # Widgets
        self.balance_label = tk.Label(root, text=f"Balance: {self.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.bet_label = tk.Label(root, text="Enter Bet (max 100):", font=("Arial", 12))
        self.bet_label.pack()

        self.bet_entry = tk.Entry(root, font=("Arial", 12))
        self.bet_entry.pack(pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_game, font=("Arial", 12), bg="lightblue")
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def play_game(self):
        try:
            bet = int(self.bet_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        if bet < 1 or bet > self.balance:
            messagebox.showwarning("Invalid Bet", f"Bet must be between 1 and {self.balance}.")
            return

        odds = random.randint(1, 10)
        result = random.choice(["Win", "Lose"])

        if result == "Win":
            winning = bet * odds
            self.balance += winning
            self.result_label.config(
                text=f"You won! Odds: {odds}, Winning: {winning}", fg="green"
            )
        else:
            self.balance -= bet
            self.result_label.config(
                text=f"You lost! Odds: {odds}, Bet: {bet}", fg="red"
            )

        self.balance_label.config(text=f"Balance: {self.balance}")

        if self.balance <= 0:
            messagebox.showinfo("Game Over", "You have no more balance. Thank you for playing!")
            self.root.quit()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = BettingGame(root)
    root.mainloop()
