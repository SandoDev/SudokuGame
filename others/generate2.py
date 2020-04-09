import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku
from random import random
import numpy as np
from timeit import default_timer


def generate_new_sudoku(sudo):
    """
    Generate new sudoku of 9x9.\n
    This algorithm has a 85% probability of generating a sudoku correctly\n
    The average speed of execution of 1000 sudokus is 6 seconds on a machine with standard resources
    
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
    discarded = sudo.inicializate_sudoku(9)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    values = sudo.inicializate_sudoku(9)
    blockeds = []
    partially_blockeds = []
    past_number = []
    dictionary_memory = {
        '1': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '2': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '3': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '4': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '5': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '6': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '7': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '8': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []},
        '9': {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}
    }
    dictionary_memory_aux = dictionary_memory
    counter_memories=0

    # fill the grid values
    for index, row in enumerate(values):
        values[index] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        discarded[index] = []

    # principal for
    while len(numbers) != 0:  # una por cada numero diferente en un sudoku
        number = random_in_list2(numbers)
        past_number.append(number)  # el pasado es el ultimo indice -1
        numbers.remove(number)
        blockeds = []

        for index in range(9):
            discarded[index] = []

        row = 0
        while row <= 8:  # una por cada FILA del sudoku
            if row == 0:
                partially_blockeds = []
            elif row == 3:
                partially_blockeds = []
            elif row == 6:
                partially_blockeds = []

            column = random_in_list(
                values[row], blockeds, partially_blockeds, discarded[row], dictionary_memory[str(number)][str(row)])

            if column < 3:
                for partially in range(0, 3):
                    if partially != column:
                        partially_blockeds.append(partially)
            elif column >= 3 and column < 6:
                for partially in range(3, 6):
                    if partially != column:
                        partially_blockeds.append(partially)
            elif column > 5:
                for partially in range(6, 9):
                    if partially != column:
                        partially_blockeds.append(partially)

            if column == 99:
                if row == 0:
                    counter_memories += 1
                    if counter_memories > 10:
                        dictionary_memory = dictionary_memory_aux
                        break
                        
                    numbers.append(number)
                    current_num = number
                    number = past_number[-2]  # 2
                    past_number.remove(current_num)
                    row = 8
                    for past_row in range(9):
                        blockeds.append(discarded_column(
                            past_row+1, number, sudoku))

                    column_discared = discarded_column(
                        row+1, number, sudoku)
                    # TODO discareded necesita ser dictionary para asociar las pocisiones descartadas a un numero
                    discarded[row] = []
                    discarded[row].append(column_discared)
                    dictionary_memory[str(number)][str(row)].append(column_discared)
                    sudoku[row][column_discared] = 0
                    values[row].append(column_discared)
                    blockeds.remove(column_discared)
                    # Limpiar de los parcialmente bloqueados
                    if column_discared < 3:
                        for partially in range(0, 3):
                            if partially != column_discared:
                                try:
                                    partially_blockeds.remove(partially)
                                except:
                                    pass
                    elif column_discared >= 3 and column_discared < 6:
                        for partially in range(3, 6):
                            if partially != column_discared:
                                try:
                                    partially_blockeds.remove(partially)
                                except:
                                    pass
                    elif column_discared > 5:
                        for partially in range(6, 9):
                            if partially != column_discared:
                                try:
                                    partially_blockeds.remove(partially)
                                except:
                                    pass

                    #row -= 1  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                    # print("print row: ", row)
                    # print("print column: ", column)
                    # print("print number: ", number)
                    # print("print blocked: ", blockeds)
                    # print("print partially_blocked: ", partially_blockeds)
                    # print("print numbers: ", numbers)
                    # print("-----print values-----")
                    # for value in values:
                    #     print(value)
                    # print("-----print sudoku-----")
                    # sudo.print_sudoku(sudoku)

                    # print()
                    continue

                column_discared = discarded_column(
                    row, number, sudoku)
                discarded[row] = []
                # descartar la COLUMNA utilizada en la iteración anterior de este NUMERO
                discarded[row-1].append(column_discared)
                # Limpiar la pocisión del sudoku
                sudoku[row-1][column_discared] = 0
                values[row-1].append(column_discared)

                # Limpiar el dato de los bloqueados
                blockeds.remove(column_discared)

                # Limpiar de los parcialmente bloqueados
                if column_discared < 3:
                    for partially in range(0, 3):
                        if partially != column_discared:
                            try:
                                partially_blockeds.remove(partially)
                            except:
                                pass
                elif column_discared >= 3 and column_discared < 6:
                    for partially in range(3, 6):
                        if partially != column_discared:
                            try:
                                partially_blockeds.remove(partially)
                            except:
                                pass
                elif column_discared > 5:
                    for partially in range(6, 9):
                        if partially != column_discared:
                            try:
                                partially_blockeds.remove(partially)
                            except:
                                pass

                row -= 1  # devolverse a la iteración aterior de este NUMERO # linea 5 FILA-1
                # print("print row: ", row)
                # print("print column: ", column)
                # print("print number: ", number)
                # print("print blocked: ", blockeds)
                # print("-----print memory-----")
                # print(dictionary_memory)
                # print("print partially_blocked: ", partially_blockeds)
                # print("print numbers: ", numbers)
                # print("-----print values-----")
                # for value in values:
                #     print(value)
                # print("-----print sudoku-----")
                # sudo.print_sudoku(sudoku)

                # print()
                continue

            blockeds.append(column)

            values[row].remove(column)
            sudoku[row][column] = number

            row += 1

            # print("print row: ", row)
            # print("print column: ", column)
            # print("print number: ", number)
            # print("print blocked: ", blockeds)
            # print("print partially_blocked: ", partially_blockeds)
            # print("print numbers: ", numbers)
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


def random_in_list(values: list, 
                blockeds: list, 
                partially_blockeds: list, 
                discarded: list,
                memory: list) -> int:

    one = partially_blockeds + blockeds + discarded + memory
    tow = values

    count = 0

    for item in tow:
        if item in one:
            count += 1

    if count == len(values):
        return 99

    number = int(random()*10)-1
    num_val = number in values
    num_bloq = number not in blockeds
    num_part = number not in partially_blockeds
    num_dis = number not in discarded
    num_mem = number not in memory
    if num_val and num_bloq and num_part and num_dis and num_mem:
        return number
    else:
        return random_in_list(values, blockeds, partially_blockeds, discarded, memory)


def random_in_list2(values: list):
    """Generate a random number in a list [0,9]"""
    number = int(random()*10)
    if number not in values:
        return random_in_list2(values)
    else:
        return number


# Principal main
if __name__ == "__main__":
    sudoku = Sudoku()
    valor = False

    conteo_buenas = 0
    conteo_malas = 0

    ini_time = default_timer()
    end_time = 0

    while not valor:
        sus = generate_new_sudoku(sudoku)
        valor = sudoku.validate_grid(sus)

    # ----------------------------------------------------
    # for i in range(1000):
    #     sus = generate_new_sudoku(sudoku)
    #     valor = sudoku.validate_grid(sus)
    #     if valor:
    #         conteo_buenas += 1
    #     else:
    #         conteo_malas += 1
    # ----------------------------------------------------
    end_time = default_timer()
    print(end_time-ini_time, "/", conteo_buenas, "/", conteo_malas)
