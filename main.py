from window import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(
        5, 5,
        100, 100,
        5, 5,
        win)
    print("!")
    win.wait_to_close()


main()
