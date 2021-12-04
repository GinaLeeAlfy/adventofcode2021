

# Open the input file
with open("day3\input3.txt") as puzzleFile:
    finalArray = []
    doesArrayNeedInitialization = True
    for line in puzzleFile:
        if doesArrayNeedInitialization:
            lengthOfLine = len(line) - 1
            for i in range(lengthOfLine):
                finalArray.append({"ones": 0, "zeros": 0})
            doesArrayNeedInitialization = False
        # For character in the line
        for index, character in enumerate(line):
            # if the character is a 1 add to the 1 tally for that column else add to the 0
            if character == "1":
                finalArray[index]["ones"] += 1
            elif character == "0":
                finalArray[index]["zeros"] += 1
    gamma = ""
    epsilon = ""
    # for value in array see which is greater and thats the value for gamma
    for characterTally in finalArray:
        if characterTally["ones"] > characterTally["zeros"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    # Convert string of binary numbers to an integer
    gammaAsInt = int(gamma, 2)
    epsilonAsInt = int(epsilon, 2)
    print(gammaAsInt * epsilonAsInt)
