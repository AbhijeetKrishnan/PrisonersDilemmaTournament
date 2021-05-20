import random

def strategy(history, memory):
    
    PAYOUTS = {
        (0, 0): (1, 1),
        (0, 1): (5, 0),
        (1, 0): (0, 5),
        (1, 1): (3, 3)
    }

    defect_tolerance = 0 # how many opponent defects we will tolerate before defecting ourselves
                         # 0 is essentially tit-for-tat
                         # 1 is essentially ftft

    if memory is None:
        memory = {
            'p1_total': 0,
            'p2_total': 0,
        }
    p1_total = memory['p1_total']
    p2_total = memory['p2_total']

    if history.shape[1] > 0:
        p1_payoff, p2_payoff = PAYOUTS[history[0,-1], history[1,-1]]
        p1_total += p1_payoff
        p2_total += p2_payoff

    balance = p1_total - p2_total
    # print(p1_total, p2_total, balance)

    if balance < defect_tolerance * -5:
        choice = 0
    else:
        choice = 1

    memory['p1_total'] = p1_total
    memory['p2_total'] = p2_total
    return choice, memory