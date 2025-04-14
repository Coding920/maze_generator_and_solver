from window import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(
        5, 5,
        100, 100,
        7, 7,
        win, True)
    win.wait_to_close()


main()
