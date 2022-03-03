import sys
import time


def typewriter(string):
    """
   Typewriter visul for the opening intor screen
   """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)