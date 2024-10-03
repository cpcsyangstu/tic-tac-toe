import tkinter as tk    # for the graphics
import random           # for random location generator to place the food

# STEP 0
ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

# STEP 1: game window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
app = App()
# window = tkinter.Tk()
app.title("Snake")
app.resizable(False, False)     # disallow the user to change the window size

# # STEP 2: canvas
canvas = tk.Canvas(app, bg = "gray", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
app.update()

# STEP 3: center the app in the center of the screen
# center the window
window_width = app.winfo_width()
window_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
#format "(w)x(h)+(x)+(y)"
app.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# (STEP 1) keep this towards the end 
app.mainloop()


