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


def name_player_checker(player_name, first_p):
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


def player_choise_check(player_choise,board_positions):
    # while player_choise.isdigit() == False :
    #     print("\n------------------------------------------------------------------------------")
    #     print('You can only pick a number between 1 and 9')
    #     print("------------------------------------------------------------------------------")
    #     player_choise = input('\nPick a number on the board: ')
    while 10 < int(player_choise) < 0:
        print("\n------------------------------------------------------------------------------")
        print('You can only pick a number between 1 and 9')
        print("------------------------------------------------------------------------------")
        player_choise = input('\nPick a number on the board: ')

    while int(player_choise) not in board_positions:
        print("This position is not available, please pick a position that is available on the board ")
        player_choise = input('\nPick a number on the board: ')
    board_positions.remove(int(player_choise))
    return player_choise,board_positions

def BoardImage(player_choise,player_turn,Position147,Position258,Position369):
    player_turn += 1
    if player_turn % 2 != 0:
        player = "X"
    elif player_turn % 2 == 0:
        player = "O"
    player_choise = int(player_choise)


    if player_choise == 1 or player_choise == 4 or player_choise == 7:
        Position147 = [w.replace(str(player_choise), str(player)) for w in Position147]
    if player_choise == 2 or player_choise == 5 or player_choise == 8:
        Position258 = [w.replace(str(player_choise), str(player)) for w in Position258]
    if player_choise == 3 or player_choise == 6 or player_choise == 9:
        Position369 = [w.replace(str(player_choise), str(player)) for w in Position369]

    for i in range(len(Position147)):
         print(Position147[i], Position258[i], Position369[i])

    return Position147,Position258,Position369

def boardlogic(player_x,player_o):
    board_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winer == False
    Position147 = ["    |", " 1  |", "----|", "    |", " 4  |", "----|", "    |", " 7  |", "    |"]
    Position258 = ["    |", " 2  |", "----|", "    |", " 5  |", "----|", "    |", " 8  |", "    |"]
    Position369 = ["    ", "  3 ", "----", "    ", "  6 ", "----", "    ", "  9 ", "    "]

    player_choise = "0"
    while len(board_positions) != 0:
        Position147,Position258,Position369 = BoardImage(player_choise,len(board_positions),Position147,Position258,Position369)
        if len(board_positions) % 2 != 0:
            print("It is your turn ",player_x , "player X")
            player_choise = input('\nPick a number on the board: ')
            checked_player_choise, board_positions = player_choise_check(player_choise,board_positions)
            winner = check_winner(Position147, Position258, Position369,winner)

        elif len(board_positions) % 2 == 0:
            print("It is your turn ",player_o , "player O")
            player_choise = input('\nPick a number on the board: ')
            checked_player_choise, board_positions = player_choise_check(player_choise, board_positions)
            winner = check_winner(Position147, Position258, Position369,winner)
    BoardImage(player_choise, len(board_positions), Position147, Position258, Position369)



def check_winner(Position147, Position258, Position369):

    #postions = Position147 + Position258 + Position369
    postions = ["    |", " 1  |", "----|", "    |", " X  |", "----|", "    |", " X  |", "    |"]
    removetable = str.maketrans('', '', '@#%|- ')
    out_list = [s.translate(removetable) for s in postions]
    str_list = list(filter(None, out_list))
    winning_combo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in winning_combo:
        if all(str_list[i]):
            return winner == True


def main():
    '''
    This function is the main where it all runs from.
    '''

    while 1 != 0:
        number = menu_main()
        if number == 1:
            print("------------------------------Tic-tac-toe---------------------------------------")
            player_X = input('What is your name player X: ')
            player_x = name_player_checker(player_X, "")
            player_O = input('What is your name player O: ')
            player_o = name_player_checker(player_O, player_x)
            print('\n' * 44)
            print("--------------------------------------------------------------------------------")
            print("Welcome player X : ", player_x, "and player O ", player_o)
            print("--------------------------------------------------------------------------------")

            # functie die per beurt vraagt van de nummer is en checkt of die nummer niet gebruikt is of dat de numer klopt
            # die functie returnt de correcte nummer en de player aan de beurt en dan wordt de functie van de board aangeroepem
            # die functie verandert dan de board en print dat mooi uit
            # dan is weer de andere aan de beurt

            boardlogic(player_x,player_o)

        if number == 4:
            sys.exit()

        if number not in [1, 2, 3, 4]:
            print("\n------------------------------------------------------------------------------")
            print('You have to enter a word containing between 1 and 4 letters and other symbols are not allowed.')
            print("------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
