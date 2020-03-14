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

def validate_sudoku():
    block = []
    for f in range(len(sudoku)):
        for c in range(len(sudoku)):
            if f < int(len(sudoku)/3) and c < int(len(sudoku)/3):
                block.append(sudoku[f][c])

    print("block1: " + str(block))
    block = validate_block(block)
    print("block2: " + str(block))

def validate_block(block: list):
    contadores = [0,0,0,0,0,0,0,0,0]
    nums = (1,2,3,4,5,6,7,8,9)
    firts = [False,False,False,False,False,False,False,False,False]
    for num in block:
        if num in nums:
            contadores[num-1] +=1

    # Second state for the list
    for index, num in enumerate(block):
        if contadores[num-1] > 1 and firts[num-1]:
            block[index]=0
        elif contadores[num-1] > 1:
            firts[num-1] = True

    

    return block


if __name__ == "__main__":
    inicializate_sudoku()
    create_sudoku()
    validate_sudoku()
    print("#### GAME OF SUDOKUS ####\ndesea imprimir el sudoku (Y/N)?")
    res = input()
    if res == 'Y':
        print_sudoku()
        print()
    elif res == 'N':
        print("Bye bye...")
        exit
    else:
        print("opción incorrecta")