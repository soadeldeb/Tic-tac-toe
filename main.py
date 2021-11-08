'''name: Soad Eldeb
   Assignment: Tic tac toe
   Version: 1
   datum: 08-11-2021
'''

from random import randint
import sys, os
import time


def menu_main():
    '''
    This function is the main menu function of the game.
    The user gets 4 options to choose from.
    '''
    print('\nWhat would you like to do: ')
    print('1. Play the game Tic tac toe')
    print('2. View the Score board')
    print('3. Your Statistics')
    print('4. Exit')
    menu_option = input('\nPick a number from the menu options:')

    try:
        menu_option = int(menu_option)
    except ValueError:
        menu_option = 0

    if menu_option in [1, 2, 3, 4]:
        return menu_option
    else:
        return 0


def main():
    '''
    This function is the main where it all runs from.
    '''
    name = input('What is your name: ')
    while name.isalpha() == False:
        print("\n------------------------------------------------------------------------------")
        print('Your name can only contain letters.')
        print("------------------------------------------------------------------------------")
        name = input('\nWhat is your name: ')
    while len(name) <= 3 or len(name) >= 10:
        print("\n----------------------------------------------------------------------------")
        print('Your name needs to contain between 3 and 10 letters.')
        print("------------------------------------------------------------------------------")
        name = input('\nWhat is your name: ')
    while 1 != 0:
        number = menu_main()
        if number == 1:
            print("------------------------------Tic-tac-toe---------------------------------------")

        if number == 4:
            sys.exit()

        if number not in [1, 2, 3, 4]:
            print("\n------------------------------------------------------------------------------")
            print('You have to enter a word containing between 1 and 4 letters and other symbols are not allowed.')
            print("------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
