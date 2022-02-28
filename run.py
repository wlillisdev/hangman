"""
    import modules & libaries
"""
import random
# import words
from words import words
# import libary of ascii_letters
import string
# import handman tries pictuers
from hangman_visual import lives_visual_dict
# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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
def hangman():
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

        print('You have', lives, 'lives left')
        # letters that have been used
        print('You have used these letters: ', ' '.join(used_letters))

        # Tells the user what the current word with dashes (ie S - - P)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
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
                print('Letter is not in the word.')
        # If user guessed character that has already been guessed give feedback
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        # If user guessed a character that is not a letter give user feedback
        else:
            print('Invalid character. Please try again with a letter.')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Game Over you died:( The word was', word)
        user_lose()
        restart_game()
    else:
        print('You are clever you guessed the word', word, '\nWell Done!!')
        user_wins()
        restart_game()


def restart_game():
    """
    Gives User Option to restart a game of hangman when game finished.
    otherwise it will returns user to title screen
    """
    
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Hangman? (Y/N)\n').upper()


        try:
            if restart == "Y":
                game_restart = True
                hangman()

            elif restart == "N":
                game_restart = True
                print("\n")
                print('Bye for Now, Mind Your Neck ;)')
                # start_game()
                

            else:
                raise ValueError(
                    f" You must type in Y or N. You typed {(restart)}"
                )

       

       


# if __name__ == "__main__":
#     start_game()

def user_wins():
    """
    Display winner! banner
    """
    print(
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
    print(
         """
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

hangman()