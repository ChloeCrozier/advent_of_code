total1 = 0
total2 = 0

def fullyContains(a1, a2, b1, b2):
    if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
        return 1
    return 0

def overlaps(a1, a2, b1, b2):
    if len([value for value in [i for i in range(a1, a2 + 1)] if value in [i for i in range(b1, b2 + 1)]]) > 0:
        return 1
    return 0


for line in open('d4.txt', 'r').readlines():
    a, b = line.split(',')[0], line.split(',')[1]
    a1, a2, b1, b2 = a.split('-')[0], a.split('-')[1], b.split('-')[0], b.split('-')[1]
    total1 = total1 + fullyContains(int(a1), int(a2), int(b1), int(b2))
    total2 = total2 + overlaps(int(a1), int(a2), int(b1), int(b2))

# Part 1
print(total1)
# Part 2
print(total2)