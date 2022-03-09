# import os to help clear terminal
import sys
# import time for type writer function
import time
# os module used to clear termainal
import os
# import libary of ascii_letters
import string
# import words
import random
from words import words
# import handman tries pictuers
from hangman_lives import lives_visual_dict
# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Home Screen window when game start
def start_screen():
    """Sets start screen  up for the user asking for name
    and if they would like to start
    """
    print(
        Fore.YELLOW + """
            ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
            ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
            ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
            ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
            ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """
    )
    # Intro message in typewriter effect
    typewriter("""
    THERE CAN BE ONLY ONE WINNER.....\t\n
    WILL IT BE YOU OR THE HANGMAN.....\t\n
    """)
    # Ask for user name
    while True:
        username = input('SO WHAT IS YOUR NAME ?\n')

        if not username.isalpha():
            print(Fore.RED + 'INVALID,USERNAME MUSH HAVE CHARACTERS')
            continue
        else:
            typewriter(f"""WELCOME, {username.upper()} \n""")
            typewriter(""" I HOPE YOU ARE READY...\n""")
            typewriter(f"""THE LAST, {username.upper()} THAT PLAYED..... \n""")
            typewriter(""".. IS STILL HANGING AROUND ;)....\n\n""")
            break


# Main Menu for game
def menu():
    """
    Function for hangmans main menu.User can select
    3 options,Hangman Rules,Play Game and Exit Game
    """
    # Clear Terminal
    clear()
    print(Fore.YELLOW + '=============================================\n')
    print(Fore.CYAN + "HANGMAN MENU\n")
    print(Fore.GREEN + "1. HANGMAN RULES")
    print(Fore.GREEN + "2. START GAME")
    print(Fore.GREEN + "3. EXIT GAME \n")
    print(Fore.YELLOW + '=============================================')
    # Tests to see if valid selcetion of menu option
    while True:
        player_choice = input(Fore.CYAN + "PLEASE PICK 1.2.3 FROM THE MENU \n")

        if player_choice == '1':
            hangman_rules()
        elif player_choice == '2':
            play_hangman()
        elif player_choice == '3':
            exit_game()
        else:
            print(Fore.RED + "PLEASE PICK A VALID OPTION FROM THE MENU!")


# User can exit the whole game
def exit_game():
    """
    Exit game function
    """
    print("BYE FOR NOW...")
    print("IF YOU CHANGE YOUR MIND")
    print("CLICK THE RUN PROGRAM BOX TOP LEFT-TO START OVER")
    sys.exit()


# Rules of the game
def hangman_rules():
    """
    Outlines the rules of the game for the user
    using typewrite effect
    """
    # Clear Terminal
    clear()
    # Outlines Rules of game using typewriter effect
    typewriter("""
    HANGMAN RULES\t\n
    THE RULES ARE SIMPLE, YOU HAVE 7 LIVES\t\n
    YOU MUST GUESS THE HIDDEN WORD,\t\n
    TYPE A LETTER AND PRESS ENTER,\t\n
    EVERYTIME YOU GUESS WRONG....\t\n
    YOU WILL LOSE A LIFE AND THE ROPE WILL TIGHTEN....\t\n
    EVERYTIME YOU GUESS RIGHT....\t\n
    A LETTER WILL BE REVALED IN THE HIDDEN WORD\t\n
    THERE WILL BE ONLY ONE WINNER....\t\n
    THE STAKES ARE HIGH.....\t\n
    GOOD LUCK YOU WILL NEED IT\n
    \n""")
    # Give option to play or return to menu.
    print(Fore.CYAN + "WOULD YOU LIKE TO PLAY HANGMAN ? \n")

    # Test for see for valid selection
    while True:
        game_on = input("PRESS 1 FOR YES OR 2 FOR NO: ")

        if game_on == '1':
            play_hangman()
        elif game_on == '2':
            menu()
        else:
            print(Fore.RED + "TRY AGAIN,PICK A VALID OPTION!")


# Pick Word from list of words
def get_word():
    """
    This will pick at random a word from the words_list
    that the player will have to guess.
    """
    # Select a randon word from the list
    word = random.choice(words)
    # Return word in uppercase
    return word.upper()


