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
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, coordinates: tuple[Point, Point]):
        self.x1, self.y1 = coordinates[0].x, coordinates[0].y
        self.x2, self.y2 = coordinates[1].x, coordinates[1].y
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
