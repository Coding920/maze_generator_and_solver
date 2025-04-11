from window import Window
from drawed import Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(
        5, 5,
        15, 8,
        50, 50,
        win)
    win.wait_to_close()


main()
