import numpy as np

with open('day8.txt', 'r') as f:
    data = [[num for num in line.split()].pop() for line in f]

grid = [[0 for col in range(len(data))] for row in range(len(data))]

def set(row, col, sightLine):
    global total
    grid[row][col] = np.prod(sightLine)

for row in range(1, len(data) - 1):

    for col in range(1, len(data[row]) - 1):
        sightLine = [0, 0, 0, 0]
        above = []
        below = []
        left = []
        right = []

        # search above
        for a in range(row - 1, -1, -1):
            sightLine[0] += 1
            if data[a][col] >= data[row][col]:
                break

        # search below
        for b in range(row + 1, len(data[row])):
            sightLine[1] += 1
            if data[b][col] >= data[row][col]:
                break

        # search left
        for l in range(col - 1, -1, -1):
            sightLine[2] += 1
            if data[row][l] >= data[row][col]:
                break

        # search right
        for r in range(col + 1, len(data[row])):
            sightLine[3] += 1
            if data[row][r] >= data[row][col]:
                break

        print(data[row][col], sightLine)
        set(row, col, sightLine)

for row in grid:
    for col in row:
        print(col),
    print('\n')

print(max(map(max, grid)))