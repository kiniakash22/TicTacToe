# Game of TicTacToe

# displays the current board
def display_board():
    print("\n","-"*6, "Current Board:", "-"*6, "\n")
    for i in range (0, 4):
        for j in range (0, 4):
            print(currentBoard[i][j], end=" "*4)
        print("\n")

# updates the current board with user value
def update_board(x, y, c):
    if currentBoard[x][y] == '-':
        currentBoard[x][y] = c
        return True
    else:
        return False

# checks if all the values are same horizontally
def check_winner_horizontal(check):
    for i in range(1, 4):
        if currentBoard[i][1] == currentBoard[i][2] == currentBoard[i][3] == check:
            return True
    return False

# checks if all the values are same vertically
def check_winner_vertical(check):
    for j in range(1, 4):
        if currentBoard[1][j] == currentBoard[2][j] == currentBoard[3][j] == check:
            return True
    return False

# checks if all the values are same diagonally
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

# checks if user is the winner by calling all the other check methods
def check_winner(check):
    return (check_winner_diagonal(check) or check_winner_horizontal(check) or check_winner_vertical(check))


print("\nWelcome to the game of TicTacToe!")

while True:
    currentBoard = [['.', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
    chars = ['X', 'O']
    validPlay = False
    display_board()
    moves = 0
    while moves < 9:
        while not validPlay:
            check = chars[moves%2]
            print("Player", check , "please enter the position you want to play (x, y):")
            try:
                x = int(input())
                y = int(input())
                if (x < 1 or x > 3) or ( y < 1 or y > 3):
                    print("You've entered an option which is out of bound. Please enter a correct option")
                    continue
            except ValueError:
                print("You've entered an option which is not an Integer. Please enter a correct option")
                continue
            validPlay = update_board(x, y, check)
            if not validPlay:
                print("You've entered an option which already has a play. Please enter a correct option")
        validPlay = False
        display_board()
        if check_winner(check):
            print("Player ", check, " wins!!!")
            break
        moves += 1
    playAgain = input("Press (n/N) to exit or any other key to play again: ").upper()
    if playAgain == 'N':
        print("Thank you for playing. Bye!!!")
        break