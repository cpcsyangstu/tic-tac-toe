import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

label = tk.Label(window, text="Hello World!")
canvas = tk.Canvas(window,bg="black",width=500,height=500)

label.pack()
canvas.pack()

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
