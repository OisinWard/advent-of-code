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

        print(f"opponentMoveTranslated: {opponentMoveTranslated} playerMoveTranslated: {playerMoveTranslated}")
