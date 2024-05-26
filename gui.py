import tkinter as tk
from tkinter import messagebox
import random

# A dictionary of celebrities with their estimated net worth (in millions)
net_worth = {
    "Elon Musk": 250000,
    "Jeff Bezos": 180000,
    "Bill Gates": 115000,
    "Mark Zuckerberg": 70000,
    "Warren Buffett": 105000,
    "Larry Page": 105000,
    "Sergey Brin": 100000,
    "Steve Jobs": 10000,
    "Oprah Winfrey": 3000,
    "Michael Jordan": 2200,
    "Mukesh Ambani": 83000,
    "Gautam Adani": 60000,
    "Ratan Tata": 1000,
    "Shah Rukh Khan": 750,
    "Amitabh Bachchan": 400,
    "Akshay Kumar": 300,
    "Virat Kohli": 125,
    "Sachin Tendulkar": 170,
    "Deepika Padukone": 50,
    "Priyanka Chopra": 70
}

class NetWorthGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Net Worth 'This or That' Game")
        self.root.geometry("500x500")
        self.score = 0
        
        self.create_widgets()
        self.new_game()
    
    def create_widgets(self):
        self.root.configure(bg='#1e1e1e')
        
        self.welcome_label = tk.Label(self.root, text="Welcome to the Net Worth 'This or That' Game!", font=("Helvetica", 16), wraplength=400, justify="center", bg='#1e1e1e', fg='#ffffff')
        self.welcome_label.pack(pady=20)
        
        self.instruction_label = tk.Label(self.root, text="Guess who has the higher net worth by clicking on 'A' or 'B'.", font=("Helvetica", 12), wraplength=400, justify="center", bg='#1e1e1e', fg='#ffffff')
        self.instruction_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 12), bg='#1e1e1e', fg='#ffffff')
        self.score_label.pack(pady=5)
        
        self.celeb1_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg='#1e1e1e', fg='#add8e6')
        self.celeb1_label.pack(pady=5)
        
        self.celeb2_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg='#1e1e1e', fg='#add8e6')
        self.celeb2_label.pack(pady=5)
        
        self.button_frame = tk.Frame(self.root, bg='#1e1e1e')
        self.button_frame.pack(pady=20)
        
        self.button_a = tk.Button(self.button_frame, text="A", command=lambda: self.check_choice('a'), font=("Helvetica", 12), width=10, bg="#00bfff", fg="#ffffff")
        self.button_a.pack(side=tk.LEFT, padx=10)
        
        self.button_b = tk.Button(self.button_frame, text="B", command=lambda: self.check_choice('b'), font=("Helvetica", 12), width=10, bg="#00bfff", fg="#ffffff")
        self.button_b.pack(side=tk.RIGHT, padx=10)
        
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 12), wraplength=400, justify="center", bg='#1e1e1e', fg='#ffffff')
        self.message_label.pack(pady=10)
        
        self.retry_button = tk.Button(self.root, text="Retry", command=self.retry_game, font=("Helvetica", 12), state=tk.DISABLED, bg="orange", fg="#ffffff")
        self.retry_button.pack(pady=10)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 12), bg="red", fg="#ffffff")
        self.exit_button.pack(pady=10)
    
    def get_two_random_celebrities(self):
        return random.sample(list(net_worth.keys()), 2)
    
    def new_game(self):
        self.celeb1, self.celeb2 = self.get_two_random_celebrities()
        self.celeb1_label.config(text=f"A: {self.celeb1}")
        self.celeb2_label.config(text=f"B: {self.celeb2}")
        self.message_label.config(text="")
        self.retry_button.config(state=tk.DISABLED)
        self.button_a.config(state=tk.NORMAL)
        self.button_b.config(state=tk.NORMAL)
    
    def check_choice(self, choice):
        chosen_celeb = self.celeb1 if choice == 'a' else self.celeb2
        other_celeb = self.celeb2 if choice == 'a' else self.celeb1
        
        if net_worth[chosen_celeb] >= net_worth[other_celeb]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.message_label.config(text="Correct!", fg="green")
            messagebox.showinfo("Correct!", f"{chosen_celeb} has a net worth of ${net_worth[chosen_celeb]:,} million.\n"
                                             f"{other_celeb} has a net worth of ${net_worth[other_celeb]:,} million.")
            self.new_game()
        else:
            self.message_label.config(text="Wrong!", fg="red")
            messagebox.showerror("Wrong!", f"{chosen_celeb} has a net worth of ${net_worth[chosen_celeb]:,} million.\n"
                                           f"{other_celeb} has a net worth of ${net_worth[other_celeb]:,} million.")
            self.retry_button.config(state=tk.NORMAL)
            self.button_a.config(state=tk.DISABLED)
            self.button_b.config(state=tk.DISABLED)
    
    def retry_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.new_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = NetWorthGame(root)
    root.mainloop()
