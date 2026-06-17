def check_winner(board, mark):
    return (
        (board[0] == mark and board[1] == mark and board[2] == mark) or
        (board[3] == mark and board[4] == mark and board[5] == mark) or
        (board[6] == mark and board[7] == mark and board[8] == mark) or
        (board[0] == mark and board[3] == mark and board[6] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[0] == mark and board[4] == mark and board[8] == mark) or
        (board[2] == mark and board[4] == mark and board[6] == mark)
    )

print("Welcome to Tic Tac Toe!")

player1 = input("Enter Player 1 name (X): ")
player2 = input("Enter Player 2 name (O): ")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while True:

    # Player 1 turn
    position = int(input(player1 + " Enter position for X (0-8): "))

    if board[position] == " ":
        board[position] = "X"
    else:
        print("Position already occupied!")
        continue

    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

    if check_winner(board, "X"):
        print(player1, "wins!")
        break

    # Player 2 turn
    position = int(input(player2 + " Enter position for O (0-8): "))

    if board[position] == " ":
        board[position] = "O"
    else:
        print("Position already occupied!")
        continue

    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

    if check_winner(board, "O"):
        print(player2, "wins!")
        break