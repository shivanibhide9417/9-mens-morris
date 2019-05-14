

import sys
import Board

maximum = sys.maxsize
minimum = -sys.maxsize

def input_board(inputfile):
    board = list()
    for line in inputfile:
        for ch in line:
            board.append(ch)
    return board

def minimax_black(d,board,flag):
    out = Board.createObject()
    inp = Board.createObject()
    
    if(d==0):
        white_count = 0
        black_count = 0
        total_count = 0
        for position in range(0,len(board)):
            if(board[position]=="W"):
                white_count+=1
            if(board[position]=="B"):
                black_count+=1
        total_count = black_count-white_count
        l = Board.generate_moves_midgameEndgame(board)
        listsize = len(l)
        if(black_count<=2):
            out.value = 10000
        elif(white_count<=2):
            out.value = -10000
        elif(listsize==0):
            out.value = 10000
        else:
            out.value = 1000*(total_count)-listsize
        out.stateCount = out.stateCount+1
        out.boardState = board
       
        return out
    listofMoves = list()
    if(flag==1):
        
        listofMoves = Board.generate_moves_midgameEndgame_black(board)
        out.value = minimum
    else:
        listofMoves = Board.generate_moves_midgameEndgame(board)
        out.value = maximum
    
    for b in listofMoves:
        if(flag==1):
            inp = minimax_black(d-1,b,0)
            if(inp.value> out.value):
                out.value = inp.value
                out.boardState = b
            out.stateCount = out.stateCount + inp.stateCount
        else:
            inp = minimax_black(d-1,b,1)
            if(inp.value< out.value):
                out.value = inp.value
                out.boardState = b
            out.stateCount = out.stateCount + inp.stateCount
    return out

def board_output(board):
    outputfile = open(sys.argv[2],"w")
    
    for ch in board:
        outputfile.write(ch)
    outputfile.close()

    
    
#main
inputfile = open(sys.argv[1])
board = list()
depth = int(sys.argv[3])   
board = input_board(inputfile)
out = minimax_black(depth,board,1)

print("Next state:",''.join(out.boardState))
print("states evaluated:",out.stateCount)
print("estimate value:",out.value)

board_output(out.boardState)
inputfile.close()
