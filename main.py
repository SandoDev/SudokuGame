from random import random

sudoku = []

def inicializate_sudoku(value):
    for i in range(value):
        sudoku.append([0]*value)

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
    print("block3: " + str(block))

    contador = 0
    for f in range(len(sudoku)):
        for c in range(len(sudoku)):
            if f < int(len(sudoku)/3) and c < int(len(sudoku)/3):
                sudoku[f][c] = block[contador]
                contador += 1

def validate_block(block: list):
    contadores = [0,0,0,0,0,0,0,0,0]
    nums = (1,2,3,4,5,6,7,8,9)
    firts = [False,False,False,False,False,False,False,False,False]
    for num in block:
        if num in nums:
            contadores[num-1] +=1

    # Second state for the list
    """firts estate = [1,2,3,2,3,4,5]
        second state = [1,2,3,0,0,4,5]
    """
    for index, num in enumerate(block):
        if contadores[num-1] > 1 and firts[num-1]:
            block[index]=0
        elif contadores[num-1] > 1:
            firts[num-1] = True

    print("block2: " + str(block))
    contadores = [0,0,0,0,0,0,0,0,0]
    for num in block:
        if num in nums:
            contadores[num-1] +=1

    # Second state for the list
    """second state = [1,2,3,0,0,4,5]
        third state = [1,2,3,6,7,4,5]
    """
    for index, num in enumerate(contadores):
        if num == 0:
            value = True
            for indicator,data in enumerate(block):
                if data == 0 and value:
                    block[indicator]=nums[index]
                    value = False

    return block


if __name__ == "__main__":
    inicializate_sudoku(9)
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