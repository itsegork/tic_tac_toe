import tkinter as tk
from tkinter import messagebox
import random

# Инициализация доски строками
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def draw_board():
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            button = buttons[index]
            button.config(text=board[index], state=tk.NORMAL)

def check_winner():
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return None

def player_move(index):
    if board[index] not in "XO":
        board[index] = "X"
        buttons[index].config(text="X", state=tk.DISABLED)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Победа", f"{winner} победил!")
            reset_board()
        elif all(x in "XO" for x in board):
            messagebox.showinfo("Ничья", "Ничья!")
            reset_board()
        else:
            computer_move()

def computer_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] not in "XO":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"
    buttons[best_move].config(text="O", state=tk.DISABLED)
    winner = check_winner()
    if winner:
        messagebox.showinfo("Победа", f"{winner} победил!")
        reset_board()
    elif all(x in "XO" for x in board):
        messagebox.showinfo("Ничья", "Ничья!")
        reset_board()

def minimax(board, is_maximizing):
    winner = check_winner()
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif all(x in "XO" for x in board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] not in "XO":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = str(i + 1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] not in "XO":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = str(i + 1)
                best_score = min(score, best_score)
        return best_score

def reset_board():
    global board
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    draw_board()

# Создание окна
root = tk.Tk()
root.title("Крестики-нолики")

buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

draw_board()
root.mainloop()