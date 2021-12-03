
currentValue = -1
numberOfIncreases = 0

# Open the input file
with open("day1\input1a.txt") as puzzleFile:
    # For every line in the file
    for line in puzzleFile:
        # Convert string to integer
        valueAsInt = int(line)
        # if there is an increase in depth and its not the first value
        if valueAsInt > currentValue and currentValue != -1:
            numberOfIncreases += 1
        # Eitherway we want to update our current depth
        currentValue = valueAsInt

# Print out final number of increases 
print(numberOfIncreases)