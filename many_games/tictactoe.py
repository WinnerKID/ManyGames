import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):  # Check rows
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):  # Check diagonals
        return True
    return False

def player_move(board, row, col):
    if board[row - 1][col - 1] == " ":
        board[row - 1][col - 1] = "X"
        return True
    else:
        return False

def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

def start_game():
    print("Let's play Tic-Tac-Toe!\nYou'll be the X and i'll be the O!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
        if player_move(board, row, col):
            display_board(board)
            if check_win(board, "X"):
                print("Congratulations! You win!")
                break
            if not any(" " in row for row in board):
                print("It's a draw!")
                break

            computer_move_row, computer_move_col = computer_move(board)
            if computer_move_row is not None:
                print(f"Computer's move: {computer_move_row} {computer_move_col}")
                board[computer_move_row][computer_move_col] = "O"
                display_board(board)
                if check_win(board, "O"):
                    print("Computer wins!")
                    break
            else:
                print("It's a draw!")
                break

if __name__ == "__main__":
    start_game()
