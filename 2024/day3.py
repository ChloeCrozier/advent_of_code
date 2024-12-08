# Run with: python day{#}.py {INPUT_PATH}
import sys
import re
data = open(sys.argv[1], 'r').readlines()

p1Total = 0

for line in data:
    line = line.strip()

    # This fidns all instances of 'mul(#,#)' within a line
    matches = re.findall(r'(mul\(\d+,\d+\))', line)

    for match in matches:
        splitMatch = re.split('(\d+)', match)
        p1Total += int(splitMatch[1]) * int(splitMatch[3])

# Part 1 -----
print(p1Total)
# ------------

multiply = True
p2Total = 0

for line in data:
    line = line.strip()

    # This finds all instances of 'mul(#,#)', 'do()', or 'don't()' within a line
    # The result is a touple where the index is which one matched ie. ('', 'do()', '')
    matches = re.findall(r'(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))', line)

    for match in matches:
        match = list(filter(None, match))[0]
        if match == 'don\'t()':
            multiply = False
        if match == 'do()':
            multiply = True
        else:
            if multiply == True:
                splitMatch = re.split('(\d+)', match)
                p2Total += int(splitMatch[1]) * int(splitMatch[3])

# Part 3 -----              
print(p2Total)
# ------------
