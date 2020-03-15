from random import random
import numpy as np
from colorama import init
from colorama import Fore, Back, Style


class Sudoku:

    def __init__(self, size=9):
        self.sudoku = self.inicializate_sudoku(size)
        init()

    def inicializate_sudoku(self, rows, columns=9):
        grid = []
        for i in range(rows):
            grid.append([0]*columns)

        return grid

    def print_sudoku(self, grid, styles=3):
        """styles = 1: Horizontal\n
        styles = 2: Vertical\n
        styles = 3: Bloques\n
        """
        if styles == 3:
            for f in range(len(grid)):
                for c in range(len(grid)):
                    grid3 = int(len(grid)/3)
                    grid6 = int(len(grid)-3)
                    if f < grid3 and c < grid3:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    elif (f < grid3) and (c >= grid3 and c < grid6):
                        print("[", grid[f][c], "]", end="")
                    elif f < grid3 and c >= grid6:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    elif (f >= grid3 and f < grid6) and c < grid3:
                        print("[", grid[f][c], "]", end="")
                    elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    elif (f >= grid3 and f < grid6) and c >= grid3:
                        print("[", grid[f][c], "]", end="")
                    elif f >= grid6 and c < grid3:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    elif f >= grid6 and (c >= grid3 and c < grid6):
                        print("[", grid[f][c], "]", end="")
                    elif f >= grid6 and c >= grid3:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                print()
        elif styles == 1:
            for f in range(len(grid)):
                for c in range(len(grid)):
                    if f % 2 == 0:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    else:
                        print("[", grid[f][c], "]", end="")
                print()
        elif styles == 2:
            for f in range(len(grid)):
                for c in range(len(grid)):
                    if c % 2 == 0:
                        print(Back.WHITE + Fore.BLACK +
                              "[", grid[f][c], "]", end="")
                        print(Style.RESET_ALL, end="")
                    else:
                        print("[", grid[f][c], "]", end="")
                print()
        else:
            for f in range(len(grid)):
                for c in range(len(grid)):
                    print("[", grid[f][c], "]", end="")
                print()

    def zero_different(self, num):
        if num == 0:
            return self.zero_different(int(random()*10))
        else:
            return num

    def create_sudoku(self):
        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                # self.validate_number(zero_different(int(random()*10)),self.sudoku,f,c)
                self.sudoku[f][c] = self.zero_different(int(random()*10))

    def validate_grid(self, grid: list):
        vertical = [False, False, False, False,
                    False, False, False, False, False]
        horizontal = [False, False, False, False,
                      False, False, False, False, False]
        block = [False, False, False, False,
                 False, False, False, False, False]

        for index, row in enumerate(grid):
            horizontal[index] = self.validate_line(list(row))

        grid_transpose = np.transpose(grid)

        for index, column in enumerate(grid_transpose):
            vertical[index] = self.validate_line(list(column))

        lines_of_blocks = self.inicializate_sudoku(9, 0)

        for f in range(len(grid)):
            for c in range(len(grid)):
                if f < int(len(grid)/3) and c < int(len(grid)/3):
                    lines_of_blocks[0].append(grid[f][c])
                elif (f < int(len(grid)/3)) and (c >= int(len(grid)/3) and c < int(len(grid)-3)):
                    lines_of_blocks[1].append(grid[f][c])
                elif f < int(len(grid)/3) and c >= int(len(grid)-3):
                    lines_of_blocks[2].append(grid[f][c])
                elif (f >= int(len(grid)/3) and f < int(len(grid)-3)) and c < int(len(grid)/3):
                    lines_of_blocks[3].append(grid[f][c])
                elif (f >= int(len(grid)/3) and f < int(len(grid)-3)) and (c >= int(len(grid)/3) and c < int(len(grid)-3)):
                    lines_of_blocks[4].append(grid[f][c])
                elif (f >= int(len(grid)/3) and f < int(len(grid)-3)) and c >= int(len(grid)/3):
                    lines_of_blocks[5].append(grid[f][c])
                elif f >= int(len(grid)-3) and c < int(len(grid)/3):
                    lines_of_blocks[6].append(grid[f][c])
                elif f >= int(len(grid)-3) and (c >= int(len(grid)/3) and c < int(len(grid)-3)):
                    lines_of_blocks[7].append(grid[f][c])
                elif f >= int(len(grid)-3) and c >= int(len(grid)/3):
                    lines_of_blocks[8].append(grid[f][c])

        self.print_sudoku(lines_of_blocks, 1)

        for index, line in enumerate(lines_of_blocks):
            block[index] = self.validate_line(list(line))

        print(horizontal)
        print(vertical)
        print(block)

    def validate_line(self, line: list):
        """Validate a line of numbers

        Return true if a line of numbers has all and alone
        the values of the one to nine

        Example: [1,2,3,4,5,6,7,9,8]

        Parameters:\n
        line: list with numbers

        """
        contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        for num in line:
            if num in nums:
                contadores[num-1] += 1

        for cont in contadores:
            if cont != 1:
                return False

        return True

    def validate_sudoku(self):
        block = []
        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                if f < int(len(self.sudoku)/3) and c < int(len(self.sudoku)/3):
                    block.append(self.sudoku[f][c])

        print("block1: " + str(block))
        block = self.create_block(block)
        print("block3: " + str(block))

        contador = 0
        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                if f < int(len(self.sudoku)/3) and c < int(len(self.sudoku)/3):
                    self.sudoku[f][c] = block[contador]
                    contador += 1

    def create_block(self, block: list):
        contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        firts = [False, False, False, False, False, False, False, False, False]
        for num in block:
            if num in nums:
                contadores[num-1] += 1

        # Second state for the list
        """firts estate = [1,2,3,2,3,4,5]
            second state = [1,2,3,0,0,4,5]
        """
        for index, num in enumerate(block):
            if contadores[num-1] > 1 and firts[num-1]:
                block[index] = 0
            elif contadores[num-1] > 1:
                firts[num-1] = True

        print("block2: " + str(block))
        contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for num in block:
            if num in nums:
                contadores[num-1] += 1

        # Second state for the list
        """second state = [1,2,3,0,0,4,5]
            third state = [1,2,3,6,7,4,5]
        """
        for index, num in enumerate(contadores):
            if num == 0:
                value = True
                for indicator, data in enumerate(block):
                    if data == 0 and value:
                        block[indicator] = nums[index]
                        value = False

        return block
