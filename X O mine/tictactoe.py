X = "X"
O = "O"
EMPTY = None


def initial_state():
    """Returns the initial state of the Tic-Tac-Toe board."""
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """Returns the player who has the next move."""
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """Returns a set of all possible actions (i, j) on the board."""
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """Returns the board after making a move."""
    if action not in actions(board):
        raise ValueError("Invalid move")

    i, j = action
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """Returns the winner if there is one."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """Returns True if the game is over, False otherwise."""
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """Returns +1 if X wins, -1 if O wins, 0 otherwise."""
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0


def minimax(board):
    """Returns the best possible move for the AI."""
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -float("inf")
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = float("inf")
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float("inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
