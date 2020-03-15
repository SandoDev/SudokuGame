import unittest
from sudokus_manager.sudoku import Sudoku


class TestSudokuMethods(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()

    def test_validate_line(self):
        line = [2, 1, 4, 6, 7, 8, 3, 9, 5]  # Ok, correct line
        # line = [2, 1, 4, 6, 8, 3, 9, 5] # Failure, incorrect quantity of numbers
        # line = [2, 1, 4, 0, 7, 8, 3, 9, 5]  # Failure, line with zero
        # line = [2, 2, 4, 6, 7, 8, 3, 9, 5, 1] # Failure, incorrect quantity of numbers
        # line = [2, 1, 4, 6, 7, 8, 3, 9, 2]  # Failure, repeated numbers
        self.assertEqual(self.sudoku.validate_line(line), True)

    def test_validate_block(self):
        self.sudoku.create_sudoku()
        self.sudoku.validate_grid(self.sudoku.sudoku)


if __name__ == '__main__':
    unittest.main()
