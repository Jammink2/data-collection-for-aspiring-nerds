#!/usr/bin/python
#a single hand game of rock, paper, scissors
#john@johnhamm.ink

import random

tie= "a tie"
p1 = "Player 1; Player 2 loses"
p2 = "Player 2; Player 1 loses"

myDict = {('rock', 'rock') : tie, ('rock', 'paper') : p2,
('rock', 'scissors') : p1, ('paper', 'rock') : p1, ('paper', 'paper') : tie, ('paper', 'scissors') : p2, ('scissors', 'rock') : p2, ('scissors', 'paper') : p1, ('scissors', 'scissors') : tie } 

def throw(player1, player2):
    verdict = myDict[(player1, player2)]
    print "The game goes to " + verdict

print "Ya wanna play Rock, Paper, Scissors?"
player1 = raw_input("Throw!  Choose 'rock', 'paper', or 'scissors': " )
print "Player 1 chooses: " + player1
player2 = random.choice(['rock', 'paper', 'scissors'])
print "Player 2 chooses: " + player2
throw(player1, player2)
