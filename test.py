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

    def test_break_enter_and_exit(self):
        m1 = Maze(0, 0, 1, 90, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1.cells[0][0].has_left
            or m1.cells[-1][-1].has_right
        )

        m1 = Maze(0, 0, 90, 1, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1.cells[0][0].has_left
            or m1.cells[-1][-1].has_right
        )

        m1 = Maze(0, 0, 1, 1, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1.cells[0][0].has_left
            or m1.cells[-1][-1].has_right
        )

        m1 = Maze(0, 0, 100, 100, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1.cells[0][0].has_left
            or m1.cells[-1][-1].has_right
        )

    def test_break_walls_r(self):
        m1 = Maze(0, 0, 100, 100, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    cell.has_left is False
                    or cell.has_right is False
                    or cell.has_top is False
                    or cell.has_bottom is False
                )

    def test_reset_visited(self):
        m1 = Maze(0, 0, 100, 100, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    not cell.visited
                )

    def test_solve(self):
        m1 = Maze(0, 0, 100, 100, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    m1.solve()
                )

        m1 = Maze(0, 0, 2, 2, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    m1.solve()
                )

        m1 = Maze(0, 0, 100, 1, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    m1.solve()
                )

        m1 = Maze(0, 0, 1, 100, 10, 10)
        m1.break_walls()
        for row in m1.cells:
            for cell in row:
                self.assertTrue(
                    m1.solve()
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
