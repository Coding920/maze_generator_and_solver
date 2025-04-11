import time
from drawed import Cell, Line, Point
from window import Window


class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: Window = None
    ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        self.cells = []
        x = self.x
        for i in range(self.num_cols):
            cells = []
            y = self.y
            for j in range(self.num_rows):
                p1 = Point(x, y)
                p2 = Point(x + self.cell_size_x, y + self.cell_size_y)
                cell = Cell(p1, p2)
                cells.append(cell)
                if self.win:
                    self.win.draw_cell(cell)
                    self.animate()
                y += self.cell_size_y
            x += self.cell_size_x
            self.cells.append(cells)

    def animate(self):
        self.win.redraw()
        time.sleep(0.1)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_left = False
        self.cells[-1][-1].has_right = False
        if self.win:
            self.win.draw_cell(self.cells[0][0])
            self.win.draw_cell(self.cells[-1][-1])
