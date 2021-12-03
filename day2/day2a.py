horizontal = 0
depth = 0

def parseCommand(command, value):
    # Editing the global variables
    global horizontal
    global depth
    # Value needs to be int for final calculation
    valueAsInt = int(value)
    # Switch on command
    if command == "forward":
        horizontal += valueAsInt
    elif command == "up":
        depth -= valueAsInt
    elif command == "down":
        depth += valueAsInt

def parseInput(line):
    command, value = line.split()
    parseCommand(command, value)

# Open the input file
with open("day2\input2.txt") as puzzleFile:
    for line in puzzleFile:
        parseInput(line)

print(horizontal * depth)
