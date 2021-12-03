
currentValue = -1
numberOfIncreases = 0
fileAsList = []

# Open the input file
with open("day1\input1a.txt") as puzzleFile:
    # For every line in the file
    fileAsList = puzzleFile.readlines()

# Iterate through the list size minus 2
for index in range(len(fileAsList)- 2):
    # Get the next three values
    currentWindow0 = int(fileAsList[index])
    currentWindow1 = int(fileAsList[index+1])
    currentWindow2 = int(fileAsList[index+2])
    currentSum = currentWindow0 + currentWindow1 + currentWindow2
    # if there is an increase in depth and its not the first value
    if currentSum > currentValue and currentValue != -1:
        numberOfIncreases += 1
    # Eitherway we want to update our current depth
    currentValue = currentSum

# Print out final number of increases 
print(numberOfIncreases)