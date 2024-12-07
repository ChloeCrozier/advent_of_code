stateGrid = [['*'] * 6] * 6
stateGrid[0][0] = 'S'
traveledGrid = [['*'] * 6] * 6
traveledGrid[5][0] = '#'
traveled = 0

for row in stateGrid:
    print(row)

print('\n\n')

for entry in open('test.txt', 'r').readlines():
    print(entry)

# def follow(direction):
    