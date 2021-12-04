
def parseNumbers(line):
    return line.split(",")

def parseBoards(puzzleFileAsList):
    listOfBoards = []
    mapOfNumbers = {}
    currentBoard = []
    currentBoardNumber = 0
    i = 0
    for line in puzzleFileAsList:
        if line != "\n":
            charactersAsAList = line.strip().split()
            currentBoard.append(charactersAsAList)
            for j, character in enumerate(charactersAsAList):
                if character in mapOfNumbers:
                    mapOfNumbers[character].append([currentBoardNumber, i, j])
                else:
                    mapOfNumbers[character] = [[currentBoardNumber, i, j],]
            i += 1
        else:
            listOfBoards.append(currentBoard)
            currentBoard = []
            currentBoardNumber += 1
            i = 0
    listOfBoards.append(currentBoard)
    return listOfBoards, mapOfNumbers

def playBingo(board, row, col):
    isFinished = True
    board[row][col] = "T"
    # Look through the row to see if its complete
    for character in board[row]:
        if character != "T":
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
    for line in board:
        for character in line:
            if character.isnumeric():
                runningSum += int(character)
    return runningSum * int(number)

# Open the input file
with open("day4\input4.txt") as puzzleFile:
    puzzleFileAsList = puzzleFile.readlines()
    numbersToBeCalled = parseNumbers(puzzleFileAsList[0])
    listOfBoards, mapOfNumbers = parseBoards(puzzleFileAsList[2:])
    isFinished = False
    for number in numbersToBeCalled:
        for boardNumber, row, col in mapOfNumbers[number]:
            board = listOfBoards[boardNumber]
            isFinished = playBingo(board, row, col)
            if isFinished:
                winningNumber = calculatePoints(board, number)
                print(winningNumber)
                break
        if isFinished:
            break

    
