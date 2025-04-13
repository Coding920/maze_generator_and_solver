import time
import random
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
            win: Window = None,
            seed=True
    ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.abandoned_cells = []
        if seed:
            random.seed(1, version=2)
        self.create_cells()
        if self.win:
            self.win.set_break_walls_func(self.break_walls)
            self.win.set_solve_func(self.solve)

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
                    self.animate(0.001)
                y += self.cell_size_y
            x += self.cell_size_x
            self.cells.append(cells)

    def animate(self, sleep_seconds):
        self.win.redraw()
        time.sleep(sleep_seconds)

    def break_walls(self):
        self._break_walls_r(0, 0)
        if self.abandoned_cells:
            for coord in self.abandoned_cells:
                self._break_walls_r(
                    coord[0], coord[1])
        self._break_entrance_and_exit()
        self._reset_visited()

    def _reset_visited(self):
        for cell_list in self.cells:
            for cell in cell_list:
                cell.visited = False

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_left = False
        self.cells[-1][-1].has_right = False
        if self.win:
            self.win.draw_cell(self.cells[0][0])
            self.win.draw_cell(self.cells[-1][-1])

    def _break_walls_r(self, i, j, depth=0):
        deep_return = False
        if depth > 800:  # Don't let it recurse too deep
            deep_return = True
        self.cells[i][j].visited = True

        while True:
            to_visit = []

            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if i < len(self.cells) - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if j < len(self.cells[0]) - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                return
            elif len(to_visit) - 1 == 0:
                rand = 0
            else:
                rand = random.randrange(len(to_visit))

            if deep_return:
                self.abandoned_cells.append((i, j))
                return

            new_i, new_j = self._break_cell_wall(
                self.cells[i][j],
                self.cells[to_visit[rand][0]][to_visit[rand][1]], i, j)

            self._break_walls_r(new_i, new_j, depth + 1)

    def _break_cell_wall(self, current_cell: Cell, other_cell: Cell, i, j):
        break_wall_seconds = 0.04
        if i < len(self.cells) - 1 and other_cell == self.cells[i + 1][j]:
            current_cell.has_right = False
            other_cell.has_left = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(break_wall_seconds)
            return i + 1, j

        if j < len(self.cells[i]) - 1 and other_cell == self.cells[i][j + 1]:
            current_cell.has_bottom = False
            other_cell.has_top = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(break_wall_seconds)
            return i, j + 1

        if i > 0 and other_cell == self.cells[i - 1][j]:
            current_cell.has_left = False
            other_cell.has_right = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(break_wall_seconds)
            return i - 1, j

        if j > 0 and other_cell == self.cells[i][j - 1]:
            current_cell.has_top = False
            other_cell.has_bottom = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(break_wall_seconds)
            return i, j - 1

    def solve(self):
        return self._solve_r()

    def _solve_r(self, i=0, j=0):
        solve_speed_seconds = 0.1
        if self.win:
            self.animate(solve_speed_seconds)
        self.cells[i][j].visited = True
        if self.cells[i][j] == self.cells[-1][-1]:
            return True

        to_visit = []
        for _ in range(4):
            if (i > 0 and not self.cells[i - 1][j].visited
                    and not self.cells[i][j].has_left):
                to_visit.append((i - 1, j))

            if (j > 0 and not self.cells[i][j - 1].visited
                    and not self.cells[i][j].has_top):
                to_visit.append((i, j - 1))

            if (i < len(self.cells) - 1 and not self.cells[i + 1][j].visited
                    and not self.cells[i][j].has_right):
                to_visit.append((i + 1, j))

            if (j < len(self.cells[i]) - 1 and not self.cells[i][j + 1].visited
                    and not self.cells[i][j].has_bottom):
                to_visit.append((i, j + 1))

            if not to_visit:
                return False
            elif len(to_visit) == 1:
                rand = 0
            else:
                rand = random.randrange(len(to_visit))

            rand_coords = to_visit[rand]
            if self.win:
                self.win.draw_move(
                    self.cells[i][j],
                    self.cells[rand_coords[0]][rand_coords[1]]
                )
            correct_cell = self._solve_r(rand_coords[0], rand_coords[1])
            if correct_cell:
                return True
            if self.win:
                self.win.draw_move(
                    self.cells[i][j],
                    self.cells[rand_coords[0]][rand_coords[1]],
                    undo=True
                )

        return False
