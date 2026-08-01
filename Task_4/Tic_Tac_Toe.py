import math


# Empty game board
board = [" " for _ in range(9)]


def show_position_guide():
    """Display the position numbers available to the player."""

    print("\nPosition Guide:\n")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()


def show_board():
    """Display the current game board."""

    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    """Check whether the given player has won."""

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for positions in winning_positions:
        if all(board[position] == player for position in positions):
            return True

    return False


def board_is_full():
    """Check whether all positions have been used."""

    return " " not in board


def minimax(ai_turn):
    """Check future moves and return the best possible score."""

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_is_full():
        return 0

    if ai_turn:
        best_score = -math.inf

        for position in range(9):
            if board[position] == " ":
                board[position] = "O"

                score = minimax(False)

                board[position] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for position in range(9):
            if board[position] == " ":
                board[position] = "X"

                score = minimax(True)

                board[position] = " "

                best_score = min(best_score, score)

        return best_score


def computer_move():
    """Choose the best move for the computer."""

    best_score = -math.inf
    best_position = None

    for position in range(9):
        if board[position] == " ":
            board[position] = "O"

            score = minimax(False)

            board[position] = " "

            if score > best_score:
                best_score = score
                best_position = position

    if best_position is not None:
        board[best_position] = "O"


def player_move():
    """Take a valid position from the player."""

    while True:
        try:
            position = int(
                input("Enter your position from 1 to 9: ")
            ) - 1

            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")

            elif board[position] != " ":
                print("This position is already occupied.")

            else:
                board[position] = "X"
                break

        except ValueError:
            print("Please enter a valid number.")


def start_game():
    """Control the complete game."""

    print("=" * 45)
    print("         CODSOFT TIC-TAC-TOE AI")
    print("=" * 45)

    print("\nYou are X.")
    print("The computer is O.")

    show_position_guide()

    while True:
        show_board()

        player_move()

        if check_winner("X"):
            show_board()
            print("Congratulations! You won.")
            break

        if board_is_full():
            show_board()
            print("The game is a draw.")
            break

        print("\nComputer is choosing the best move...")

        computer_move()

        if check_winner("O"):
            show_board()
            print("The computer won the game.")
            break

        if board_is_full():
            show_board()
            print("The game is a draw.")
            break


start_game()