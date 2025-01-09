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
            seen = {(r,c): 1}
            while (r + rMove)  >= 0 and (r + rMove) < len(testGrid) and (c + cMove) >= 0 and (c + cMove) < len(testGrid[0]):
                if testGrid[r + rMove][c + cMove] == '#' or testGrid[r + rMove][c + cMove] == 'O':
                    changeDir()
                    # print(f"foudn o, {row}, {col}")
                if testGrid[r + rMove][c + cMove] == '.':
                    testGrid[r + rMove][c + cMove] = 'X'
                    p2Count += 1
                    seenCount = 0
                    if ((r + rMove), (c + cMove)) not in seen:
                        seen[((r + rMove), (c + cMove))] = 1
                    else:
                        seen[((r + rMove), (c + cMove))] += 1

                if testGrid[r + rMove][c + cMove] == 'X':
                    seenCount += 1
                    if seen[((r + rMove), (c + cMove))] > 0:
                        seen[((r + rMove), (c + cMove))] -= 1

                # print(len(seen), p2Count, seenCount)
                if len(direction) > 2 and seenCount > p2Count:
                    if sum(seen.values()) == 0:
                        loopCount += 1
                        # print(p2Count, seenCount)
                        # r = -2
                        # c = -2

                    # for line in testGrid:
                    #     print(line)
                    # print(seen)
                        break

                r += rMove
                c += cMove
                # print(r, c, seenCount, p2Count)

            # if row == 1 and col == 5:
            #     for line in testGrid:
            #         print(line)

            testGrid[row][col] = '.'
            # print(seen)
        # print()

print(loopCount)