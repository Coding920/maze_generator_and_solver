from tkinter import Tk, BOTH, Canvas
from drawed import Line, Cell


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Game")
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root, height=height, width=width)

        self.canvas.grid()

        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_to_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color=fill_color)

    def draw_cell(self, cell: Cell):
        cell.draw(self.canvas)
