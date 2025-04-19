from window import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(
        5, 5,
        50, 50,
        15, 15,
        win, True)
    win.wait_to_close()


main()
