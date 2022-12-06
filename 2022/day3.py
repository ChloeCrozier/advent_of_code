# part 1
f = open('d3.txt', 'r')
total = 0

def getPriority(letter):
    if((letter).islower()):
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

for line in f:
    total = total + getPriority(list(set(line[0:len(line)/2]).intersection(line[len(line)/2:len(line)])).pop())

print(total)


#part 2
total = 0

def getPriority(letter):
    letter.sort(reverse = True)
    if(letter[0].islower()):
        return ord(letter[0]) - 96
    else:
        return ord(letter[0]) - 64 + 26

for group in list(zip(*[iter(open('d3.txt', 'r').readlines())]*3)):
    total = total + getPriority(list(set(group[0]).intersection(group[1]).intersection(group[2])))

print(total)