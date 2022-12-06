scores_p1 = []
scores_p2 = []

values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

beats = {
    1: 3,
    2: 1,
    3: 2
}

loseDrawWin = {
    'X': 'l',
    'Y': 'd',
    'Z': 'w'
}

def getScore_p1(opp, you):
    scoreYou = values[you]
    scoreOpp = values[opp]

    if(beats[scoreOpp] == scoreYou):
        return 0 + scoreYou
    elif(scoreOpp == scoreYou):
        return 3 + scoreYou
    else:
        return 6 + scoreYou

def getScore_p2(opp, you):
    scoreOpp = values[opp]
    outcome = loseDrawWin[you]
    
    if(outcome == 'l'):
        yourMove = beats[scoreOpp]
    elif(outcome == 'd'):
        yourMove = scoreOpp
    else:
        yourMove = beats.keys()[beats.values().index(scoreOpp)]

    if(beats[scoreOpp] == yourMove):
        return 0 + yourMove
    elif(scoreOpp == yourMove):
        return 3 + yourMove
    else:
        return 6 + yourMove

f = open('d2.txt', 'r')
for line in f:
    scores_p1.append(getScore_p1(line[0], line[2]))
    scores_p2.append(getScore_p2(line[0], line[2]))



print(sum(scores_p1))
print(sum(scores_p2))