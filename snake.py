import tkinter as tk    # for the graphics
import random           # for random location generator to place the food

# STEP 0
ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

# STEP 4: create the Tile class for the snake and food
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

# STEP 4: initialize the game: create the snake head and the food
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)      # x y are in pixel (not col,row numbers)
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
# STEP 5: we need to make snake move. We need snake velocity
velocity_x = 0
velocity_y = 0

# STEP 4: draw the snake
def draw():
    global snake
    # draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="lime green")
    # draw the food
    canvas.create_rectangle(food.x, food.y, food.x+TILE_SIZE, food.y+TILE_SIZE, fill="red")
    # redraws at a frequency
    app.after(100, draw)    # 100ms call the draw function ==> 10 frames per second

# STEP 4: run the program
draw()

# STEP 5: make the snake move. We need a key listener


# (STEP 1) keep this towards the end 
app.mainloop()


