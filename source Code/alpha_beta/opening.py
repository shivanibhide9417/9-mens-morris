

import sys
import Board
 
maximum = sys.maxsize
minimum = -sys.maxsize

def input_board(inputfile):
    print("Reading file...")
    board = list()
    for line in inputfile:
        for ch in line:
            board.append(ch)
    return board


def static_estimation_function(board):
    white_count = 0
    black_count = 0
    total_count = 0
    for position in range(0,len(board)):
        if(board[position]=="W"):
            white_count+=1
        if(board[position]=="B"):
            black_count+=1
    total_count = white_count-black_count;
    return total_count

def alpha_beta_open(d,board,alpha,beta,flag):
    inp = Board.createObject()
    op = Board.createObject()
    boardPositionList = list()
    if(d==0):
        
        total_count = static_estimation_function(board)
        op.value = total_count
        op.stateCount = op.stateCount +1
        return op
    if(flag==1):
        boardPositionList = Board.generate_opening_moves(board)
      
    else:
      
        boardPositionList = Board.opening_moves_black(board)
       
        
    for bposition in boardPositionList:
        if(flag==1):
            inp = alpha_beta_open(d-1,bposition,alpha,beta, 0)
            if (inp.value > alpha):
                alpha = inp.value
                op.boardState = bposition
            op.stateCount = op.stateCount + inp.stateCount
        else:
             inp = alpha_beta_open(d-1,bposition,alpha,beta, 1)
             if (inp.value < beta):
                beta = inp.value
                op.boardState = bposition
             op.stateCount = op.stateCount + inp.stateCount
        if(alpha>=beta):
            break
    if (flag==1):
        op.value =alpha
    else:
        op.value = beta
    return op

def board_output(board):
   
    outputfile = open(sys.argv[2],"w")
    
    for ch in board:
        outputfile.write(ch)
    outputfile.close()


inputfile = open(sys.argv[1])
depth = int(sys.argv[3])  
board = input_board(inputfile)
out = alpha_beta_open(depth,board,minimum,maximum,1)
print("Next state:",''.join(out.boardState))
print("states evaluated:",out.stateCount)
print("estimate value:",out.value)

board_output(out.boardState)
inputfile.close()
