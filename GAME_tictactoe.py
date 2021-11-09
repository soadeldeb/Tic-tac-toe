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
    print('1. Play the game Tic tac toe (two players)')
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

def name_player_checker(player_name,first_p):
    while player_name.isalpha() == False:
        print("\n------------------------------------------------------------------------------")
        print('Your name can only contain letters.')
        print("------------------------------------------------------------------------------")
        player_name = input('\nWhat is your name: ')
    while len(player_name) <= 3 or len(player_name) >= 10:
        print("\n----------------------------------------------------------------------------")
        print('Your name needs to contain between 3 and 10 letters.')
        print("------------------------------------------------------------------------------")
        player_name = input('\nWhat is your name: ')
    while player_name.lower() == first_p.lower():
        print("The name of player O can not be the same as player X please choose another name.")
        player_name = input('\nWhat is your name player O: ')
    return player_name

def BoardImage(player_choise,player_turn):
    empty_board = {'1':'1','2':'2','3':'3',
                   '4':'4', '5':'5','6':'6',
                   '7':'7', '8':'8','9':'9'}

    Position147 = ["    |"," 1  |","----|","    |"," 4  |","----|","    |"," 7  |","    |"]
    Position258 = ["    |"," 2  |","----|","    |"," 5  |","----|","    |"," 8  |","    |"]
    Position369 = ["    ","  3 ","----","    ","  6 ","----","    ","  9 ","    "]

    if player_choise == 1 | player_choise == 4 | player_choise == 7:
        Position147.replace(str(player_choise),player_turn)

    for i in range(len(Position147)):
        print(Position147[i],Position258[i],Position369[i])




def main():
    '''
    This function is the main where it all runs from.
    '''

    while 1 != 0:
        number = menu_main()
        if number == 1:
            print("------------------------------Tic-tac-toe---------------------------------------")
            player_X = input('What is your name player X: ')
            player_x = name_player_checker(player_X,"")
            player_O = input('What is your name player O: ')
            player_o = name_player_checker(player_O,player_x)

            print("Welcome player X : ", player_x, "and player O ", player_o)


            BoardImage(player_choise,player_turn)


        if number == 4:
            sys.exit()

        if number not in [1, 2, 3, 4]:
            print("\n------------------------------------------------------------------------------")
            print('You have to enter a word containing between 1 and 4 letters and other symbols are not allowed.')
            print("------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
