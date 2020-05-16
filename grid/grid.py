from colorama import init
from colorama import Fore, Back, Style


def new_grid(rows=9, columns=9, number=0):
    """
    Create new grid

    Parameters
    ----------
        rows: int
            number of rows
        columns: int
            number of columns
        number: int
            number for fill the grid

    Returns
    --------
        grid: list
    """
    grid = []
    for i in range(rows):
        grid.append([number]*columns)

    return grid


def print_grid(grid, style=0):
    """
    Print a grid with different styles

    Parameters
    ----------
        grid: list
            grid to print

        style: int
            0: withuot style
            1: horizontal
            2: vertical
            3: blocks

    Returns
    ----------
        Output in console
    """
    rows = len(grid)
    columns = len(grid[0])

    if style == 0:
        for i in range(rows):
            for j in range(columns):
                print("[", grid[i][j], "]", end="")
            print()
    elif style == 1:
        for i in range(rows):
            for j in range(columns):
                if i % 2 == 0:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                else:
                    print("[", grid[i][j], "]", end="")
            print()
    elif style == 2:
        for i in range(rows):
            for j in range(columns):
                if j % 2 == 0:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                else:
                    print("[", grid[i][j], "]", end="")
            print()
    elif style == 3:
        line_row = 0
        line_column = 0

        if rows % 3 == 0:
            line_row = rows/3
        elif rows % 2 == 0:
            line_row = rows/2
        else:
            line_row = (rows/3).__round__()
        if columns % 3 == 0:
            line_column = columns/3
        elif columns % 2 == 0:
            line_column = columns/2
        else:
            line_column = (columns/3).__round__()

        for i in range(rows):
            for j in range(columns):
                if i < line_row and j < line_column:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                elif (i < line_row) and \
                        (j >= line_column and j < line_column*2):
                    print("[", grid[i][j], "]", end="")
                elif i < line_row and \
                        j >= line_column*2:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                elif (i >= line_row and i < line_row*2) and \
                        j < line_column:
                    print("[", grid[i][j], "]", end="")
                elif (i >= line_row and i < line_row*2) and \
                        (j >= line_column and j < line_column*2):
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                elif (i >= line_row and i < line_row*2) \
                        and j >= line_column*2:
                    print("[", grid[i][j], "]", end="")
                elif i >= line_row and j < line_column:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
                elif i >= line_row and \
                        (j >= line_column and j < line_column*2):
                    print("[", grid[i][j], "]", end="")
                elif i >= line_row and j >= line_column:
                    print(Back.WHITE + Fore.BLACK +
                          "[", grid[i][j], "]", end="")
                    print(Style.RESET_ALL, end="")
            print()
    else:
        for i in range(rows):
            for j in range(columns):
                print(grid[i][j], end="")
            print()
