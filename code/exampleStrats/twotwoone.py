import random

def strategy(history, memory):
    numTurns = history.shape[1]
    if numTurns % 4 == 3:
        choice = 0
    else:
        choice = 1
    return choice, None