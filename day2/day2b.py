horizontal = 0
depth = 0
aim = 0

def parseCommand(command, value):
    # Editing the global variables
    global horizontal
    global depth
    global aim
    # Value needs to be int for final calculation
    valueAsInt = int(value)
    # Switch on command
    if command == "forward":
        horizontal += valueAsInt
        depth += valueAsInt * aim
    elif command == "up":
        aim -= valueAsInt
    elif command == "down":
        aim += valueAsInt

def parseInput(line):
    command, value = line.split()
    parseCommand(command, value)

# Open the input file
with open("day2\input2.txt") as puzzleFile:
    for line in puzzleFile:
        parseInput(line)

print(horizontal * depth)
