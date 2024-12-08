# Run with: python day{#}.py {INPUT_PATH}
import sys

data = open(sys.argv[1], 'r').readlines()

safeReports = 0

def isSafe(nums, sortedNums):
    for i in range(len(nums) - 1):
        diff = int(nums[i]) - int(nums[i + 1])
        if diff == 0:
            return False
        if abs(diff) > 3:
            return False
        if sortedNums[i] != nums[i]:
            return False
    return True

for line in data:
    nums = line.strip().split(' ')
    nums = [int(x) for x in nums]

    if nums[0] < nums[1]:
        sortedNums = sorted(nums)
    else:
        sortedNums = sorted(nums, reverse=True)

    if isSafe(nums, sortedNums):
        safeReports += 1

# Part 1 ---------
print(safeReports)
# ----------------

safeTolerance = 0

for line in data:
    nums = line.strip().split(' ')
    nums = [int(x) for x in nums]

    for i in range(len(nums)):
        removedLevel = nums[0:i] + nums[i + 1:]

        if removedLevel[0] < removedLevel[1]:
            sortedNums = sorted(removedLevel)
        else:
            sortedNums = sorted(removedLevel, reverse=True)

        if isSafe(removedLevel, sortedNums):
            safeTolerance += 1
            break

# Part 2 -----------
print(safeTolerance)
# ------------------