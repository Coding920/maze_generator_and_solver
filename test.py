import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )
        num_cols = 1
        num_rows = 53
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )
        num_cols = 43
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
