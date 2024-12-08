# Run with: python day{#}.py {INPUT_PATH}
import sys
import re

data = open(sys.argv[1], 'r').readlines()

p1Horizontal = 0
p1Vertical = 0
p1DiagLeft = 0
p1DiagRight = 0

# p1Horizontal
for line in data:
    matchesForward = re.finditer(r'(?=(XMAS)+)', line)
    for entry in matchesForward:
        # print(entry.group(1))
        p1Horizontal += 1

    matchesReverse = re.finditer(r'(?=(SAMX)+)', line)
    for entry in matchesReverse:
        # print(entry.group(1))
        p1Horizontal += 1
# print('h', p1Horizontal)

# p1Vertical
for row in range(len(data) - 3):
    for col in range(len(data[row]) - 1):
        word = data[row][col] + data[row + 1][col] + data[row + 2][col] + data[row + 3][col]
        if word == 'XMAS' or word == 'SAMX':
            p1Vertical += 1
            # print(word)
# print('v', p1Vertical)

# Diagonal \
for row in range(len(data) - 3):

    colLength = len(data[row])
    if(data[row][-1] == '\n'):
        colLength -= 1

    for col in range(colLength - 3):
        word = data[row][col] + data[row + 1][col + 1] + data[row + 2][col + 2] + data[row + 3][col + 3]
        if word == 'XMAS' or word == 'SAMX':
            p1DiagLeft += 1
            # print(word)
# print('l', p1DiagLeft)

# Diagonal /
for row in range(len(data) - 1, 2, -1):

    colLength = len(data[row])
    if(data[row][-1] == '\n'):
        colLength -= 1

    for col in range(colLength - 3):
        word = data[row][col] + data[row - 1][col + 1] + data[row - 2][col + 2] + data[row - 3][col + 3]
        if word == 'XMAS' or word == 'SAMX':
            p1DiagRight += 1
            # print(word)
# print('r', p1DiagRight)

# Part 1 --------------------------------------------------
print(p1Horizontal + p1Vertical + p1DiagLeft + p1DiagRight)
# ---------------------------------------------------------

xCount = 0

# X-shape
for row in range(len(data) - 2):

    colLength = len(data[row])
    if(data[row][-1] == '\n'):
        colLength -= 1

    for col in range(colLength - 2):
        word = data[row][col] + data[row][col + 2] + data[row + 1][col + 1] + data[row + 2][col] + data[row + 2][col + 2]
        if word == 'MSAMS' or word == 'SSAMM' or word == 'MMASS' or word == 'SMASM':
            xCount += 1
            # print(word)

# Part 2 ----
print(xCount)
# -----------
