import sys
sys.path.append('./')
from sudokus_manager.sudoku import Sudoku
import numpy as np
from random import random


sudo = Sudoku()
grid = sudo.sudoku
# sudo.print_sudoku(grid)


def number_assignment2(number: int):
    """Esta función hasta el momento tiene la certeza de asignar 
    el numero por cada bloque, por cada fila y cada columna
    """
    columns = [9, 9, 9, 9, 9, 9, 9, 9, 9]

    blocks = ["libre", "libre", "libre", "libre",
              "libre", "libre", "libre", "libre", "libre"]

    # Repeat for each column
    for line, data in enumerate(grid):
        new_list=[]
        if line < 3:
            column = sudo.generate()
            for index_repeat,repeat_columns in enumerate(columns):
                if repeat_columns ==9:
                    new_list.append(index_repeat)
                            
            if not(column in new_list):
                for new in new_list:
                    #------------------Validar que grid[line][index]==0
                    column=new
                    break

            #------------------Validar que grid[line][index]==0


            if column < 3:
                if blocks[0] == "libre":
                    blocks[0] = "ocupado"
                    for index in range(0, 3):
                        if index != column and columns[index] != 1: #------------------Validar que grid[line][index]==0
                            columns[index] = 10
                            #column = index
            elif column >= 3 and column <= 5:
                if blocks[1] == "libre":
                    blocks[1] = "ocupado"
                    for index in range(3, 6):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            else:
                if blocks[2] == "libre":
                    blocks[2] = "ocupado"
                    for index in range(6, 9):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            if columns[column] == 1 or columns[column] == 10:
                for index, data2 in enumerate(columns):
                    if data2 != 10 and data2 != 1:
                        column = index
                        if index < 3:
                            blocks[0] = "ocupado"
                            for index_range in range(0, 3):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        elif index >= 3 and index <= 5:
                            blocks[1] = "ocupado"
                            for index_range in range(3, 6):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        else:
                            blocks[2] = "ocupado"
                            for index_range in range(6, 9):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        break
            columns[column] = 1

            grid[line][column] = number

            if line == 2:
                for index_column, reset in enumerate(columns):
                    if reset == 10:
                        columns[index_column] = 9

        elif line >= 3 and line <= 5:
            column = sudo.generate()
            for index_repeat,repeat_columns in enumerate(columns):
                if repeat_columns ==9:
                    new_list.append(index_repeat)
            
            if not(column in new_list):
                for new in new_list:
                    column=new
                    break
            if column < 3:
                if blocks[3] == "libre":
                    blocks[3] = "ocupado"
                    for index in range(0, 3):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
                            #asignar el index como nueva columna
            elif column >= 3 and column <= 5:
                if blocks[4] == "libre":
                    blocks[4] = "ocupado"
                    for index in range(3, 6):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            else:
                if blocks[5] == "libre":
                    blocks[5] = "ocupado"
                    for index in range(6, 9):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            if columns[column] == 1 or columns[column] == 10:
                for index, data2 in enumerate(columns):
                    if data2 != 10 and data2 != 1:
                        column = index
                        if index < 3:
                            blocks[3] = "ocupado"
                            for index_range in range(0, 3):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        elif index >= 3 and index <= 5:
                            blocks[4] = "ocupado"
                            for index_range in range(3, 6):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        else:
                            blocks[5] = "ocupado"
                            for index_range in range(6, 9):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        break
            columns[column] = 1

            grid[line][column] = number

            if line == 5:
                for index_column, reset in enumerate(columns):
                    if reset == 10:
                        columns[index_column] = 9
        else:
            column = sudo.generate()
            for index_repeat,repeat_columns in enumerate(columns):
                if repeat_columns ==9:
                    new_list.append(index_repeat)
            
            if not(column in new_list):
                for new in new_list:
                    column=new
                    break
            if column < 3:
                if blocks[6] == "libre":
                    blocks[6] = "ocupado"
                    for index in range(0, 3):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            elif column >= 3 and column <= 5:
                if blocks[7] == "libre":
                    blocks[7] = "ocupado"
                    for index in range(3, 6):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            else:
                if blocks[8] == "libre":
                    blocks[8] = "ocupado"
                    for index in range(6, 9):
                        if index != column and columns[index] != 1:
                            columns[index] = 10
                            #column = index
            if columns[column] == 1 or columns[column] == 10:
                for index, data2 in enumerate(columns):
                    if data2 != 10 and data2 != 1:
                        column = index
                        if index < 3:
                            blocks[6] = "ocupado"
                            for index_range in range(0, 3):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        elif index >= 3 and index <= 5:
                            blocks[7] = "ocupado"
                            for index_range in range(3, 6):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        else:
                            blocks[8] = "ocupado"
                            for index_range in range(6, 9):
                                if index_range != column and columns[index_range] != 1 and columns[index_range] != 10:
                                    columns[index_range] = 10
                        break
            columns[column] = 1

            grid[line][column] = number
            if line == 8:
                for index_column, reset in enumerate(columns):
                    if reset == 10:
                        columns[index_column] = 9


def to_block_columns():
    pass


def number_assignment(number: int):
    columns = [9, 9, 9, 9, 9, 9, 9, 9, 9]

    blocks = sudo.blocks_to_line(grid)

    # sudo.print_sudoku(grid)
    #sudo.print_sudoku(blocks, 1)

    # Repeat for each column
    for line, data in enumerate(grid):

        # Acount columns
        column = sudo.generate()
        if columns[column] == 1:
            for index, data2 in enumerate(columns):
                if data2 == 9:
                    column = index
                    break
        columns[column] = 1

        # Validate and assigment
        if not(number in grid[line]):
            ready_blocks, columns_range = validate_in_blocks(
                line, number, blocks)
            if not(ready_blocks[line]):
                if grid[line][column] == 0:
                    grid[line][column] = number
                    blocks = sudo.blocks_to_line(grid)
                else:
                    columns[column] = 9
                    for index2, data3 in enumerate(grid[line]):
                        if data3 == 0:
                            grid[line][index2] = 0
                            break
            else:
                for ready, data4 in enumerate(ready_blocks):
                    if not(ready_blocks[ready]):
                        for columns_vacia in range(3):
                            if columns_vacia == 0:
                                columns[column] = 9
                                columns[columns_vacia] = 1
                                grid[line][columns_vacia] = number
                                blocks = sudo.blocks_to_line(grid)
                                salir = True
                                break
                        if salir:
                            break
                        else:
                            columns[column] = 9
                            for index2, data3 in enumerate(grid[line]):
                                if data3 == 0:
                                    grid[line][index2] = 0
                                    break


def validate_in_blocks(line, number, blocks) -> list:
    ready_blocks = []

    for line in blocks:
        if number in line:
            ready_blocks.append(True)
        else:
            ready_blocks.append(False)

    return ready_blocks


numbers2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# for num in numbers2:
#     number_assignment(num)


number_assignment2(1)
number_assignment2(8)
number_assignment2(7)
sudo.print_sudoku(grid)
