from sudokus_manager.sudoku import Sudoku


# Main principal
if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.inicializate_sudoku(9)
    sudoku.create_sudoku()
    sudoku.validate_sudoku()
    print("#### GAME OF SUDOKUS ####\ndesea imprimir el sudoku (Y/N)?")
    res = input()
    if res == 'Y':
        sudoku.print_sudoku()
        print()
    elif res == 'N':
        print("Bye bye...")
        exit
    else:
        print("opción incorrecta")
