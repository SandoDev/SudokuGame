from timeit import default_timer
import numpy as np
from random import random
import sys
sys.path.append('./')
from sudoku.sudoku import Sudoku


def principal_algorithm(sudo):
    """
    Generate new sudoku of 9x9.\n
    This algorithm has a 61% probability of generating a sudoku correctly\n
    The average speed of execution of 1000 sudokus is 3 seconds on a machine with standard resources
    
    Parameters
    ----------
        sudo: instance of class Sudoku()

    Retunrs
    ----------
        sudoku: list
            list with new sudoku of 9x9

    """
    # define variables
    sudoku = sudo.inicializate_sudoku(9)
    values = sudo.inicializate_sudoku(9)
    discarded = sudo.inicializate_sudoku(9)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dictionary_memory = {'1': [],
                         '2': [],
                         '3': [],
                         '4': [],
                         '5': [],
                         '6': [],
                         '7': [],
                         '8': [],
                         '9': []}

    blocked = []
    partially_blocked = []
    past_number = []

    # fill the grid values
    for index, row in enumerate(values):
        values[index] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        discarded[index] = []

    # principal while
    while len(numbers) != 0:  # una por cada numero diferente en un sudoku
        
        number = random_in_list(numbers)
        past_number.append(number)  # el pasado es el ultimo indice -1
        numbers.remove(number)
        blocked = []
        row = 0
        for index in range(9):
            discarded[index] = []
        
        while row <= 8:  # una por cada FILA del sudoku
            column = random_in_list(values[row])
            if row == 0:
                partially_blocked = []
                if column in dictionary_memory[str(number)]:
                    column = random_in_list(values[row],dictionary_memory[str(number)])
                    if column == 99:
                        #print("las listas son iguales :'( ")
                        break
                        numbers.append(number)
                        current_num = number
                        number = past_number[-2]  # 2
                        past_number.remove(current_num)
                        row = 8
                        for past_row in range(9):
                            blocked.append(discarded_column(
                                past_row+1, number, sudoku))

                        column_discared = discarded_column(
                            row+1, number, sudoku)
                        # TODO discareded necesita ser dictionary para asociar las pocisiones descartadas a un numero
                        discarded[row] = []
                        discarded[row].append(column_discared)
                        dictionary_memory[str(number)].append(column_discared)
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

                        #row -= 1  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                        continue

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

            if row == 8 and column in dictionary_memory[str(number)]:
                #print("revisaaaar")
                column_discared = discarded_column(
                    row, number, sudoku)
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

                row -= 1  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                continue

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

                        if row-1 == 0:
                            dictionary_memory[str(number)].append(discarded_column(row, number, sudoku))
                            # agregar esa columna a la memoria del numero
                            # de tal forma que ese numero no pueda volver
                            # a ser asignado a esa columna

                        if row == 0:
                            numbers.append(number)
                            current_num = number
                            number = past_number[-2]  # 2
                            past_number.remove(current_num)
                            row = 8
                            for past_row in range(9):
                                blocked.append(discarded_column(
                                    past_row+1, number, sudoku))

                            column_discared = discarded_column(
                                row+1, number, sudoku)
                            # TODO discareded necesita ser dictionary para asociar las pocisiones descartadas a un numero
                            discarded[row] = []
                            discarded[row].append(column_discared)
                            dictionary_memory[str(number)].append(column_discared)
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
                            column_discared = discarded_column(
                                row, number, sudoku)
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

            # print("print row: ", row)
            # print("print column: ", column)
            # print("print number: ", number)
            # print("print blocked: ", blocked)
            # print("print partially_blocked: ", partially_blocked)
            # print("print numbers: ", numbers)
            # print("print memory_dict: ", dictionary_memory)
            # print("-----print discarded-----")
            # for value in discarded:
            #     print(value)
            # print("-----print values-----")
            # for value in values:
            #     print(value)
            # print("-----print sudoku-----")
            # sudo.print_sudoku(sudoku)

            # print()

    return sudoku


def discarded_column(current_row, current_number, grid):
    column_discared = 99
    for index, value in enumerate(grid[current_row-1]):
        if value == current_number:
            column_discared = index
            break
        if column_discared == 99 and index == len(grid[current_row-1])-1:
            print("noooooo. error")

    return column_discared


def random_in_list(values: list, excludes_memory=[]):
    """Generate a random number in a list [0,9]"""

    if values == excludes_memory:
        return 99

    if values == None:
        print(values, " ¿una lista vacia?, ¿enserio?")
    number = int(random()*10)
    if number not in values or number in excludes_memory:
        return random_in_list(values, excludes_memory)
    else:
        return number


# Principal main
def create_new_sudoku():
    sudoku = Sudoku()
    valor = False

    conteo_buenas = 0
    conteo_malas = 0

    ini_time = default_timer()
    end_time = 0

    while not valor:
        sus = principal_algorithm(sudoku)
        valor = sudoku.validate_grid(sus)
        
    
    #----------------------------------------------------
    # for i in range(1000):
    #     sus = generate_new_sudoku(sudoku)
    #     valor = sudoku.validate_grid(sus)
    #     if valor:
    #         conteo_buenas += 1
    #     else:
    #         conteo_malas += 1
    #----------------------------------------------------
    end_time = default_timer()
    print(end_time-ini_time,"/",conteo_buenas,"/",conteo_malas)
    return sus


# Principal main
if __name__ == "__main__":
    sudoku = Sudoku()
    valor = False

    conteo_buenas = 0
    conteo_malas = 0

    ini_time = default_timer()
    end_time = 0

    # while not valor:
    #     sus = principal_algorithm(sudoku)
    #     valor = sudoku.validate_grid(sus)

    # ----------------------------------------------------
    for i in range(1000):
        sus = principal_algorithm(sudoku)
        valor = sudoku.validate_grid(sus)
        if valor:
            conteo_buenas += 1
        else:
            conteo_malas += 1
    # ----------------------------------------------------
    end_time = default_timer()
    print(end_time-ini_time, "/", conteo_buenas, "/", conteo_malas)