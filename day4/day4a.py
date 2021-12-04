
def parseNumbers(line):
    return line.split(",")

def parseBoards(puzzleFileAsList):
    listOfBoards = []
    currentBoard = []
    for line in puzzleFileAsList:
        if line != "\n":
            currentBoard.append(line.strip().split())
        else:
            listOfBoards.append(currentBoard)
            currentBoard = []
    return listOfBoards

def playBingo(board, number):
    col = -1
    row = -1
    found = False
    isFinished = False
    for i, line in enumerate(board):
        for j, character in enumerate(line):
            if character == number:
                col = j
                row = i
                found = True
                break
        if found:
            break
    if found:
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
    listOfBoards = parseBoards(puzzleFileAsList[2:])
    isFinished = False
    for number in numbersToBeCalled:
        for board in listOfBoards:
            isFinished = playBingo(board, number)
            if isFinished:
                winningNumber = calculatePoints(board, number)
                print(winningNumber)
                break
        if isFinished:
            break

    
