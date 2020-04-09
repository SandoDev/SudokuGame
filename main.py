from sudokus_manager.sudoku import Sudoku
from colorama import deinit
from others.generate_sudoku import create_new_sudoku


# Main principal
if __name__ == "__main__":
    sudoku = Sudoku()
    sus = create_new_sudoku()
    #sudoku.create_sudoku()
    #sudoku.fix_horizontal_pseudo()
    #sudoku.fix_vertical_pseudo()
    #sudoku.sudoku = sudoku.fix_blocks_pseudo(sudoku.sudoku)
    print("Resultado sudoku: ",sudoku.validate_grid(sus))
    print("#### GAME OF SUDOKUS ####\ndesea imprimir el sudoku (Y/N)?")
    res = input()
    if res == 'Y':
        sudoku.print_sudoku(sus)
        print()
    elif res == 'N':
        print("Bye bye...")
        exit
    else:
        print("opción incorrecta")
    deinit()
