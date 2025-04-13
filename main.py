from window import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(
        5, 5,
        20, 20,
        35, 35,
        win, False)
    win.wait_to_close()


main()
