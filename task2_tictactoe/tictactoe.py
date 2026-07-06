# Simple Tic-Tac-Toe Board
board = [' ' for _ in range(9)]

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# Test the board display
print_board()

def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Example: Player 'X' makes a move at position 4 (the center)
make_move(4, 'X')
print_board()
