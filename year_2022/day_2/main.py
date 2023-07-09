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

with open('input.txt','r') as input_file:
    for line in input_file:
        line.split()
        opponentMove = line[0]
        playerMove = line[2]
        if opponentMove == "A":
            opponentMoveTranslated = "Rock"
        if opponentMove == "B":
            opponentMoveTranslated = "Paper"
        if opponentMove == "C":
            opponentMoveTranslated = "Scisors"
        
        if playerMove == "X":
            playerMoveTranslated = "Rock"
        if playerMove == "Y":
            playerMoveTranslated = "Paper"
        if playerMove == "Z":
            playerMoveTranslated = "Scisors"
"""        
A X 1+3=4    Rock Rock = Draw
A Y 1+6=7    Rock Paper = Win
A Z 1+0=1    Rock Scisors = Loss 
B X 2+0=2    Paper Rock = Loss
B Y 2+3=5    Paper Paper = Draw
B Z 2+6=8    Paper Scisors = Win
C X 3+6=9    Scisors Rock = Win
C Y 3+0=3    Scisors Paper = Loss
C Z 3+3=6    Scisors Scisors = Draw
"""         

        if playerMoveTranslated == opponentMoveTranslated:
            result = "Draw"
        if playerMoveTranslated 
        print(f"opponentMoveTranslated: {opponentMoveTranslated} playerMoveTranslated: {playerMoveTranslated}")
