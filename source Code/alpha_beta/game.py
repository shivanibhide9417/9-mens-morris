
import sys
import Board
 
maximum = sys.maxsize
minimum = -sys.maxsize

#Input-open file
def read_board(inputfile):
    print("Reading file..")
    board = list()
    for line in inputfile:
        for ch in line:
            board.append(ch)
    return board

#calculate static estimation value
def staticEstimationOpening(board):
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

def alpha_beta_game(d,board,alpha,beta,flag):
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
        total_count = white_count-black_count
        l = Board.generate_moves_midgameEndgame_black(board)
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
        return out
    list_of_moves = list()
    if(flag==1):
        
        list_of_moves = Board.generate_moves_midgameEndgame(board)
        
    else:
        list_of_moves = Board.generate_moves_midgameEndgame_black(board)
        
    
    for b in list_of_moves:
        if(flag==1):
            inp = alpha_beta_game(d-1,b,alpha,beta,0)
            if(inp.value> alpha):
                alpha = inp.value
                out.boardState = b
            out.stateCount = out.stateCount + inp.stateCount
        else:
            inp = alpha_beta_game(d-1,b,alpha,beta,1)
            if(inp.value< beta):
                beta = inp.value
                out.boardState = b
            out.stateCount = out.stateCount + inp.stateCount
        if(alpha>=beta):
            break
    if (flag==1):
        out.value = alpha
    else:
        out.value = beta
    return out

#output-write to file
def write_board(board):
    #print("Write output file")
    outputfile = open(sys.argv[2],"w")
    
    for ch in board:
        outputfile.write(ch)
    outputfile.close()

#main
inputfile = open(sys.argv[1])
depth = int(sys.argv[3])   
board = read_board(inputfile)
out = alpha_beta_game(depth,board,minimum,maximum,1)

print("next state:",''.join(out.boardState))
print("states evaluated:",out.stateCount)
print("estimate value:",out.value)

write_board(out.boardState)
inputfile.close()