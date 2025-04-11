from window import Window
from drawed import Point, Line, Cell


def main():
    win = Window(800, 800)
    p1 = Point(5, 5)
    p2 = Point(400, 400)
    p3 = Point(400, 5)
    p4 = Point(755, 400)
    cell = Cell(p1, p2)
    cell2 = Cell(p3, p4)
    win.draw_cell(cell)
    win.draw_cell(cell2)
    win.draw_move(cell, cell2, undo=False)
    win.wait_to_close()


main()
