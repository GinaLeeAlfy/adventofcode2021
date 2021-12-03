numberOfIncreases = 0
fileAsList = []
start = 0
end = 3

# Open the input file
with open("day1\input1a.txt") as puzzleFile:
    # For every line in the file
    fileAsList = puzzleFile.readlines()

# as long as end is a valid index
while end < len(fileAsList):
    # Get the integer values
    startValue = int(fileAsList[start])
    endValue = int(fileAsList[end])
    # Compare the new value against the old
    if startValue < endValue:
        numberOfIncreases += 1
    start += 1
    end += 1

# Print out final number of increases 
print(numberOfIncreases)