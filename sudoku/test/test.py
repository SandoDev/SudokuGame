import unittest
from sudokus_manager.sudoku import Sudoku
from others.generate_sudoku_refactor import create_new_sudoku
from random import random
import random as rn
import numpy as np

class TestSudokuMethods(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()

    def test_validate_line(self):
        line = [2, 1, 4, 6, 7, 8, 3, 9, 5]  # Ok, correct line
        line2 = [2, 1, 4, 6, 8, 3, 9, 5] # Failure, incorrect quantity of numbers
        line3 = [2, 1, 4, 0, 7, 8, 3, 9, 5]  # Failure, line with zero
        line4 = [2, 2, 4, 6, 7, 8, 3, 9, 5, 1] # Failure, incorrect quantity of numbers
        line5 = [2, 1, 4, 6, 7, 8, 3, 9, 2]  # Failure, repeated numbers
        self.assertTrue(self.sudoku.validate_line(line))
        self.assertFalse(self.sudoku.validate_line(line2))
        self.assertFalse(self.sudoku.validate_line(line3))
        self.assertFalse(self.sudoku.validate_line(line4))
        self.assertFalse(self.sudoku.validate_line(line5))

    def test_blocks_to_line_1(self):
        """Tests that convert blocks to lines in a grid (list of lists)"""
        grid = self.sudoku.inicializate_sudoku(9)

        # Assigment especify values
        grid[0][0] = 1  # Block 1
        grid[1][1] = 2  # Block 1
        grid[2][2] = 3  # Block 1
        grid[5][5] = 9  # Block 5
        grid[7][4] = 7  # Block 8
        grid[6][6] = 7  # Block 9

        values_grid = (grid[0][0],
                       grid[1][1],
                       grid[2][2],
                       grid[5][5],
                       grid[7][4],
                       grid[6][6])

        # Transform blocks to lines
        line_blocks = self.sudoku.blocks_to_line(grid)

        values_blocks = (line_blocks[0][0],  # Block 1, Line 1
                         line_blocks[0][4],  # Block 1, Line 1
                         line_blocks[0][8],  # Block 1, Line 1
                         line_blocks[4][8],  # Block 5, Line 5
                         line_blocks[7][4],  # Block 8, Line 8
                         line_blocks[8][0],  # Block 9, Line 9
                         )

        # Compare some grid blocks with some lines of lines_blocks
        self.assertEqual(values_blocks, values_grid)

    def test_blocks_to_line_2(self):
        """Tests that convert blocks to lines in a grid (array of arrays)"""
        grid = self.sudoku.inicializate_sudoku(9)

        # Assigment especify values
        grid[0][0] = 1  # Block 1
        grid[1][1] = 2  # Block 1
        grid[2][2] = 3  # Block 1
        grid[5][5] = 9  # Block 5
        grid[7][4] = 7  # Block 8
        grid[6][6] = 7  # Block 9

        grid = np.transpose(grid)

        values_grid = (grid[0][0],
                       grid[1][1],
                       grid[2][2],
                       grid[5][5],
                       grid[7][4],
                       grid[6][6])

        # Transform blocks to lines
        line_blocks = self.sudoku.blocks_to_line(grid)

        values_blocks = (line_blocks[0][0],  # Block 1, Line 1
                         line_blocks[0][4],  # Block 1, Line 1
                         line_blocks[0][8],  # Block 1, Line 1
                         line_blocks[4][8],  # Block 5, Line 5
                         line_blocks[7][4],  # Block 8, Line 8
                         line_blocks[8][0],  # Block 9, Line 9
                         )

        # Compare some grid blocks with some lines of lines_blocks
        self.assertEqual(values_blocks, values_grid)

    def test_generate(self):
        """Tests a random number of times 
        that the generated number is between 0 and 8
        """
        cant_interations = int(random()*100)
        for i in range(cant_interations):
            number = self.sudoku.generate()  # Generate number
            self.assertGreaterEqual(number, 0)  # number >= 0
            self.assertLessEqual(number, 8)  # number <= 8

    def test_zero_different(self):
        """Tests a random number of times 
        that the generated number is between 1 and 9
        """
        cant_interations = int(random()*100)
        for i in range(cant_interations):
            number = self.sudoku.zero_different()  # Generate number
            self.assertGreaterEqual(number, 1)  # number >= 1
            self.assertLessEqual(number, 9)  # number <= 9

    def test_create_new_sudoku(self):
        for i in range(1000):
            sudo = create_new_sudoku(self.sudoku)
            self.assertTrue(self.sudoku.validate_grid(sudo))


if __name__ == '__main__':
    unittest.main()
