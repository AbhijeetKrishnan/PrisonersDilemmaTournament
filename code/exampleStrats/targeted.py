import random

def strategy(history, memory):
    game_length = history.shape[1]
    choice = 1

    if memory is not None:
        if memory == 0:
            return 0, memory
        elif memory == 1:
            if game_length == 3:
                return 0, memory
            elif game_length > 3:
                return 1, memory
        elif memory == 2:
            return (1 - history[0, -1]), memory
        elif memory == 3:
            choice = 1
            if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
                choice = 0
            return choice, memory

    if game_length == 0:
        choice = 1
    elif game_length == 1:
        opponent = history[1,-1]
        choice = 0
        if opponent == 0: # always defect, random, joss
            memory = 0 # always defect
    elif game_length == 2:
        opponent = history[1,-1]
        choice = 0
        if opponent == 0: # detective, random, joss
            memory = 1 # anti-detective
    elif game_length == 3:
        opponent = history[1,-1]
        choice = 1
        if opponent == 1: # ftft
            memory = 2 # anti-ftft
    elif game_length == 4:
        opponent = history[1,-1]
        if opponent == 1: # always cooperate, simpleton
            choice = 0
            memory = 0 # anti-always cooperate
        else:
            choice = 1
    elif game_length == 5:
        opponent = history[1,-1]
        if opponent == 0: # gT
            choice = 0
            memory = 0
        else: # Tf, simpleton
            choice = 1
            memory = 3 

    return choice, memory