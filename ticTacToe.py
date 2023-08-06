from random import choice
import numpy as np
import collections

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def Clearboard(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def winningPlayer(board, player):
    conditions = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]

    if [player, player, player] in conditions:
        return True

    return False

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def printResult(board):
    return
    if winningPlayer(board, 1):
        print('X has won! ' + '\n')

    elif winningPlayer(board, -1):
        print('O\'s have won! ' + '\n')

    else:
        print('Draw' + '\n')

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])

    return blank

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def boardFull(board):
    if len(blanks(board)) == 0:
        return True
    return False

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def setMove(board, x, y, player):
    board[x][y] = player



#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def getScore(board):
    if winningPlayer(board, 1):
        return 10

    elif winningPlayer(board, -1):
        return -10

    else:
        return 0

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def abminimax(board, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or gameWon(board):
        return [row, col, getScore(board)]

    else:
        for cell in blanks(board):
            setMove(board, cell[0], cell[1], player)
            score = abminimax(board, depth - 1, alpha, beta, -player)
            if player == 1:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]

            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            setMove(board, cell[0], cell[1], 0)

            if alpha >= beta:
                break

        if player == 1:
            return [row, col, alpha]

        else:
            return [row, col, beta]

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def o_comp(board):
    if len(blanks(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        setMove(board, x, y, -1)
        Gameboard(board)
        return x, y

    else:
        result = abminimax(board, len(blanks(board)), float("-inf"), float("inf"), -1)
        # print(result)
        setMove(board, result[0], result[1], -1)
        Gameboard(board)
        return result[0], result[1]

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def x_comp(board):
    if len(blanks(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        setMove(board, x, y, 1)
        Gameboard(board)
        return x, y

    else:
        result = abminimax(board, len(blanks(board)), float("-inf"), float("inf"), 1)
        # print(result)
        setMove(board, result[0], result[1], 1)
        Gameboard(board)
        return result[0], result[1]

#https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning/blob/main/tictactoe%20using%20alphabetapruning.py
def makeMove(board, player, mode):
    if mode == 1:
        if player == 1:
            playerMove(board)

        else:
            o_comp(board)
    else:
        if player == 1:
            o_comp(board)
        else:
            x_comp(board)










#mein Quellcode
def hilfsfunktion(board):
    for numberi,spalte in enumerate(board):
        for numberj,symbol in enumerate(spalte):
            if (symbol == 'X'):
                board[numberi][numberj] = 1
            if (symbol == 'O'):
                board[numberi][numberj] = -1
            if (symbol == '-'):
                board[numberi][numberj] = 0
    winner = None
    me = None
    if(len(blanks(board))%2 == 0):
        x,y = o_comp(board)
        me = 0 
        
    elif(len(blanks(board))%2 == 1):
        x,y = x_comp(board)
        me = 1 
        
    if(gameWon(board)):
        if(winningPlayer(board, 1)):
            if(me == 1):
                winner = 1
            else:
                winner = -1
        if(winningPlayer(board, -1)):
            if(me == 0):
                winner = 1
            else:
                winner = -1
            
    if(len(blanks(board)) == 0):
        if(winningPlayer(board, 1)):
            if(me == 1):
                winner = 1
            else:
                winner = -1
        elif(winningPlayer(board, -1)):
            if(me == 0):
                winner = 1
            else:
                winner = -1
        else:
            winner = 0
    
    return x,y,winner
    
#mein Quellcode
def solve(board):
    x,y,winner = hilfsfunktion(board)
    everythingfine = np.array(board).flatten()
    
    if(collections.Counter(everythingfine)[1] == collections.Counter(everythingfine)[-1] or collections.Counter(everythingfine)[1] - 1 == collections.Counter(everythingfine)[-1]):
        if((x*3 + y + 1) >= 0):
            return((x*3 + y + 1), winner)
        else:
            return(None, winner)
    else:
        return(None, None)
        
        
if __name__ == "__main__":
    board = [['O', '-', '-'], ['-', 'X', '-'], ['-', '-', '-']]
    print(solve(board))
