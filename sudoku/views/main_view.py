from colorama import init
from colorama import Fore, Back, Style


def main_menu():
    value, options = text_menu()
    if value not in options:
        print(Fore.RED + "Wrong choice!!")
        print(Style.RESET_ALL)
        main_menu()

    if value == '0':
        exit_game()

    if value == '1':
        # TODO por hacer esta vista
        print("See scores")

    if value == '2':
        value, options = quick_game()
        if value not in options:
            print(Fore.RED + "Wrong choice!!")
            print(Style.RESET_ALL)
            main_menu()

        if value == '0':
            exit_game()

        if value == '00':
            main_menu()

        # TODO por completar esta vista

    if value == '3':
        # TODO por hacer esta vista
        print("Flags")

    if value == '4':
        # TODO por hacer esta vista
        print("General settings")

    if value == '5':
        # TODO por hacer esta vista
        print("Game instructions")

    if value == '6':
        # TODO por hacer esta vista
        print("About the game")


def exit_game():
    print("Bye bye... :D")
    exit


def text_menu():
    options = ['0', '1', '2', '3', '4', '5', '6']
    tittle = "#### GAME OF SUDOKUS ####"
    [print('-', end="") for letter in tittle]
    print()
    print(Style.BRIGHT + Back.GREEN + tittle, end="")
    print(Style.RESET_ALL)
    print(options[1]+" - See scores")
    print(options[2]+" - Quick game")
    print(options[3]+" - Flags")
    print(options[4]+" - General settings")
    print(options[5]+" - Game instructions")
    print(options[6]+" - About the game")
    print(options[0]+" - Exit")
    print()
    print("choose your option: ", end="")
    return input(), options


def quick_game():
    options = ['00', '0', '1', '2', '3', '4']
    tittle = "#### GAME OF SUDOKUS ####"
    sub = generate_subtittle('QUICK GAME', len(tittle), '=')
    [print('-', end="") for letter in tittle]
    print()
    print(Style.BRIGHT + Fore.GREEN + tittle)
    print()
    print(Fore.GREEN + sub, end="")
    print(Style.RESET_ALL)
    print(options[2]+" - Easy")
    print(options[3]+" - Medium")
    print(options[4]+" - Hard")
    print(options[5]+" - Researcher")
    print(options[0]+" - Return")
    print(options[1]+" - Exit")
    print()
    print("choose your option: ", end="")
    return input(), options


def generate_subtittle(sub: str, length: int, complement: str = '-'):
    """Generate a subtittle with specific length"""
    final = ""
    len_sub = len(sub)
    value = length-len_sub
    left = 0
    rigth = 0
    side_value = 0
    complement = complement
    separator = ""
    if len_sub < length:
        separator = " "
    elif len_sub == length:
        return sub
    else:
        for i in range(length):
            final = final + complement
        return final

    if value % 2 == 0:
        side_value = int(value/2)-1
        for i in range(length):
            if i < side_value:
                final = final + complement
            elif i > (side_value+len_sub)+1:
                final = final + complement
            elif (side_value+len_sub)+1 == i:
                final = final + separator+sub+separator
    else:
        left = int((value - 1)/2)
        rigth = left+1+len_sub
        for i in range(length):
            if i < left:
                final = final + complement
            elif i > rigth:
                final = final + complement
            elif left+1 == i:
                final = final + separator+sub+separator

    return final
