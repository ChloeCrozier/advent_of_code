# Part 1
letters = open('d6.txt', 'r').readline().split()[0]
def getIndex():
    for i in range(0, len(letters) - 3):
        if len(set(letters[i:i+4])) == 4:
            return i + 4
print(getIndex())