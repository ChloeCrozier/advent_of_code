file = open('d1.txt', 'r')
calories = []
value = 0

for line in file:
    if line == '\n':
        calories.append(value)
        value = 0
    else:
        value = value + int(line)

def popMax(lst):
    max = calories[0]
    for i in range (0, len(calories)):
        if max < calories[i]:
            max = calories[i]

    calories.remove(max)
    return max

highest = popMax(calories) 
print('The sum total of the basket with the highest calories', highest)

topThree = highest+ popMax(calories) + popMax(calories)
print('The sum total of the three baskets with the highest calories', topThree)