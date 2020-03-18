from sudokus_manager.sudoku import Sudoku
from colorama import deinit


# Main principal
if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.create_sudoku()
    #sudoku.fix_horizontal_pseudo()
    sudoku.fix_vertical_pseudo()
    #sudoku.sudoku = sudoku.fix_blocks_pseudo(sudoku.sudoku)
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
