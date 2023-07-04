"""
Tic Tac Toe Player
"""

import math
import copy

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
    tmpx = 0
    tmpo = 0
    for i in board:
        for j in i:
            if j == X:
                tmpx += 1
            elif j == O:
                tmpo += 1

    if tmpx == tmpo:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    returned = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                returned.add((i, j))
    
    return returned



def result(board, action):
    try:
        if action[0] > 2:
            raise ValueError("Not Good!")
        elif action[1] > 2:
            raise ValueError("Not Good!")
    except:
        raise ValueError("NO")

    try:
        action[2]
        raise ValueError("Not")
    except:
        tmpone = copy.deepcopy(board)
        if player(board) == X:
            tmpone[action[0]][action[1]] = X
        else:
            tmpone[action[0]][action[1]] = O

    return tmpone


def winner(board):
    # left up to right bottom 
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    
    # right up to left bottom
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    
    # 2nd horizon
    if board[1].count(X) == 3:
        return X
    if board[1].count(O) == 3:
        return O
    
    #2nd vertical
    if board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    if board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    
    #1st horizon
    if board[0].count(X) == 3:
        return X
    if board[0].count(O) == 3:
        return O
    
    #3rd verical
    if board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    
    #3rd horizon
    if board[2].count(X) == 3:
        return X
    if board[2].count(O) == 3:
        return O
    
    #1st vertical
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    if board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    
    return None


def terminal(board):
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    goodie = None
    if terminal(board):
        return None
    def maxVal(board):
        v = -9999999999999999999999999
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, minVal(result(board, action)))
        return v

    def minVal(board):
        v = 999999999999999999999999999999999
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, maxVal(result(board, action)))
        return v

    if player(board) == X:
        max_yes = -99999999999999999
        for action in actions(board):
            val = minVal(result(board, action))
            if val >= max_yes:
                goodie = action
                max_yes = val

    else:
        min_yes = 9999999999999999
        for action in actions(board):
            val = maxVal(result(board, action))
            if val <= min_yes:
                goodie = action
                min_yes = val


    return goodie

