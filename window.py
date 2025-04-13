from tkinter import ttk, Tk, Canvas
import tkinter as tk
from drawed import Line, Cell


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Game")
        self.root.geometry(f"{width}x{height}")
        self.frame = ttk.Frame(self.root)
        self.canvas = Canvas(self.frame, height=height, width=width)
        self.control_frame = ttk.Frame(self.root, relief=tk.RAISED)
        self.break_walls = ttk.Button(self.control_frame, text="Break Walls")
        self.start_solve = ttk.Button(
            self.control_frame, text="Solve with algorithm")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.grid(column=0, row=0)
        self.canvas.grid(stick=tk.NSEW)
        self.control_frame.grid(column=0, row=1)
        self.break_walls.grid(column=0, row=0)
        self.start_solve.grid(column=1, row=0)

        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def set_break_walls_func(self, func):
        self.break_walls.configure(command=func)
        self.break_walls.update()

    def set_solve_func(self, func):
        self.start_solve.configure(command=func)
        self.start_solve.update()

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

    def draw_move(self, cell1: Cell, cell2: Cell, undo=False):
        cell1.draw_move(self.canvas, cell2, undo)
