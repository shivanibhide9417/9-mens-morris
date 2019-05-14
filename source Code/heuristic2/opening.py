

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
    count = 0
    for position in range(0,len(board)):
        if(board[position]=="W"):
            white_count+=1
        if(board[position]=="B"):
            black_count+=1
    total_count = white_count-black_count
    for i in range(0,len(board)):
        if(board[i]=="x"):
            if(Board.forms_mill(i,board,"W")==True):
                count+=1
    return total_count+count

def minimax_h2(d,board,flag):
    

    op = Board.createObject()
    inp = Board.createObject()
    boardPositionList = list()
    if(d==0):
        
        finalcount = static_estimation_function(board)
        op = Board.createObject(finalcount,op.stateCount+1,board)
        return op
        
    if(flag==1):
        #print(board)
        boardPositionList = Board.generate_opening_moves(board)
        op.value = minimum
    else:
        #print(board)
        boardPositionList = Board.opening_moves_black(board)
        #print(boardPositionList)
        op.value = maximum
    
    
    for boardPosition in boardPositionList:
        if(flag==1):
            inp = minimax_h2(d-1,boardPosition,0)
            if(inp.value>op.value):
                op.value = inp.value
                op.boardState = boardPosition
            op.stateCount = op.stateCount + inp.stateCount
        else:
            inp = minimax_h2(d-1,boardPosition,1)
            if(inp.value<op.value):
                op.value = inp.value
                op.boardState = boardPosition
            op.stateCount = op.stateCount + inp.stateCount
    return op    

def board_output(board):
   
    outputfile = open(sys.argv[2],"w")
    
    for ch in board:
        outputfile.write(ch)
    outputfile.close()                      

#Main
inputfile = open(sys.argv[1])
depth = int(sys.argv[3]) 
board = input_board(inputfile)
out = minimax_h2(depth,board,1)

print("Next State:",''.join(out.boardState))
print("States evaluated:",out.stateCount)
print("Estimate value:",out.value)

board_output(out.boardState)
inputfile.close()

  


