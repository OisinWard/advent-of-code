"Opponent"
"A is rock"
"B is paper"
"C is scisors"

"Player"
"X is rock"
"Y is paper"
"Z is scisors"

"1 for Rock"
"2 for Paper"
"3 for Scissors"

"0 if you lost"
"3 if the round was a draw"
"6 if you won"

score = 0
with open('input.txt','r') as input_file:
    for line in input_file:
#       line.split()
        if line == 'A X\n':
          roundScore = 4
          score = score + roundScore
        if line == 'A Y\n':
          roundScore = 8
          score = score + roundScore
        if line == 'A Z\n':
          roundScore =3 
          score = score + roundScore
        if line == 'B X\n':
          roundScore = 1
          score = score + roundScore
        if line == 'B Y\n':
          roundScore = 5
          score = score + roundScore
        if line == 'B Z\n':
          roundScore = 9
          score = score + roundScore
        if line == 'C X\n':
          roundScore = 7
          score = score + roundScore
        if line == 'C Y\n':
          roundScore = 2 
          score = score + roundScore
        if line == 'C Z\n':
          roundScore = 6
          score = score + roundScore

print(score)
"""        
A X 1+3=4    Rock Rock = Draw
A Y 2+6=8    Rock Paper = Win
A Z 3+0=3    Rock Scisors = Loss 
B X 1+0=1    Paper Rock = Loss
B Y 2+3=5    Paper Paper = Draw
B Z 3+6=9    Paper Scisors = Win
C X 1+6=7    Scisors Rock = Win
C Y 2+0=2    Scisors Paper = Loss
C Z 3+3=6    Scisors Scisors = Draw
"""         

