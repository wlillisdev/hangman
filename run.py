# Write your code to expect a terminal of 80 characters wide and 24 rows high
# import randon python standard library
import random
# import words
from words import words
# import libary of ascii_letters
import string


def get_word():
    """
    This will pick at random a word from the words_list
    that the player will have to guess.
    """
    # Select a randon word from the list
    word = random.choice(words)
    # Return word in uppercase 
    return word.upper() 
    

    

def play_hangman():
    """
    Play a game of hangman.
    Displays  lives and layout for player to play game.
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
    
    # Getting the users letter guess
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
                print('')

     

    
    
