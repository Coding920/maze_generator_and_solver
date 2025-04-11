from tkinter import Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=3
        )


class Cell:
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1.x, point1.y
        self.x2, self.y2 = point2.x, point2.y
        self.has_top = True
        self.has_bottom = True
        self.has_left = True
        self.has_right = True

    def draw(self, canvas: Canvas):
        if self.has_top:
            canvas.create_line(
                self.x1, self.y1, self.x2, self.y1, fill="black", width=2
            )
        if self.has_bottom:
            canvas.create_line(
                self.x1, self.y2, self.x2, self.y2, fill="black", width=2
            )
        if self.has_left:
            canvas.create_line(
                self.x1, self.y1, self.x1, self.y2, fill="black", width=2
            )
        if self.has_right:
            canvas.create_line(
                self.x2, self.y1, self.x2, self.y2, fill="black", width=2
            )

    def draw_move(self, canvas: Canvas, to_cell, undo=False):
        if undo:
            fill = "gray"
        else:
            fill = "red"

        self_center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        cell_center = Point((to_cell.x1 + to_cell.x2) / 2,
                            (to_cell.y1 + to_cell.y2) / 2)
        canvas.create_line(self_center.x, self_center.y,
                           cell_center.x, cell_center.y, fill=fill, width=3)
