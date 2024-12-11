# Run with: python day{#}.py {INPUT_PATH}
import sys
import copy

direction = ['up']
rMove = -1
cMove = 0

def changeDir():
    global direction
    global rMove
    global cMove
    if direction[-1] == 'up':
        direction.append('right')
        rMove = 0
        cMove = 1
    elif direction[-1] == 'right':
        direction.append('down')
        rMove = 1
        cMove = 0
    elif direction[-1] == 'down':
        direction.append('left')
        rMove = 0
        cMove = -1
    else:
        direction.append('up')
        rMove = -1
        cMove = 0
    return direction, rMove, cMove

inputData = open(sys.argv[1], 'r').readlines()
baseGrid = []
for line in inputData:
    baseGrid.append(list(line.strip()))

# For part 2
data = copy.deepcopy(baseGrid)

r = 0
c = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == '^':
            r = row
            c = col

data[r][c] = 'X'
p1Count = 1
while (r + rMove)  >= 0 and (r + rMove) < len(data) and (c + cMove) >= 0 and (c + cMove) < len(data[0]):
    if data[r + rMove][c + cMove] == '#':
        changeDir()
    if data[r + rMove][c + cMove] == '.':
        data[r + rMove][c + cMove] = 'X'
        p1Count += 1
    r += rMove
    c += cMove

# for row in data:
#     line = ''
#     for col in row:
#         line += col
#     print(line)

# Part 1 -----
print(p1Count)
# ------------

loopCount = 0
for row in range(len(baseGrid)):
    for col in range(len(baseGrid[row])):

        testGrid = copy.deepcopy(baseGrid)
        seenCount = 0

        if testGrid[row][col] == '.':
            testGrid[row][col] = 'O'

            r = 0
            c = 0
            for i in range(len(testGrid)):
                for j in range(len(testGrid[i])):
                    if testGrid[i][j] == '^':
                        r = i
                        c = j

            direction = ['up']
            rMove = -1
            cMove = 0
            testGrid[r][c] = 'X'

            p2Count = 1
            while (r + rMove)  >= 0 and (r + rMove) < len(testGrid) and (c + cMove) >= 0 and (c + cMove) < len(testGrid[0]):
                if testGrid[r + rMove][c + cMove] == '#' or testGrid[r + rMove][c + cMove] == 'O':
                    changeDir()
                if testGrid[r + rMove][c + cMove] == '.':
                    testGrid[r + rMove][c + cMove] = 'X'
                    p2Count += 1
                    seenCount = 0
                if testGrid[r + rMove][c + cMove] == 'X':
                    seenCount += 1
                if seenCount > p2Count:
                    loopCount += 1
                    # print(p2Count, seenCount)
                    # r = -2
                    # c = -2

                    for line in testGrid:
                        print(line)
                    break

                r += rMove
                c += cMove
                # print(r, c, seenCount, p2Count)

            # for line in testGrid:
            #   print(line)

            testGrid[row][col] = '.'
        # print()

print(loopCount)