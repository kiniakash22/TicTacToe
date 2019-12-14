
def display_board():
    print("-"*6, "Current Board:", "-"*6, "\n")
    for i in range (0, 4):
        for j in range (0, 4):
            print(currentBoard[i][j], end=" "*4)
        print("\n")

def update_board(x, y, c):
    if currentBoard[x][y] == '-':
        currentBoard[x][y] = c
        return True
    else:
        return False

def check_winner_horizontal(check):
    for i in range(1, 4):
        if currentBoard[i][1] == currentBoard[i][2] == currentBoard[i][3] == check:
            return True
    return False

def check_winner_vertical(check):
    for j in range(1, 4):
        if currentBoard[1][j] == currentBoard[2][j] == currentBoard[3][j] == check:
            return True
    return False

def check_winner_diagonal(check):
    flagLD = True
    flagRD = True
    for i in range (1, 4):
        for j in range (1, 4):
            #left diagonal
            if i==j:
                if currentBoard[i][j] != check:
                    flagLD = False
            #right diagonal
            if i+j == 4:
                if currentBoard[i][j] != check:
                    flagRD = False           
    if flagLD or flagRD: return True
    else: return False

def check_winner(check):
    return (check_winner_diagonal(check) or check_winner_horizontal(check) or check_winner_vertical(check))


print("Welcome to the game of TicTacToe!")

currentBoard = [[' ', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
validPlayX = False
validPlayO = False
display_board()
moves = 9
while moves > 0:
    while not validPlayX:
        print("Player X please enter your option:")
        x = int(input())
        y = int(input())
        validPlayX = update_board(x, y, 'X')
        if not validPlayX:
            print("You've entered an incorrect option. Please enter a correct option")
    validPlayX = False
    display_board()
    if check_winner("X"):
        print("Player X wins!!!")
        break

    while not validPlayO:
        print("Player O please enter your option:")
        x = int(input())
        y = int(input())
        validPlayO = update_board(x, y, 'O')
    validPlayO = False
    display_board()
    if check_winner("O"):
        print("Player O wins!!!")
        break
    moves -= 1
