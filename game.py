import tkinter as tk
import random
import time
import winsound
from threading import Thread

# Main window
root = tk.Tk()
root.title("Memory Game")
root.geometry("400x500")
root.config(bg="white")

# Game variables
colors = ["red", "blue", "green", "yellow"]
sequence = []
user_sequence = []
buttons = {}
is_user_turn = False
round_number = 0
high_score = 0

# Header frame (for score display)
header_frame = tk.Frame(root, bg="white")
header_frame.pack(fill=tk.X, padx=10, pady=5)

status_label = tk.Label(header_frame, text="Welcome to Memory Game!", font=("Arial", 14), bg="white")
status_label.pack(side=tk.LEFT)

high_score_label = tk.Label(header_frame, text="🏆 High Score: 0", font=("Arial", 14), bg="white")
high_score_label.pack(side=tk.RIGHT)

# Sound frequencies for each color
def play_sound(color):
    tones = {
        "red": 400,
        "blue": 500,
        "green": 600,
        "yellow": 700,
    }
    winsound.Beep(tones[color], 200)

# Flash a button (visual + sound)
def flash_button(color, delay):
    play_sound(color)
    orig_color = buttons[color]["bg"]
    buttons[color].config(bg="white")
    root.update()
    time.sleep(delay / 2)
    buttons[color].config(bg=orig_color)
    root.update()
    time.sleep(delay / 2)

# Show the full sequence
def play_sequence():
    global is_user_turn, user_sequence
    is_user_turn = False
    user_sequence = []
    delay = max(0.6 - round_number * 0.03, 0.1)  # Speed increases per round
    status_label.config(text=f"Round {round_number}: Memorize the sequence...")
    time.sleep(1)
    for color in sequence:
        flash_button(color, delay)
    status_label.config(text="Your turn! Click the buttons.")
    is_user_turn = True

# Start the game with 4 initial unique steps
def start_game():
    global sequence, round_number
    sequence.clear()
    round_number = 1
    last_color = None
    for _ in range(4):
        new_color = random.choice(colors)
        while new_color == last_color:
            new_color = random.choice(colors)
        sequence.append(new_color)
        last_color = new_color
    update_high_score()
    Thread(target=play_sequence).start()

# Add a new color and move to the next round
def next_round():
    global round_number
    round_number += 1
    last_color = sequence[-1]
    new_color = random.choice(colors)
    while new_color == last_color:
        new_color = random.choice(colors)
    sequence.append(new_color)
    update_high_score()
    Thread(target=play_sequence).start()

# Update high score
def update_high_score():
    global high_score
    if round_number > high_score:
        high_score = round_number
        high_score_label.config(text=f"🏆 High Score: {high_score}")

# Handle user input
def check_user_input(color):
    if not is_user_turn:
        return
    user_sequence.append(color)
    index = len(user_sequence) - 1
    flash_button(color, 0.2)

    if user_sequence[index] != sequence[index]:
        status_label.config(text=f"❌ Game Over! You reached round {round_number}.")
        return

    if user_sequence == sequence:
        status_label.config(text="✅ Correct! Get ready for the next round...")
        root.after(1000, next_round)

# Create color buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack()

for i, color in enumerate(colors):
    btn = tk.Button(
        button_frame,
        bg=color,
        width=10,
        height=5,
        command=lambda c=color: check_user_input(c)
    )
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
    buttons[color] = btn

# Start button
start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=start_game)
start_button.pack(pady=20)

# Run the app
root.mainloop()
