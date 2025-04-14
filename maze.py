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
        self.solve_speed_seconds = 0
        self.break_wall_seconds = 0
        self.create_speed_seconds = 0
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
                    self.animate(self.create_speed_seconds)
                y += self.cell_size_y
            x += self.cell_size_x
            self.cells.append(cells)

    def animate(self, sleep_seconds=0):
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
        self.abandoned_cells = []

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
        if depth > 800:  # Don't let it recurse too deep
            self.abandoned_cells.append((i, j))
            self.cells[i][j].visited = True
            return
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

            new_i, new_j = self._break_cell_wall(
                self.cells[i][j],
                self.cells[to_visit[rand][0]][to_visit[rand][1]], i, j)

            self._break_walls_r(new_i, new_j, depth + 1)

    def _break_cell_wall(self, current_cell: Cell, other_cell: Cell, i, j):
        if i < len(self.cells) - 1 and other_cell == self.cells[i + 1][j]:
            current_cell.has_right = False
            other_cell.has_left = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(self.break_wall_seconds)
            return i + 1, j

        if j < len(self.cells[i]) - 1 and other_cell == self.cells[i][j + 1]:
            current_cell.has_bottom = False
            other_cell.has_top = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(self.break_wall_seconds)
            return i, j + 1

        if i > 0 and other_cell == self.cells[i - 1][j]:
            current_cell.has_left = False
            other_cell.has_right = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(self.break_wall_seconds)
            return i - 1, j

        if j > 0 and other_cell == self.cells[i][j - 1]:
            current_cell.has_top = False
            other_cell.has_bottom = False
            if self.win:
                self.win.draw_cell(current_cell)
                self.win.draw_cell(other_cell)
                self.animate(self.break_wall_seconds)
            return i, j - 1

    def solve(self):
        return self._solve_r()

    def _solve_r(self, i=0, j=0, depth=0):
        if self.cells[i][j] == self.cells[-1][-1]:
            self.cells[i][j].visited = True
            return True
        if depth > 800:
            self._solve_iteratively(i, j)

        self.cells[i][j].visited = True

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
                self.animate(self.solve_speed_seconds)
            correct_cell = self._solve_r(
                rand_coords[0], rand_coords[1], depth + 1)
            if correct_cell:
                return True
            if self.win:
                self.win.draw_move(
                    self.cells[i][j],
                    self.cells[rand_coords[0]][rand_coords[1]],
                    undo=True
                )
                self.animate(self.solve_speed_seconds)

        return False

    def _solve_iteratively(self, i=0, j=0):
        to_visit = []
        to_visit.append((i, j))

        history_stack = []
        while to_visit:
            new_push = False
            i, j = to_visit.pop()
            cur_cell = self.cells[i][j]
            cur_cell.visited = True
            history_stack.append(cur_cell)
            if cur_cell == self.cells[-1][-1]:
                if self.win:
                    self.win.draw_move(
                        history_stack[-2],
                        cur_cell)
                    self.animate(self.solve_speed_seconds)
                return True

            if (i > 0 and not self.cells[i - 1][j].visited
                    and not self.cells[i][j].has_left):
                to_visit.append((i - 1, j))
                new_push = True

            if (j > 0 and not self.cells[i][j - 1].visited
                    and not self.cells[i][j].has_top):
                to_visit.append((i, j - 1))
                new_push = True

            if (i < len(self.cells) - 1 and not self.cells[i + 1][j].visited
                    and not self.cells[i][j].has_right):
                to_visit.append((i + 1, j))
                new_push = True

            if (j < len(self.cells[i]) - 1 and not self.cells[i][j + 1].visited
                    and not self.cells[i][j].has_bottom):
                to_visit.append((i, j + 1))
                new_push = True

            if self.win and len(history_stack) > 1 and new_push:
                prev_cell = history_stack[-2]
                self.win.draw_move(
                    cur_cell,
                    prev_cell
                )
                self.animate(self.solve_speed_seconds)
            if self.win and len(history_stack) > 1 and not new_push:
                found = False
                follow_cell = history_stack.pop()
                self.win.draw_move(
                    follow_cell,
                    history_stack[-1],
                    True)
                self.animate(self.solve_speed_seconds)
                if not to_visit:
                    return False
                next_i, next_j = to_visit[-1]

                while not found:
                    check_cell = history_stack.pop()
                    if (check_cell == self.cells[next_i - 1][next_j]
                            and not self.cells[next_i][next_j].has_left):
                        found = True
                    elif (check_cell == self.cells[next_i][next_j - 1]
                            and not self.cells[next_i][next_j].has_top):
                        found = True
                    elif (check_cell == self.cells[next_i + 1][next_j]
                            and not self.cells[next_i][next_j].has_right):
                        found = True
                    elif (check_cell == self.cells[next_i][next_j + 1]
                            and not self.cells[next_i][next_j].has_bottom):
                        found = True

                    self.win.draw_move(
                        follow_cell,
                        check_cell,
                        True)
                    self.animate(self.solve_speed_seconds)
                    follow_cell = check_cell
                history_stack.append(check_cell)

        return False
