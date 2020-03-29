import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku
from random import random
import numpy as np


def generate_new_sudoku(sudo):
    """
    Generate new sudoku of 9x9
    """
    # define variables
    sudoku = sudo.inicializate_sudoku(9)
    values = sudo.inicializate_sudoku(9)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    discarded = []
    blocked = []
    partially_blocked = []

    # fill the grid values
    for index, row in enumerate(values):
        values[index] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # principal for
    for i in range(9):  # una por cada numero diferente en un sudoku
        number = random_in_list(numbers)
        numbers.remove(number)
        blocked = []
        for row in range(9):  # una por cada FILA del sudoku
            column = random_in_list(values[row])
            if row == 0:
                partially_blocked = []
            elif row == 3:
                partially_blocked = []
            elif row == 6:
                partially_blocked = []

            print("print partially_blocked: ", partially_blocked)

            if column not in discarded and column not in blocked and column not in partially_blocked:
                blocked.append(column)
                if column < 3:
                    for partially in range(0, 3):
                        if partially != column:
                            partially_blocked.append(partially)
                elif column >= 3 and column < 6:
                    for partially in range(3, 6):
                        if partially != column:
                            partially_blocked.append(partially)
                elif column > 5:
                    for partially in range(6, 9):
                        if partially != column:
                            partially_blocked.append(partially)
                values[row].remove(column)

                # assigning the number to sudoku
                sudoku[row][column] = number
            else:
                for value in values[row]:
                    column = value
                    if column not in discarded and column not in blocked and column not in partially_blocked:
                        blocked.append(column)
                        if column < 3:
                            for partially in range(0, 3):
                                if partially != column:
                                    partially_blocked.append(partially)
                        elif column >= 3 and column < 6:
                            for partially in range(3, 6):
                                if partially != column:
                                    partially_blocked.append(partially)
                        elif column > 5:
                            for partially in range(6, 9):
                                if partially != column:
                                    partially_blocked.append(partially)
                        values[row].remove(column)

                        # assigning the number to sudoku
                        sudoku[row][column] = number
                        break
                    elif (column in discarded or column in blocked or column in partially_blocked) and column == values[row][len(values[row])-1]:

                        # descartar la COLUMNA utilizada en la iteración anterior de este NUMERO
                        # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1

                        # assigning the number to sudoku
                        sudoku[row][column] = 0

            print("print row: ", row)
            print("print column: ", column)
            print("print number: ", number)
            print("print blocked: ", blocked)
            print("print partially_blocked: ", partially_blocked)
            print("print discarded: ", discarded)
            print("print numbers: ", numbers)
            print("-----print values-----")
            for value in values:
                print(value)
            print("-----print sudoku-----")
            sudo.print_sudoku(sudoku)

            print()

    return sudoku


def random_in_list(values: list):
    """Generate a random number in a list [0,9]"""
    if values == None:
        print(values, " ¿una lista vacia?, ¿enserio?")
    number = int(random()*10)
    if number not in values:
        return random_in_list(values)
    else:
        return number


# Principal main
if __name__ == "__main__":
    sudoku = Sudoku()
    sus = generate_new_sudoku(sudoku)
    sudoku.validate_grid(sus)
