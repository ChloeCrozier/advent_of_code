directory = {}
curr = []

for line in open('d7.txt', 'r').readlines():
    line = line[0:len(line) - 1].split()
    if len(line) > 1 and line[1] == 'cd' and line[2] != '..':
        curr.append(line[2])
        directory[str(curr)] = 0
    if len(line) > 1 and line[1] == 'cd' and line[2] == '..':
        curr.pop()
    if len(line) > 1 and line[0] != '$' and line[0] != 'dir':
        for i in range(0, len(curr)):
            directory[str(curr[0: len(curr) - i])] += int(line[0])

for key, value in directory.items():
    print(key, value)

print(sum([value for key, value in directory.items() if value <= 100000]))