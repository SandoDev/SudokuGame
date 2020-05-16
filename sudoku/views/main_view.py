from colorama import init
from colorama import Fore, Back, Style
from .utils import generate_title

MAIN_TITTLE = generate_title("GAME OF SUDOKUS", 25, '#')


def main_menu():
    """Main menu"""
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
        values_quick, options_quick = quick_game()
        if values_quick not in options_quick:
            print(Fore.RED + "Wrong choice!!")
            print(Style.RESET_ALL)
            main_menu()

        if values_quick == '0':
            exit_game()

        if values_quick == '00':
            main_menu()

        if values_quick == '1':
            values_easy, options_easy = easy_game()

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
    """Exit the game"""
    print("Bye bye... :D")
    exit


def text_menu():
    """Main menu texts"""
    options = ['0', '1', '2', '3', '4', '5', '6']
    tittle = MAIN_TITTLE
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
    """Quick game texts"""
    options = ['00', '0', '1', '2', '3', '4']
    tittle = MAIN_TITTLE
    sub = generate_title('QUICK GAME', len(tittle), '=')
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


def easy_game():
    """Easy game texts"""
    options = ['00', '0', '1', '2', '3', '4']
    tittle = MAIN_TITTLE
    sub = generate_title('EASY GAME', len(tittle), '=')
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
