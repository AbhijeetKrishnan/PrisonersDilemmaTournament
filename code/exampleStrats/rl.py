import random
from collections import defaultdict

import numpy as np

def strategy(history, memory):
    n = 2 # 1 <= n <= ? (upper limit defined by available memory)
    eps = 0.0001 # prevent divide-by-zero errors
    eps2 = 0.0001

    if memory is None:
        memory = {
            'table': defaultdict(int), # table maps a state (n-length most-recent history slice)
                                         # to the number of times the opponent chose defect in
                                         # that state
            'total': defaultdict(int), # total maps a state to the number of times it was seen
            'prev_state': None
        }
    
    table = memory['table']
    total = memory['total']
    prev_state = memory['prev_state']
    
    # if game length is <= n, use tit-for-tat strategy
    if history.shape[1] <= n:
        choice = 1
        if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
            choice = 0
    else:
        if prev_state is None:
            prev_state = str(history[1, -1-n:-1])

        # examine history of previous n turns
        state = str(history[1, -n:])

        # calculate expected returns from co-operate and defect
        cooperate_return = table[state] / (total[state] + eps) * 5 + (total[state] - table[state]) / (total[state] + eps) * 3
        defect_return = (total[state] - table[state]) / (total[state] + eps)
        
        # calculate best action
        if cooperate_return >= defect_return:
            choice = 1
        else:
            choice = 0

        # implement e-greedy action selection
        #if random.random() < eps2:
        #    choice = 1 - choice

        # update table & total based on previous state and opponent action
        total[state] += 1
        opponent_action = history[1,-1]
        if opponent_action == 0: # opponent chose defect
            table[state] += 1

        #print(table, total)

        memory['table'] = table
        memory['total'] = total
        memory['prev_state'] = state

    return choice, memory