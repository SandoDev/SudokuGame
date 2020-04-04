from random import random
import numpy as np
import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku


def generate_new_sudoku(sudo):
    """
    Generate new sudoku of 9x9
    """
    # define variables
    sudoku = sudo.inicializate_sudoku(9)
    values = sudo.inicializate_sudoku(9)
    discarded = sudo.inicializate_sudoku(9)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    blocked = []
    partially_blocked = []
    past_number = []

    # fill the grid values
    for index, row in enumerate(values):
        values[index] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        discarded[index] = []

    # principal for
    while len(numbers) != 0:  # una por cada numero diferente en un sudoku
    #for i in range(6):  # una por cada numero diferente en un sudoku
        number = random_in_list(numbers)
        past_number.append(number)  # el pasado es el ultimo indice -1
        numbers.remove(number)
        blocked = []
        for index in range(9):
            discarded[index] = []
        row = 0
        while row <= 8:  # una por cada FILA del sudoku
            column = random_in_list(values[row])
            if row == 0:
                partially_blocked = []
            elif row == 3:
                partially_blocked = []
            elif row == 6:
                partially_blocked = []

            if row == 5 or row == 2 or row == 8:
                # toca ir a la fila anterior buscar el numero y bloquear sus adyacentes
                for_partially_bloqued = [99, 99]
                for_partially_bloqued[0] = discarded_column(
                    row, number, sudoku)
                for_partially_bloqued[1] = discarded_column(
                    row-1, number, sudoku)
                for value_discarded in for_partially_bloqued:
                    if value_discarded < 3:
                        for partially in range(0, 3):
                            if partially != value_discarded:
                                partially_blocked.append(partially)
                    elif value_discarded >= 3 and value_discarded < 6:
                        for partially in range(3, 6):
                            if partially != value_discarded:
                                partially_blocked.append(partially)
                    elif value_discarded > 5:
                        for partially in range(6, 9):
                            if partially != value_discarded:
                                partially_blocked.append(partially)

            if column not in discarded[row] and \
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
                #discarded[row] = []
            else:
                for value in values[row]:
                    column = value
                    if column not in discarded[row] and \
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
                        # discarded[row] = [] # Limpio descartados
                        break
                    elif (column in discarded[row] or
                          column in blocked or
                          column in partially_blocked) and \
                            column == values[row][len(values[row])-1]:

                        if row == 0:
                            numbers.append(number)
                            current_num = number
                            number = past_number[-2] #2
                            past_number.remove(current_num)
                            row = 8
                            for past_row in range(9):
                                blocked.append(discarded_column(past_row+1, number, sudoku))

                            column_discared = discarded_column(row+1, number, sudoku)
                            discarded[row] = [] # TODO discareded necesita ser dictionary para asociar las pocisiones descartadas a un numero
                            discarded[row].append(column_discared)
                            sudoku[row][column_discared] = 0
                            values[row].append(column_discared)
                            blocked.remove(column_discared)
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

                            row -= 1  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                            break                          
                        else:
                            column_discared = discarded_column(row, number, sudoku)
                            discarded[row] = []
                            # descartar la COLUMNA utilizada en la iteración anterior de este NUMERO
                            discarded[row-1].append(column_discared)
                            # Limpiar la pocisión del sudoku
                            sudoku[row-1][column_discared] = 0
                            values[row-1].append(column_discared)

                            # Limpiar el dato de los bloqueados
                            blocked.remove(column_discared)

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

                            row -= 2  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                            break

            row += 1

            print("print row: ", row)
            print("print column: ", column)
            print("print number: ", number)
            print("print blocked: ", blocked)
            print("print partially_blocked: ", partially_blocked)
            print("print numbers: ", numbers)
            print("-----print discarded-----")
            for value in discarded:
                print(value)
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
