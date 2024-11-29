playBoard = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def printBoard(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print("")


def playTurn(board, player):
    print("PLAYER " + player + "'s TURN")
    spot = input("Pick a spot to play, look at your numpad: ")
    coordinates = getValue(spot)
    if board[coordinates[0]][coordinates[1]] != "-":
        printBoard(playBoard)
        print("Can't overwrite an existing spot!")
        playTurn(board, player)
    else:
        board[coordinates[0]][coordinates[1]] = player
        checkState(board)


def getValue(position):
    match position:
        case "1":
            return [2, 0]
        case "2":
            return [2, 1]
        case "3":
            return [2, 2]
        case "4":
            return [1, 0]
        case "5":
            return [1, 1]
        case "6":
            return [1, 2]
        case "7":
            return [0, 0]
        case "8":
            return [0, 1]
        case "9":
            return [0, 2]


def checkState(board):
    counter = 0
    oList = []
    xList = []
    for row in board:
        for column in row:
            counter += 1
            if column == "O":
                oList.append(counter)
            elif column == "X":
                xList.append(counter)

    combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
        [7, 5, 3],
        [9, 5, 2]
    ]

    for combination in combinations:
        oCounter = 0
        xCounter = 0
        for number in combination:
            if number in oList:
                oCounter += 1
            if number in xList:
                xCounter += 1
        if oCounter == 3:
            game["running"] = False
            printBoard(playBoard)
            print("O WINS! It took " + str(game["round"]) + " turns")
        if xCounter == 3:
            game["running"] = False
            printBoard(playBoard)
            print("X WINS! It took" + str(game["round"]) + "turns")


game = {
    "running": True,
    "player": "O",
    "round": 1
}

while game["running"]:
    printBoard(playBoard)
    playTurn(playBoard, game["player"])
    if game["player"] == "O":
        game["player"] = "X"
        game["round"] += 1
    else:
        game["player"] = "O"
