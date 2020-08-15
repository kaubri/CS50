"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


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
    moves = 0

    if board == initial_state():
        return X

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                moves += 1

    if moves % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_result = copy.deepcopy(board)
    board_result[action[0]][action[1]] = player(board)
    return board_result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for horizontal win
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    # Check for vertical win
    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O

    # Check for diagonal win
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) \
            or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) \
            or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return EMPTY

    if player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]


def max_value(board):
    v = -math.inf
    optimal_action = EMPTY

    if terminal(board):
        return utility(board), EMPTY

    for action in actions(board):
        opponent_move = min_value(result(board, action))
        if opponent_move[0] > v:
            v = opponent_move[0]
            optimal_action = action

            if v == 1:
                return v, optimal_action

    return v, optimal_action


def min_value(board):
    v = math.inf
    optimal_action = EMPTY

    if terminal(board):
        return utility(board), EMPTY

    for action in actions(board):
        opponent_move = max_value(result(board, action))
        if opponent_move[0] < v:
            v = opponent_move[0]
            optimal_action = action

            if v == -1:
                return v, optimal_action

    return v, optimal_action
