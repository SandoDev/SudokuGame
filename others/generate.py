import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku
import numpy as np
from random import random


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
        row = 0
        while row <= 8:  # una por cada FILA del sudoku
            column = random_in_list(values[row])
            if row == 0:
                partially_blocked = []
            elif row == 3:
                partially_blocked = []
            elif row == 6:
                partially_blocked = []

            print("print partially_blocked: ", partially_blocked)

            if column not in discarded and \
                    column not in blocked and \
                    column not in partially_blocked:

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
                discarded = []
            else:
                for value in values[row]:
                    column = value
                    if column not in discarded and \
                            column not in blocked and \
                            column not in partially_blocked:

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
                        discarded = [] # Limpio descartados
                        break
                    elif (column in discarded or
                          column in blocked or
                          column in partially_blocked) and \
                            column == values[row][len(values[row])-1]:

                        column_discared = discarded_column(row, number, sudoku)
                        #discarded=[]#toca crear matriz para descartar por filas
                        discarded.append(column_discared) # descartar la COLUMNA utilizada en la iteración anterior de este NUMERO,,,,,hay que limpiar a discared aqui
                        sudoku[row-1][column_discared]=0 # Limpiar la pocisión del sudoku
                        blocked.remove(column_discared) # Limpiar el dato de los bloqueados
                        values[row-1].append(column_discared)
                        # Limpiar de los parcialmente bloqueados
                        if column_discared < 3:
                            for partially in range(0, 3):
                                if partially != column_discared:
                                    try:
                                        partially_blocked.remove(partially)
                                    except:
                                        pass
                        elif column_discared >= 3 and column_discared < 6:
                            for partially in range(3, 6):
                                if partially != column_discared:
                                    try:
                                        partially_blocked.remove(partially)
                                    except:
                                        pass
                        elif column_discared > 5:
                            for partially in range(6, 9):
                                if partially != column_discared:
                                    try:
                                        partially_blocked.remove(partially)
                                    except:
                                        pass

                        row -= 2 # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                        break

            row += 1

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


def discarded_column(current_row, current_number, grid):
    column_discared = 99
    for index, value in enumerate(grid[current_row-1]):
        if value == current_number:
            column_discared = index
            break
    return column_discared


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
