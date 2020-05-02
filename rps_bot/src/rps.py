"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""

choices = ["rock", "paper", "scissors"]

def resolve(choice_1, choice_2):
    print("Resolving")
    c1_index = choices.index(choice_1)
    c2_index = choices.index(choice_2)
    print(c1_index)
    print(c2_index)
    
    winner = "tie"
    if c1_index == 0 and c2_index == 2:
        winner = choice_1
    elif c1_index == 2 and c2_index == 0:
        winner = choice_2
    elif c1_index + 1 == c2_index:
        winner = choice_2
    elif c2_index + 1 == c1_index:
        winner = choice_1
    return winner

r = "rock"
p = "paper"
s = "scissors"

print("winner: {}".format(resolve(p, p)))
    