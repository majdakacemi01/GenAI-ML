matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Welcome to TIC TAC TOE!")

def display_board():
    print("TIC TAC TOE")
    print("****************")
    for i in range(3):
        print(" ", matrix[i][0], "|", matrix[i][1], "|", matrix[i][2])
        if i < 2:
            print(" ---+---+---")
    print("****************")

def player_input(player):
    while True:
            row = int(input(f"Player {player} turn, enter row (1-3): ")) - 1
            column = int(input(f"Player {player} turn, enter column (1-3): ")) - 1

            if row not in [0, 1, 2] or column not in [0, 1, 2]:
                print("Invalid position! Choose numbers between 1 and 3.")
                continue

            if matrix[row][column] != " ":
                print("That spot is already taken! Try again.")
                continue

            matrix[row][column] = player
            break

def check_win(player):
   
    for i in range(3):
        if all(matrix[i][j] == player for j in range(3)) or all(matrix[j][i] == player for j in range(3)):
            return True

    if all(matrix[i][i] == player for i in range(3)) or all(matrix[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie():
    for row in matrix:
        if " " in row:
            return False
    return True


def play():
    current_player = "X"
    display_board()

    while True:
        player_input(current_player)
        display_board()

        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break

        if check_tie():
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play()
