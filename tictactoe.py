"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
E = EMPTY = None


class BoardNode():
    def __init__(self, action, value):
        self.action = action
        self.value = value


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = num_o = 0

    for row in board:
        for square in row:
            if square == X:
                num_x += 1
            elif square == O:
                num_o += 1

    return X if num_x == num_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i, j))

    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError

    new_board = deepcopy(board)

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal check
    for row in board:
        win = row[0]
        if row[1] == win and row[2] == win and win:
            return win

    # Vertical check
    for j in range(3):
        win = board[0][j]
        if board[1][j] == win and board[2][j] == win and win:
            return win

    # Main diagonal check
    win = board[0][0]
    if board[1][1] == win and board[2][2] == win and win:
        return win

    # Secondary diagonal check
    win = board[0][2]
    if board[1][1] == win and board[2][0] == win and win:
        return win

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    # Checks if board is full
    for row in board:
        for square in row:
            if not square:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1

    if win == O:
        return -1

    return 0


def recursive(board):
    """
    Recursive function that takes a board and returns the
    node with the best action and its utility.
    """
    if terminal(board):
        return BoardNode(None, utility(board))

    # k factor to differentiate players
    k = 1 if player(board) == O else -1

    minimax_node = BoardNode(None, k * 2)

    for action in actions(board):
        node = recursive(result(board, action))

        if k * node.value < k * minimax_node.value:
            minimax_node.value = node.value
            minimax_node.action = action

    return minimax_node


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return recursive(board).action