# function for game
def play_hangman():
    """
    Play a game of hangman.
    Displays  lives and layout for user to play game.
    And guess the random word
    """
    # Clears Termainl
    clear()
    # get random word from get_word
    word = get_word()
    # letters that are in word
    word_letters = set(word)
    # list of character in alphabet uppercase
    alphabet = set(string.ascii_uppercase)
    # letters that the user has guessed
    used_letters = set()
    # number of tries the user has before game is over
    lives = 7
    # creat a loop to iterate through input until all the letters guessed
    while len(word_letters) > 0 and lives > 0:
        print(Fore.YELLOW + '========================================')
        print('You have'.upper(), lives, 'lives left'.upper())
        # letters that have been used
        print('You have used these letters: '.upper(), ' '.join(used_letters))
        print(Fore.YELLOW + '========================================')
        # Tells the user what the current word with dashes (ie S - - P)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print(Fore.YELLOW + '========================================')
        print(Fore.GREEN + 'Current word: '.upper(), ' '.join(word_list))

        # Ask the users for a letter guess
        user_letter = input('Guess a letter:\n').upper()
        # clear()
        # If valid letter in alphabet add to user letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # If guess is in the word it will remove from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(Fore.YELLOW + '========================================')
                print(Fore.GREEN + 'correct guess,well done'.upper())
                clear()
            else:
                # takes away a life if wrong
                lives = lives - 1
                print(Fore.YELLOW + '========================================')
                print(Fore.RED + 'That Letter is not in the word.'.upper())
                clear()
        # If user guessed character that has already been guessed give feedback
        elif user_letter in used_letters:
            print(Fore.YELLOW + '=========================================')
            print(Fore.RED + 'Letter already used,please try again.'.upper())
            clear()
        # If user guessed a character that is not a letter give user feedback
        else:
            print(Fore.YELLOW + '=========================================')
            print(Fore.RED + 'Invalid character,Please usa a letter.'.upper())
            clear()

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(Fore.YELLOW + '=========================================')
        print(Fore.RED + 'hangman wins.The word was'.upper(), Fore.CYAN + word)
        user_lose()
        print(Fore.YELLOW + '=========================================')
        restart_game()
    else:
        print(Fore.YELLOW + '==========================================')
        print('You are clever you guessed the word'.upper(), Fore.CYAN + word,)
        user_win()
        print(Fore.YELLOW + '=========================================')
        restart_game()


# Restarts the game when it has finished
def restart_game():
    """ Gives player option to restart, otherwise returns to title screen """
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Again ? (Y/N)\n').upper()
        # Restarts new game of hangman
        if restart == "Y":
            game_restart = True
            clear()
            play_hangman()
        # returns the user to main menu if they fdont want to play again
        elif restart == "N":
            game_restart = True
            print('BYE FOR NOW. MIND YOU NECK I WILL BE WAITING :-)')
            clear()
            menu()

        else:
            print(Fore.RED + f"TYPE EITHER Y or N. YOU TYPED {(restart)}")


# Banner appears at end of game
def user_win():
    """
    Display this graphic when users wins game
    """
    print(
        Fore.GREEN + """
        __   __
        \\ \\ / /__  _   _
         \\ V / _ \\| | | |
          | | (_) | |_| |
          |_|\\___/_\\__,_| _
        __      _(_)_ __ | |
        \\ \\ /\\ / / | '_ \\| |
         \\ V  V /| | | | |_|
          \\_/\\_/ |_|_| |_(_)
        """
        )


# Banner appears at end of game
def user_lose():
    """
    Display Game Over when player loses!
    """
    print(
        Fore.RED + """
          ____
         / ___| __ _ _ __ ___   ___
        | |  _ / _` | '_ ` _ \\ / _ \\
        | |_| | (_| | | | | | |  __/
         \\____|\\__,_|_| |_| |_|\\___|
         / _ \\__   _____ _ __| |
        | | | \\ \\ / / _ \\ '__| |
        | |_| |\\ V /  __/ |  |_|
         \\___/  \\_/ \\___|_|  (_)
        """
        )


# Typewriter used on the intro screen
def typewriter(line):
    """
   Typewriter for the start screen into
    """
    for i in line:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)


# Clear Terminal
def clear():
    """
    Clear screen for user on replay
    """
    os.system("clear")


# Calss main functions of game
def main():
    """
    Function to call other functions used in game
    """
    start_screen()
    menu()
    get_word()
    play_hangman()
main()
