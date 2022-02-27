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
    word = get_word() # get random word from get_word
    word_letters = set(word)  # letters that are in word
    alphabet = set(string.ascii_uppercase) # list of character in alphabet uppercase
    used_letters = set()  # letters that the user has guessed
    lives = 7   # number of tries the user has before game over

    
    
