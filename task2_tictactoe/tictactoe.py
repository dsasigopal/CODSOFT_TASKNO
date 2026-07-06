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

def check_winner(player):
    # Winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw():
    return ' ' not in board
def minimax(board, depth, is_maximizing):
    if check_winner('O'): return 10 - depth
    if check_winner('X'): return depth - 10
    if check_draw(): return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# The Game Loop
while True:
    print_board()
    
    # Human turn
    pos = int(input("Choose your position (0-8): "))
    if make_move(pos, 'X'):
        if check_winner('X'): print("You win!"); break
    else:
        print("Invalid move!"); continue

    # AI turn
    if not check_draw():
        ai_pos = best_move()
        make_move(ai_pos, 'O')
        if check_winner('O'): print("AI wins!"); break
    else:
        print("It's a draw!"); break
        def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
