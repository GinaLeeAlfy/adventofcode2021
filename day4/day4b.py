# Split the line by commas
def parseNumbers(line):
    return line.strip().split(",")

def parseBoards(puzzleFileAsList):
    # Initialize our final list of boards, and map of character locations
    listOfBoards = []
    mapOfNumbers = {}
    # Track the current board being worked on
    currentBoard = []
    currentBoardNumber = 0
    # Track the current row being worked on
    i = 0
    # For each line in the input
    for line in puzzleFileAsList:
        # This line contains text
        if line != "\n":
            # Remove all newline characters and split on whitespace
            charactersAsAList = line.strip().split()
            # This line of numbers is added to the current board
            currentBoard.append(charactersAsAList)
            # Iterate through the line in column, character data notation
            for j, character in enumerate(charactersAsAList):
                # If the character is already in our map, append to the end
                if character in mapOfNumbers:
                    mapOfNumbers[character].append([currentBoardNumber, i, j])
                # Else create a new list
                else:
                    mapOfNumbers[character] = [[currentBoardNumber, i, j],]
            # Increment our row counter
            i += 1
        # This is an empty line so our board is done
        else:
            # Append our board to our list of boards
            listOfBoards.append(currentBoard)
            # Reset our board trackers
            currentBoard = []
            currentBoardNumber += 1
            i = 0
    # Remember to add the final board to the list of boards
    listOfBoards.append(currentBoard)
    # Return our generated list of boards and map of character locations
    return listOfBoards, mapOfNumbers

def playBingo(board, row, col):
    # Assume this is the winning line
    isFinished = True
    # Set this Value to called, i.e. T
    board[row][col] = "T"
    # Look through the row to see if its complete
    for character in board[row]:
        if character != "T":
            # Since the character is not T then we aren't finished yet
            isFinished = False
            break
    # Look through the column to see if its complete
    if not isFinished:
        isFinished = True
        for lineNumber in range(len(board)):
            if board[lineNumber][col] != "T":
                isFinished = False
                break
    return isFinished

def calculatePoints(board, number):
    runningSum = 0
    # Go through all values in the board and add them up
    for line in board:
        for character in line:
            if character.isnumeric():
                runningSum += int(character)
    # Final value is sum times winning number
    return runningSum * int(number)

# Open the input file
with open("day4\input4.txt") as puzzleFile:
    # Convert the input text into a list of strings
    puzzleFileAsList = puzzleFile.readlines()
    # Take the first line and convert it to numbers to be called
    numbersToBeCalled = parseNumbers(puzzleFileAsList[0])
    # Traverse the rest of the input and create our list of boards and map of character locations.
    listOfBoards, mapOfNumbers = parseBoards(puzzleFileAsList[2:])
    # Start with a non-finished state
    isFinished = False
    listOfWinningBoards = {}
    lastBoardNumber = -1
    # Iterate through all numbers to be called
    for number in numbersToBeCalled:
        # For every board in our map of character locations
        for boardNumber, row, col in mapOfNumbers[number]:
            if boardNumber in listOfWinningBoards:
                continue
            # Convert our boardnumber to actual board structure
            board = listOfBoards[boardNumber]
            # Update our board
            isFinished = playBingo(board, row, col)
            # If we won
            if isFinished:
                # Calculate our winnings
                listOfWinningBoards[boardNumber] = number
                lastBoardNumber = boardNumber
    finalBoard = listOfBoards[lastBoardNumber]
    winningNumber = calculatePoints(finalBoard, listOfWinningBoards[lastBoardNumber])
    print(winningNumber)

    
