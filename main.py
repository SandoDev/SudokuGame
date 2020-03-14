from random import random

sudoku = []

def inicializate_sudoku():
    for i in range(9):
        sudoku.append([0]*9)

def print_sudoku():
    for f in range(len(sudoku)):
        for c in range(len(sudoku)):
            print("[",sudoku[f][c],"]", end="")
        print()

def zero_different(num):
    if num == 0:
        return zero_different(int(random()*10))
    else:
        return num

def create_sudoku():
    for f in range(len(sudoku)):
        for c in range(len(sudoku)):
            sudoku[f][c] = zero_different(int(random()*10))

if __name__ == "__main__":
    inicializate_sudoku()
    create_sudoku()
    print("#### GAME OF SUDOKUS ####\ndesea imprimir el sudoku (Y/N)?")
    res = input()
    if res == 'Y':
        print_sudoku()
    elif res == 'N':
        print("Bye bye...")
        exit
    else:
        print("opción incorrecta")