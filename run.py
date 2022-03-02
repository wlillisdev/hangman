"""
    import modules & libaries
"""
# os module used to clear termainal
import os
# import words
import random
from words import words
# import libary of ascii_letters
import string
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
    print(Fore.YELLOW +
        """
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """
          )
    name = input('So What is your name ?\n')
    print(f'Welcome, {name} i hope you are ready...')
    print(f'The last, {name} that played is still hanging around ;)')
    if input(Fore.CYAN + 'Press Y to play? (Y)').upper() == "Y":
        play_hangman()

    else:
        print(f"You must type in Y or are you afraid to play {name}?")
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
        print(Fore.GREEN + '=============================================')
        print('You have', lives, 'lives left')
        # letters that have been used
        print('You have used these letters: ', ' '.join(used_letters))
        print(Fore.GREEN + '=============================================')
        # Tells the user what the current word with dashes (ie S - - P)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print(Fore.GREEN + '=============================================')
        print('Current word: ', ' '.join(word_list))

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
                print(Fore.RED + 'Letter is not in the word.')
        # If user guessed character that has already been guessed give feedback
        elif user_letter in used_letters:
            print(Fore.RED + 'You have already used that letter,try again.')
        # If user guessed a character that is not a letter give user feedback
        else:
            print(Fore.RED + 'Invalid character,Please usa a letter.')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(Fore.GREEN + '=============================================')
        print(Fore.RED + 'Game Over :( The word was', Fore.CYAN + word)
        user_lose()
        print(Fore.GREEN + '=============================================')
        restart_game()
    else:
        print('You are clever you guessed the word', Fore.CYAN + word, )
        user_win()
        print(Fore.GREEN + '=============================================')
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


def user_win():
    """
    Display winner! banner
    """
    print(Fore.GREEN +
        """
        _       ___                      
        | |     / (_)___  ____  ___  _____
        | | /| / / / __ \/ __ \/ _ \/ ___/
        | |/ |/ / / / / / / / /  __/ / 
        |__/|__/_/_/ /_/_/ /_/\___/_/ 
        """
    )


def user_lose():
    """
    Display user lose! banner
    """
    print(Fore.RED +
         """
            __   __                
            \ \ / /__  _   _       
             \ V / _ \| | | |      
              | | (_) | |_| |      
             _|_|\___/ \__,_|    _ 
            | |    ___  ___  ___| |
            | |   / _ \/ __|/ _ \ |
            | |__| (_) \__ \  __/_|
            |_____\___/|___/\___(_)
         """
    )


def clear_terminal():
    """
    Clearing the terminal.when restaring a new game
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    start_screen()