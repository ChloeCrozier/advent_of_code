import sys
data = (open(sys.argv[1], 'r')).readlines()

left = []
right = []

for line in data:
    vals = line.split('   ')
    left.append(int(vals[0]))
    right.append(int(vals[1][0:-1]))

left.sort()
right.sort()
totalDist = 0

for i in range(len(left)):
    totalDist += max(left[i], right[i]) - min(left[i], right[i])

# Part 1 -------
print(totalDist)
# --------------

rightMap = {}
for num in right:
    if num in rightMap:
        rightMap[num] += 1
    else:
        rightMap[num] = 1

similarity = 0

for num in left:
    if num in rightMap:
        similarity += num * rightMap[num]

# Part 1 --------
print(similarity)
# ---------------