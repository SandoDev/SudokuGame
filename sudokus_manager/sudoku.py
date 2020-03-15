from random import random


class Sudoku:

    def __init__(self):
        self.sudoku = []

    def inicializate_sudoku(self, value):
        for i in range(value):
            self.sudoku.append([0]*value)

    def print_sudoku(self):
        for f in range(len(self.sudoku)):
            for c in range(len(self.sudoku)):
                print("[", self.sudoku[f][c], "]", end="")
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

    def validate_number(self, num, grid, row, column):
        for f in range(len(grid)):
            for c in range(len(grid)):
                self.validate_block()
                self.validate_line()

    def validate_block(self):
        pass

    def validate_line(self, line: list):
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
