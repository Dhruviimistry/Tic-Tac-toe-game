import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Winning combinations
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            disable_all_buttons()
            return

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # FIXED: = not ==
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "0" else "0"
    label.config(text=f"Player {current_player}'s turn")

def disable_all_buttons():
    global winner
    winner = True
    for button in buttons:
        button.config(state="disabled")

# Initialize window
root = tk.Tk()  # FIXED: tk.TK() → tk.Tk()
root.title("Tic Tac Toe")  # FIXED: tittle → title

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Game state
current_player = "x"
winner = False

# Display current turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))  # FIXED: lable → label
label.grid(row=3, column=0, columnspan=3)

root.mainloop()

    
    