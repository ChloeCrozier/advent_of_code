import heapq

f = open('d1.txt', 'r')
values = []
total = 0

for line in f:
    if line != '\n':
        total = total + int(line)
    else:
        heapq.heappush(values, total)
        total = 0

print('The sum total of the basket with the highest calories', sum(heapq.nlargest(1, values)))
print('The sum total of the three baskets with the highest calories', sum(heapq.nlargest(3, values)))
