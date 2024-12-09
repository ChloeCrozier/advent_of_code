# Run with: python day{#}.py {INPUT_PATH}
import sys

data = open(sys.argv[1], 'r').readlines()

ruleDict = {}
ruleMode = True
ordered = True
orderedSum = 0
wrong = []

for line in data:
    if line == '\n':
        ruleMode = False
    else:
        if ruleMode:
            line = line.strip()
            rules = line.split('|')
            if int(rules[0]) in ruleDict:
                ruleDict[int(rules[0])].append(int(rules[1]))
            else:
                ruleDict[int(rules[0])] = [int(rules[1])]
        else:
            line = line.strip()
            updates = line.split(',')
            for i in range(len(updates) - 1):
                if int(updates[i + 1]) in ruleDict:
                    if int(updates[i]) in ruleDict[int(updates[i + 1])]:
                        ordered = False

            # Used for part 2
            if not ordered:
                wrong.append(updates)

        if ordered and not ruleMode:
            results = (line.strip()).split(',')
            orderedSum += int(results[len(results) // 2])
        ordered = True

# Part 1 -------
print(orderedSum)
# --------------

correctedSum = 0

for update in wrong:
    numberPairs = {}
    for num in update:
        num = int(num)
        for entry in update:
            entry = int(entry)
            if num != entry and entry in ruleDict and num in ruleDict[entry]:
    
                if num not in numberPairs:
                    numberPairs[num] = 1
                else:
                    numberPairs[num] += 1

            if num not in numberPairs:
                    numberPairs[num] = 0

    numberPairs = dict(sorted(numberPairs.items(), key=lambda item: item[1]))
    correctedSum += list(numberPairs)[len(numberPairs.items()) // 2]

# Part 2 ----------
print(correctedSum)
# -----------------