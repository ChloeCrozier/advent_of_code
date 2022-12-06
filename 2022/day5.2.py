# Part 2
stacks = []
stack = []
topCrates = ''

def moveCrate(num, start, dest):
    # print(stacks[start - 1][~num + 1:])
    stacks[dest - 1] += stacks[start - 1][~num + 1:]
    stacks[start - 1] = stacks[start - 1][:-num]

for line in open('d5.txt', 'r').readlines():
    if(line[0] != 'm' and len(line) > 1):
        for i in range(0, len(line), 4):
            stack.append(line[i + 1])
        stacks.insert(0, stack)
        stack = []
    elif len(line) == 1:
        stacks = [*zip(*stacks)]
        for i in range(0, len(stacks)):
            stacks[i] = [x for x in stacks[i] if x != ' ']
    else:
        moveCrate(int(line.split()[1]), int(line.split()[3]), int(line.split()[5]))

for i in range(0, len(stacks)):
    topCrates = topCrates + stacks[i].pop()

print(topCrates)