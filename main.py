from window import Window
from data import Line, Point


def main():
    win = Window(800, 600)
    p1 = Point(5, 5)
    p2 = Point(100, 100)
    line = Line(p1, p2)
    p1 = Point(250, 250)
    p2 = Point(600, 750)
    line2 = Line(p1, p2)
    win.draw_line(line, "black")
    win.draw_line(line2, "black")
    win.wait_to_close()


main()
