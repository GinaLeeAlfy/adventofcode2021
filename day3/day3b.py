import copy

def createDiagnosticBinary(tallyMap, preFilteredList, checksForMostCommon=True):
    # DiagnosticBinary starts empty
    diagnosticBinary = ""
    # For each character in a line: e.g. 010100011101
    for index in range(lengthOfLine):
        valueToCheck = ""
        # If ones is greater than or equal to the number of 0s in this column
        if tallyMap[index]["ones"] >= tallyMap[index]["zeros"]:
            # Set the winning column value to 1
            if checksForMostCommon:
                valueToCheck = "1"
            else:
                valueToCheck = "0"
        else:
            if checksForMostCommon:
                valueToCheck = "0"
            else:
                valueToCheck = "1"
        preFilteredList = filterList(tallyMap, index, lengthOfLine, preFilteredList, valueToCheck)
        if len(preFilteredList) == 1:
            diagnosticBinary = preFilteredList[0]
            break
    return diagnosticBinary
    

def filterList(tallyMap, index, lengthOfLine, preFilteredList, valueToCheck):
    # Create a new list with the new filtered lines that match our current filter
    newValueList = []
    # Iterate through our current list of values.
    # NOTE: we don't want to modify a list as we are traversing it
    for line in preFilteredList:
        # If the line column matches our filter then its added to our new list
        if line[index] == valueToCheck:
            newValueList.append(line)
        # Else, go through the line and update our tally
        else:
            reduceTally(tallyMap, line, index, lengthOfLine)
    # Now update our original list with the new filtered list
    return newValueList


def reduceTally(tallyMap, currentLine, index, lengthOfLine):
    # Start at the column we are at plus 1 and move to the end
    for lineIndex in range(index + 1, lengthOfLine):
        # Get the character at the current column
        tallyToRemove = ""
        if currentLine[lineIndex] == "1":
            tallyToRemove = "ones"
        else:
            tallyToRemove = "zeros"
        # Remove the character from our tallyDictionary
        tallyMap[lineIndex][tallyToRemove] -= 1

# Open the input file
with open("day3\input3.txt") as puzzleFile:
    oxygenValues = []
    finalOxygenArray = []
    doesArrayNeedInitialization = True
    lengthOfLine = 0
    for line in puzzleFile:
        oxygenValues.append(line)
        if doesArrayNeedInitialization:
            lengthOfLine = len(line) - 1
            for i in range(lengthOfLine):
                finalOxygenArray.append({"ones": 0, "zeros": 0})
            doesArrayNeedInitialization = False
        # For character in the line
        for index, character in enumerate(line):
            # if the character is a 1 add to the 1 tally for that column else add to the 0
            if character == "1":
                finalOxygenArray[index]["ones"] += 1
            elif character == "0":
                finalOxygenArray[index]["zeros"] += 1
    carbonDioxideValues = copy.deepcopy(oxygenValues)
    finalCarbonDioxideArray = copy.deepcopy(finalOxygenArray)

    # Oxygen starts empty
    oxygen = createDiagnosticBinary(finalOxygenArray, oxygenValues)
    carbonDioxide = createDiagnosticBinary(finalCarbonDioxideArray, carbonDioxideValues, False)
    print(int(oxygen, 2) * int(carbonDioxide, 2))
