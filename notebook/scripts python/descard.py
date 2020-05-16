from random import random
import numpy as np
import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku


def discared(sudo):
    sudoku = sudo.inicializate_sudoku(9)
    descatados = [2]

    number_final = 4
    entro_una = False

    for index, line in enumerate(sudoku):
        number = sudo.generate()
        line[number] = number_final

    index = 0
    while index <= 8:
        if 2 in descatados and not entro_una and index == 6:
            entro_una = True
            index -= 1
            descatados.append(descartar(index, number_final, sudoku))
            continue
        index += 1
    print(descatados)
    sudo.print_sudoku(sudoku)


def descartar(current_row, current_number, grid):
    column_discared = 99
    for index, value in enumerate(grid[current_row]):
        if value == current_number:
            column_discared = index
            break
    return column_discared


# Principal main
if __name__ == "__main__":
    sudoku = Sudoku()
    sus = discared(sudoku)
    # sudoku.validate_grid(sus)
