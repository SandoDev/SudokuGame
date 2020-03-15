from sudokus_manager.sudoku import Sudoku
from colorama import deinit


# Main principal
if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.create_sudoku()
    sudoku.validate_sudoku()
    sudoku.validate_grid(sudoku.sudoku)
    print("#### GAME OF SUDOKUS ####\ndesea imprimir el sudoku (Y/N)?")
    res = input()
    if res == 'Y':
        sudoku.print_sudoku(sudoku.sudoku)
        print()
    elif res == 'N':
        print("Bye bye...")
        exit
    else:
        print("opción incorrecta")
    deinit()
