# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import word_list

def get_word():
    """
    This will pick at random a word from the words_list
    that the player will have to guess.
    """
    word = random.choice(word_list)
    return word.upper()


