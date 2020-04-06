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

    def blocks_to_line(self, grid):
        """
        Transform the blocks of 3*3 of grid in horizontal lines of 1*9 in a new grid

        Parameters:\n
        `grid` grid of 9*9 (list or array)\n

        Return:\n
        `list` list of list of 9*9 with the blocks of 3*3 of `grid` converted to lines of 1*9\n
        """
        blocks = self.inicializate_sudoku(9, 0)

        grid3 = int(len(grid)/3)
        grid6 = int(len(grid)-3)
        for f in range(len(grid)):
            for c in range(len(grid)):
                if f < grid3 and c < grid3:
                    blocks[0].append(grid[f][c])
                elif (f < grid3) and (c >= grid3 and c < grid6):
                    blocks[1].append(grid[f][c])
                elif f < grid3 and c >= grid6:
                    blocks[2].append(grid[f][c])
                elif (f >= grid3 and f < grid6) and c < grid3:
                    blocks[3].append(grid[f][c])
                elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6):
                    blocks[4].append(grid[f][c])
                elif (f >= grid3 and f < grid6) and c >= grid3:
                    blocks[5].append(grid[f][c])
                elif f >= grid6 and c < grid3:
                    blocks[6].append(grid[f][c])
                elif f >= grid6 and (c >= grid3 and c < grid6):
                    blocks[7].append(grid[f][c])
                elif f >= grid6 and c >= grid6:
                    blocks[8].append(grid[f][c])

        return blocks

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

    def zero_different(self, num=0):
        """
        Generate numbers between 1 and 9

        Parameters:\n
        `num` (optional) cadidate number to return\n

        Return:\n
        `int` number between 1 and 9
        """
        if num < 1 or num > 9:
            return self.zero_different(int(random()*10))
        else:
            return num

    def create_sudoku(self):
        columns = [9, 9, 9, 9, 9, 9, 9, 9, 9]

        for line, data in enumerate(self.sudoku):
            column = self.zero_different(int(random()*10))
            if columns[column - 1] == 1:
                for index, data2 in enumerate(columns):
                    if data2 == 9:
                        column = index + 1
                        break

            columns[column - 1] = 1
            print(column)
            self.number_assignment(column)

        # for f in range(len(self.sudoku)):
        #     for c in range(len(self.sudoku)):
        #         num = self.correct_number(
        #             self.zero_different(int(random()*10)), f, c)
        #         self.sudoku[f][c] = num
        #         #self.sudoku[f][c] = self.zero_different(int(random()*10))

    def generate(self):
        """
        Generate numbers between 0 and 8

        Return:\n
        `int` number between 0 and 8
        """
        generado = int(random()*10)
        if generado > 8:
            return self.generate()
        else:
            return generado

    def number_assignment(self, number: int):
        """Algorithm creator"""
        columns = [9, 9, 9, 9, 9, 9, 9, 9, 9]

        for line, data in enumerate(self.sudoku):
            column = self.generate()

            if columns[column] == 1:
                for index, data2 in enumerate(columns):
                    if data2 == 9:
                        column = index
                        break

            columns[column] = 1
            if not(number in self.sudoku[line]):
                if self.sudoku[line][column] == 0:
                    self.sudoku[line][column] = number
                else:
                    columns[column] = 9
                    for index2, data3 in enumerate(self.sudoku[line]):
                        if data3 == 0:
                            self.sudoku[line][index2] = 0
                            break

    # Old strategy for asign numbers to sudoku
    def old_correct_number(self, num, row, column):
        """Generate the correct number in that position

        Evaluates that the number is not repeated in that row,
        column or block; if it is repeated assign zero ## a new one that is not

        Parameters:\n
        `num` number to evaluate\n
        `row` row in which the number is\n
        `column` column in which the number is

        """
        rows = self.sudoku[row]
        sudoku_transpose = np.transpose(self.sudoku)
        columns = sudoku_transpose[column]
        current_block = [False, False, False, False,
                         False, False, False, False, False, ]
        blocks = []
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

        grid3 = int(len(self.sudoku)/3)
        grid6 = int(len(self.sudoku)-3)
        if row < grid3 and column < grid3:
            current_block[0] = True
        elif (row < grid3) and (column >= grid3 and column < grid6):
            current_block[1] = True
        elif row < grid3 and column >= grid6:
            current_block[2] = True
        elif (row >= grid3 and row < grid6) and column < grid3:
            current_block[3] = True
        elif (row >= grid3 and row < grid6) and (column >= grid3 and column < grid6):
            current_block[4] = True
        elif (row >= grid3 and row < grid6) and column >= grid3:
            current_block[5] = True
        elif row >= grid6 and column < grid3:
            current_block[6] = True
        elif row >= grid6 and (column >= grid3 and column < grid6):
            current_block[7] = True
        elif row >= grid6 and column >= grid6:
            current_block[8] = True

        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                if f < grid3 and c < grid3 and current_block[0]:
                    blocks.append(self.sudoku[f][c])
                elif (f < grid3) and (c >= grid3 and c < grid6) and current_block[1]:
                    blocks.append(self.sudoku[f][c])
                elif f < grid3 and c >= grid6 and current_block[2]:
                    blocks.append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and c < grid3 and current_block[3]:
                    blocks.append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and (c >= grid3 and c < grid6) and current_block[4]:
                    blocks.append(self.sudoku[f][c])
                elif (f >= grid3 and f < grid6) and c >= grid3 and current_block[5]:
                    blocks.append(self.sudoku[f][c])
                elif f >= grid6 and c < grid3 and current_block[6]:
                    blocks.append(self.sudoku[f][c])
                elif f >= grid6 and (c >= grid3 and c < grid6) and current_block[7]:
                    blocks.append(self.sudoku[f][c])
                elif f >= grid6 and c >= grid6 and current_block[8]:
                    blocks.append(self.sudoku[f][c])

        # print("SUDOKU-----------------")
        # self.print_sudoku(self.sudoku, 3)
        # print("FILAS-----------------")
        # print(rows)
        # print("COLUMNAS-----------------")
        # print(columns)
        # print("BLOQUES-----------------")
        # print(blocks)

        num_row = num in rows
        num_column = num in columns
        num_block = num in blocks

        counter_row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        counter_column = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        counter_block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for data in rows:
            counter_row[data-1] += 1

        for data in columns:
            counter_column[data-1] += 1

        for data in blocks:
            counter_block[data-1] += 1

        if num_row and num_column and num_block:
            return 0
            # print("Todas verdaderas")
            # print(num_row, num_column, num_block)
        elif num_row and num_column:
            return 0
            # print("solo fila y columna verdaderas")
            # print(num_row, num_column, num_block)
        elif num_column and num_block:
            return 0
            # print("solo bloque y columna verdaderas")
            # print(num_row, num_column, num_block)
        elif num_row and num_block:
            return 0
            # print("solo fila y bloque verdaderas")
            # print(num_row, num_column, num_block)
        elif num_row:
            return 0
            # print("solo fila verdadera")
            # print(num_row, num_column, num_block)
        elif num_column:
            return 0
            # print("solo columna verdadera")
            # print(num_row, num_column, num_block)
        elif num_block:
            return 0
            # print("solo bloque verdadera")
            # print(num_row, num_column, num_block)
        else:
            return num
            # print("Todas falsas")
            # print(num_row, num_column, num_block)

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

        # print("Horizontal: "+str(horizontal))
        # print("Vertical: "+str(vertical))
        # print("Bloques: "+str(block))

        horizontal_true = False
        vertical_true = False
        blocks_true = False
        for hori in horizontal:
            if hori == True:
                horizontal_true = True
            else:
                horizontal_true = False
                break

        for verti in vertical:
            if verti == True:
                vertical_true = True
            else:
                vertical_true = False
                break

        for blo in block:
            if blo == True:
                blocks_true = True
            else:
                blocks_true = False
                break

        if horizontal_true and vertical_true and blocks_true:
            # print("si si si, lo has logrado")
            return True
        else:
            # print("has fallado, sigue intentando")
            return False

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
