import tkinter as tk

def click_tile(row, col):
    global board, current_player
    board[row][col].config(text=current_player + " " + str(col) + str(row))
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X" 
    message["text"] = current_player + "'s turn"

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
game_over = False
turn = 0
current_player = "X"
BLACK = "#000000"
GRAY = "#0f0f0f"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

window = tk.Tk()
window.title("Tic Tac Toe Game")
# window.resizable(False, False)
frame = tk.Frame(window)
frame.grid_propagate(True)
# tkinter grid usage: https://pythonroadmap.com/blog/tkinter-grid-manager-tutorial
message = tk.Label(frame, text=current_player+"'s turn", font=("Consolas", 30))
message.grid(row=0, column=0, columnspan=3, sticky='we')
# set up board
for row in range(3):
    for col in range(3):
        board[row][col] = tk.Button(frame, text="", font=("Consolas", 50, "bold"), bg=GRAY, fg=BLUE, width=4, height=1, name=str(row)+","+str(col), command=lambda r=row, c=col: click_tile(r, c))
        board[row][col].grid(row=row+1, column=col)

# temp_button = tk.Button(frame, text="")
# temp_button.config(text="HOLA")

frame.pack()
window.mainloop()

# board = [['.', '.', '.'],
#          ['.', '.', '.'],
#          ['.', '.', '.']]

# def print_board():
#     print(board[0])
#     print(board[1])
#     print(board[2])

# def play():
#     pass
# # main program -----------------
# # print_instructions()

# print_board()
# # if no winner then (repeat)
# # play()
# print_board()
# # check_winner()
