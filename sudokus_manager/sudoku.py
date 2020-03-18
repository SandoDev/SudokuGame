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
                num = self.correct_number(
                    self.zero_different(int(random()*10)), f, c)
                self.sudoku[f][c] = num

    def correct_number(self, num, row, column):
        """Generate the correct number in that position

        Evaluates that the number is not repeated in that row, 
        column or block; if it is repeated assign a new one that is not

        Parameters:\n
        `num` number to evaluate\n
        `row` row in which the number is\n
        `column` column in which the number is

        """
        rows = []
        columns = []
        blocks = self.inicializate_sudoku(9, 0)
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

        for line in self.sudoku:
            rows.append(line)
            columns.append(np.transpose(line))

        grid3 = int(len(self.sudoku)/3)
        grid6 = int(len(self.sudoku)-3)
        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                if f < grid3 and c < grid3:
                    blocks[0].append(self.sudoku[f][c])
                elif (f < grid3) and (c >= grid3 and c < grid6):
                    blocks[1].append(self.sudoku[f][c])
                elif f < grid3 and c >= grid6:
                    blocks[2].append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and c < grid3:
                    blocks[3].append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
                    blocks[4].append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and c >= grid3:
                    blocks[5].append(self.sudoku[f][c])
                elif f >= grid6 and c < grid3:
                    blocks[6].append(self.sudoku[f][c])
                elif f >= grid6 and (c >= grid3 and c < grid6):
                    blocks[7].append(self.sudoku[f][c])
                elif f >= grid6 and c >= grid3:
                    blocks[8].append(self.sudoku[f][c])

        print("SUDOKU-----------------")
        self.print_sudoku(self.sudoku, 3)
        print("FILAS-----------------")
        self.print_sudoku(rows, 1)
        print("COLUMNAS-----------------")
        self.print_sudoku(columns, 2)
        print("BLOQUES-----------------")
        self.print_sudoku(blocks, 1)
        if not ((num in rows) and (num in columns) and (num in blocks)):
            return num
        else:
            return 0

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

        # self.print_sudoku(lines_of_blocks, 1)

        for index, line in enumerate(lines_of_blocks):
            block[index] = self.validate_line(list(line))

        print("Horizontal: "+str(horizontal))
        print("Vertical: "+str(vertical))
        print("Bloques: "+str(block))

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

    def fix_blocks_pseudo(self, grid):
        self.print_sudoku(grid, 3)
        # lines_of_blocks = grid

        # for index, line in enumerate(lines_of_blocks):
        #     lines_of_blocks[index] = self.create_block(line)

        # print("lines of blocks")
        # self.print_sudoku(lines_of_blocks, 1)

        block1 = self.create_block(grid[0])
        block2 = self.create_block(grid[1])
        block3 = self.create_block(grid[2])
        block4 = self.create_block(grid[3])
        block5 = self.create_block(grid[4])
        block6 = self.create_block(grid[5])
        block7 = self.create_block(grid[6])
        block8 = self.create_block(grid[7])
        block9 = self.create_block(grid[8])

        print(block1)
        print(block2)
        print(block3)
        print(block4)
        print(block5)
        print(block6)
        print(block7)
        print(block8)
        print(block9)

        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 0
        contador5 = 0
        contador6 = 0
        contador7 = 0
        contador8 = 0
        contador9 = 0

        grid3 = int(len(grid)/3)
        grid6 = int(len(grid)-3)

        for f, da in enumerate(grid):
            for c, dat in enumerate(grid):
                if ((f < grid3) and (c < grid3)):
                    grid[f][c] = block1[contador1]
                    contador1 += 1

        # for f, da in enumerate(grid):
        #     for c, dat in enumerate(grid):
        #         if ((f < grid3) and (c >= grid3 and c < grid6)):
        #             grid[f][c] = block2[contador2]
        #             contador2 += 1

        # for f, da in enumerate(grid):
        #     for c, dat in enumerate(grid):
        #         if ((f < grid3) and (c >= grid6)):
        #             grid[f][c] = block3[contador3]
        #             contador3 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if (f >= grid3 and f < grid6) and c < grid3:
                    grid[f][c] = block4[contador4]
                    contador4 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
                    grid[f][c] = block5[contador5]
                    contador5 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if (f >= grid3 and f < grid6) and c >= grid6:
                    grid[f][c] = block6[contador6]
                    contador6 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if f >= grid6 and c < grid3:
                    grid[f][c] = block7[contador7]
                    contador7 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if f >= grid6 and (c >= grid3 and c < grid6):
                    grid[f][c] = block8[contador8]
                    contador8 += 1

        for f in range(len(grid)):
            for c in range(len(grid)):
                if f >= grid6 and c >= grid6:
                    grid[f][c] = block9[contador9]
                    contador9 += 1

        return grid

    def line_to_block(self, line: list) -> list:
        block = self.inicializate_sudoku(3, 0)
        block[0].append(line[:3])
        block[1].append(line[3:6])
        block[2].append(line[6:])
        return block

    def fix_vertical_pseudo(self):
        sudoku_transpose = np.transpose(self.sudoku)

        # Of Array to list
        sudoku_transpose = list(sudoku_transpose)
        for index, line in enumerate(sudoku_transpose):
            sudoku_transpose[index] = list(line)

        # create correct block
        for index, line in enumerate(sudoku_transpose):
            sudoku_transpose[index] = self.create_block(line)
        self.sudoku = np.transpose(sudoku_transpose)

        # Of Array to list
        self.sudoku = list(self.sudoku)
        for index, line in enumerate(self.sudoku):
            self.sudoku[index] = list(line)

    def fix_horizontal_pseudo(self):
        for index, line in enumerate(self.sudoku):
            self.sudoku[index] = self.create_block(line)

        # lines_of_blocks = self.inicializate_sudoku(9, 0)

        # for f in range(len(self.sudoku)):
        #     for c in range(len(self.sudoku)):
        #         grid3 = int(len(self.sudoku)/3)
        #         grid6 = int(len(self.sudoku)-3)
        #         if f < grid3 and c < grid3:
        #             lines_of_blocks[0].append(self.sudoku[f][c])
        #         elif (f < grid3) and (c >= grid3 and c < grid6):
        #             lines_of_blocks[1].append(self.sudoku[f][c])
        #         elif f < grid3 and c >= grid6:
        #             lines_of_blocks[2].append(self.sudoku[f][c])
        #         elif (f >= grid3 and f < grid6) and c < grid3:
        #             lines_of_blocks[3].append(self.sudoku[f][c])
        #         elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
        #             lines_of_blocks[4].append(self.sudoku[f][c])
        #         elif (f >= grid3 and f < grid6) and c >= grid3:
        #             lines_of_blocks[5].append(self.sudoku[f][c])
        #         elif f >= grid6 and c < grid3:
        #             lines_of_blocks[6].append(self.sudoku[f][c])
        #         elif f >= grid6 and (c >= grid3 and c < grid6):
        #             lines_of_blocks[7].append(self.sudoku[f][c])
        #         elif f >= grid6 and c >= grid3:
        #             lines_of_blocks[8].append(self.sudoku[f][c])

        # for index, line in enumerate(self.sudoku):
        #     self.sudoku[index] = self.create_block(line)

        # grid3 = int(len(self.sudoku)/3)
        # grid6 = int(len(self.sudoku)-3)
        # for f in range(len(self.sudoku)):
        #     contador = 0
        #     for c in range(len(self.sudoku)):
        #         if f < grid3 and c < grid3:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif (f < grid3) and (c >= grid3 and c < grid6):
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif f < grid3 and c >= grid6:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif (f >= grid3 and f < grid6) and c < grid3:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif (f >= grid3 and f < grid6) and c >= grid3:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif f >= grid6 and c < grid3:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif f >= grid6 and (c >= grid3 and c < grid6):
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1
        #         elif f >= grid6 and c >= grid3:
        #             self.sudoku[f][c] = lines_of_blocks[f][contador]
        #             contador += 1

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

        # print("block2: " + str(block))
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
