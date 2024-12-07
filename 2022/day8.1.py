with open('day8.txt', 'r') as f:
    data = [[num for num in line.split()].pop() for line in f]

edges = 4 * len(data) - 4
total = edges
grid = [[0 for col in range(len(data))] for row in range(len(data))]

def set(row, col):
    global total
    if grid[row][col] != 1: # if the tree was not prev sighted
        grid[row][col] = 1
        total += 1

for row in range(1, len(data) - 1):
    left = [data[row][0]]
    right = [data[row][len(data[row]) - 1]]

    # search left view
    for col in range(1, len(data[row]) - 1):
        if all(j < data[row][col] for j in left):
            set(row, col)
            print("left: ", data[row][col])
            left.append(data[row][col])

    # search right view       
    for col in range(len(data[row]) - 1, 0, -1):
        if all(q < data[row][col] for q in right):
            set(row, col)
            print("right: ", data[row][col])
            right.append(data[row][col])

data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]

for row in range(1, len(data) - 1):
    top = [data[row][0]]
    bottom = [data[row][len(data[row]) - 1]]

    # search top view
    for col in range(1, len(data[row]) - 1):
        if all(j < data[row][col] for j in top):
            set(col, row)
            print("top: ", data[row][col])
            top.append(data[row][col])

    # search bottom view       
    for col in range(len(data[row]) - 1, 0, -1):
        if all(q < data[row][col] for q in bottom):
            set(col, row)
            print("bottom: ", data[row][col])
            bottom.append(data[row][col])

for row in grid:
    for col in row:
        print(col),
    print('\n')

print(total)