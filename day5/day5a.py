class Point:
    def __init__(self, x,y):
        self.x = int(x)
        self.y = int(y)

def parseCoordinatesFromLine(line):
    twoCoordinates = line.split("->")
    x1,y1 = twoCoordinates[0].strip().split(",")
    x2,y2 = twoCoordinates[1].strip().split(",")
    return Point(x1, y1), Point(x2, y2)

def shouldConsider(startPoint, endPoint):
    # NOTE if x == y and x1 == x2 and y1 == y2 we have a point, might need to handle this case
    return (startPoint.x == endPoint.x) or (startPoint.y == endPoint.y)

def updateBoardState(board, pointOne, pointTwo):
    # Horizontal case
    if pointOne.x == pointTwo.x:
        if pointOne.y < pointTwo.y:
            startPoint = pointOne.y
            endPoint = pointTwo.y
        else:
            startPoint = pointTwo.y
            endPoint = pointOne.y
        for column in range(startPoint, endPoint + 1):
            board[pointOne.x][column] += 1
    # Vertical case
    elif pointOne.y == pointTwo.y:
        if pointOne.x < pointTwo.x:
            startPoint = pointOne.x
            endPoint = pointTwo.x
        else:
            startPoint = pointTwo.x
            endPoint = pointOne.x
        for row in range(startPoint, endPoint + 1):
            board[row][pointOne.y] += 1

def calculateAllHazardZones(board, dangerLevel=2):
    numberOfHazardZones = 0
    for row in board:
        for point in row:
            if point >= dangerLevel:
                numberOfHazardZones += 1
    return numberOfHazardZones

# Open the input file
with open("day5\input.txt") as puzzleFile:
    boardSize = 1000
    board = [ [ 0 for i in range(boardSize) ] for j in range(boardSize) ]
    for line in puzzleFile:
        startPoint, endPoint = parseCoordinatesFromLine(line)
        isValid = shouldConsider(startPoint, endPoint)
        if isValid:
            updateBoardState(board, startPoint, endPoint)
    numberOfHazardZones = calculateAllHazardZones(board)
    print(numberOfHazardZones)