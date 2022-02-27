# Write your code to expect a terminal of 80 characters wide and 24 rows high
# import randon python standard library
import random
# import words
from words import words


def get_word():
    """
    This will pick at random a word from the words_list
    that the player will have to guess.
    """
    # Select a randon word from the list
    word = random.choice(words)
    # Return word in uppercase
    return word.upper()
    

    

def play_hangman(word):
    """
    Play a game of hangman.
    Displays  lives and layout for player to play game.
    """
    
