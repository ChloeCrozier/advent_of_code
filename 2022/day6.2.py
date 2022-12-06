# Part 2
letters = open('d6.txt', 'r').readline().split()[0]
def getIndex():
    for i in range(0, len(letters) - 13):
        if len(set(letters[i:i+14])) == 14:
            return i + 14
print(getIndex())