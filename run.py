"""
    import modules & libaries
"""
import sys
import time
# os module used to clear termainal
import os
# import libary of ascii_letters
import string
# import words
import random
from words import words

# import handman tries pictuers
from hangman_visual import lives_visual_dict
# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Home Screen window when game start
def start_screen():
    """Sets start screen  up for the user asking for name
    and if they would like to start"""
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
    typewriter("""
    WELCOME TO HANGMAN\t\n
    THE RULES ARE SIMPLE, YOU HAVE 7 LIVES\t\n
    YOU MUST GUESS THE HIDDEN WORD, EVERYTIME YOU GUESS WRONG....\t\n
    YOU WILL LOSE A LIFE AND THE ROPE WILL TIGHTEN....\t\n
    THERE WILL BE ONLY ONE WINNER....THE STAKES ARE HIGH\t\n
    GOOD LUCK YOU WILL NEED IT\n
    \n""")
    name = input('SO WHAT IS YOUR NAME ?\n')
    typewriter(f"""'WELCOME, {name.upper()} I HOPE YOU ARE READY...\n""")
    typewriter(f"""THE LAST, {name.upper()} THAT PLAYED
    ..... IS STILL HANGING AROUND ;)""")
    if input(Fore.CYAN + '\n PRESS Y TO PLAY? (Y)').upper() == "Y":
        play_hangman()

    else:
        print(f"YOU MUST TYPE IN Y OR ARE YOU AFRAID TO PLAY {name.upper()}?")
        start_screen()


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
    Displays  lives and layout for player to play game.
    And guess the random word
    """
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
        print(Fore.YELLOW + '=============================================')
        print('You have'.upper(), lives, 'lives left'.upper())
        # letters that have been used
        print('You have used these letters: '.upper(), ' '.join(used_letters))
        print(Fore.YELLOW + '=============================================')
        # Tells the user what the current word with dashes (ie S - - P)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print(Fore.YELLOW + '=============================================')
        print(Fore.GREEN + 'Current word: '.upper(), ' '.join(word_list))

        # Ask the users for a letter guess
        user_letter = input('Guess a letter:\n').upper()
        # If valid letter in alphabet add to user letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # If guess is in the word it will remove from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                # takes away a life if wrong
                lives = lives - 1
                print(Fore.RED + 'That Letter is not in the word.'.upper())
        # If user guessed character that has already been guessed give feedback
        elif user_letter in used_letters:
            print(Fore.RED + 'Letter already used,please try again.'.upper())
        # If user guessed a character that is not a letter give user feedback
        else:
            print(Fore.RED + 'Invalid character,Please usa a letter.'.upper())

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(Fore.YELLOW + '=============================================')
        print(Fore.RED + 'Game Over.The word was'.upper(), Fore.CYAN + word)
        user_lose()
        print(Fore.YELLOW + '=============================================')
        restart_game()
    else:
        print('You are clever you guessed the word'.upper(), Fore.CYAN + word,)
        user_win()
        print(Fore.YELLOW + '=============================================')
        restart_game()


# Restarts the game when it has finished
def restart_game():
    """ Gives player option to restart, otherwise returns to title screen """
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Again ? (Y/N)\n').upper()

        if restart == "Y":
            game_restart = True
            clear_terminal()
            play_hangman()

        elif restart == "N":
            game_restart = True
            print('Bye for now . Mind your neck i will be waiting ;)')
            clear_terminal()
            start_screen()

        else:
            print(f" You must type in Y or N. You typed {(restart)}")


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
def clear_terminal():
    """
    Clearing the terminal.when restaring a new game
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    start_screen()