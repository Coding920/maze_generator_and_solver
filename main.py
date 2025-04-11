from window import Window
from drawed import Point, Line, Cell


def main():
    win = Window(800, 800)
    p1 = Point(5, 5)
    p2 = Point(755, 755)
    p3 = Point(400, 400)
    p4 = Point(600, 600)
    cell = Cell((p1, p2))
    cell2 = Cell((p1, p3))
    win.draw_cell(cell)
    win.draw_cell(cell2)
    line = Line(p1, p3)
    line2 = Line(p2, p4)
    win.draw_line(line, "red")
    win.draw_line(line2, "red")
    win.wait_to_close()


main()
