
from copy import deepcopy

#Initialize the board object for output
class createObject(object):
    value = 0
    statesCount = 0
    boardState = list()
   
    def __init__(self,value=0,count=0,boardState=list()):
        self.value = value
        self.stateCount = count
        self.boardState = boardState

# replace all black with white and whites with black to generate a board for the opponent
#that can be solved with the same algorithm
def switchToBlack(boardPosition):
    board=list(range(0,23))
    for position in range(0,len(boardPosition)):
        if(boardPosition[position]=="W"):
            board[position]="B"
        elif(boardPosition[position]=="B"):
            board[position]="W"
        else:
            board[position]="x"
    return board

#create a ,list of all black moves. Note interchange
def opening_moves_black(boardPosition):
    boardPosition = switchToBlack(boardPosition)
    black_moves_list = generate_add(boardPosition)   
    l = list()
    for i in range(0,len(black_moves_list)):
        b = switchToBlack(black_moves_list[i])
        l.insert(i,b)
    return l
                             
        


def generate_opening_moves(boardPosition):
    return generate_add(boardPosition)

#generate all possible moves for empty positions for white.
#check for mill.if mill is formed then a piece needs to be removed.
def generate_add(boardPosition):
    listofpositions = list()
    for i in range(0,len(boardPosition)):
        if(boardPosition[i]=="x"):
            b = deepcopy(boardPosition)
            b[i]="W"
            if close_mill(i,b):
               listofpositions = generate_remove(b,listofpositions)
            else:
                listofpositions.append(b)
    return listofpositions


def close_mill(position,b):
    c = b[position]
    if (c=="x"):
        return False
    else:
        return forms_mill(position,b,c)

#check for mill formation for the white player
def forms_mill(location,b,c):
    
    if(c=="x"):
        return False;
    
    if(location==0):
        if((b[1]==c and b[2]==c) or (b[8]==c and b[20]==c) or (b[3]==c and b[6]==c)):
            return True
        else:
            return False
        
    elif(location==1):
        if((b[0]==c and b[2]==c)):
            return True
        else:
            return False
    elif(location==2):
        if((b[0]==c and b[1]==c) or (b[5]==c and b[7]==c) or (b[13]==c and b[22]==c)):
            return True
        else:
            return False
    elif(location==3):
        if((b[0]==c and b[6]==c) or (b[4]==c and b[5]==c) or (b[9]==c and b[17]==c)):
            return True
        else:
            return False
    elif(location==4):
        if((b[3]==c and b[5]==c)):
            return True
        else:
            return False
    elif(location==5):
        if((b[3]==c and b[4]==c) or (b[2]==c and b[7]==c) or (b[12]==c and b[19]==c)):
            return True
        else:
            return False
    elif(location==6):
        if((b[0]==c and b[3]==c) or (b[10]==c and b[14]==c)):
            return True
        else:
            return False
    elif(location==7):
        if((b[2]==c and b[5]==c) or (b[11]==c and b[16]==c)):
            return True
        else:
            return False
    elif(location==8):
        if((b[0]==c and b[20]==c) or (b[9]==c and b[10]==c)):
            return True
        else:
            return False 
    elif(location==9):
        if((b[8]==c and b[10]==c) or (b[3]==c and b[17]==c)):
            return True
        else:
            return False
    elif(location==10):
        if((b[8]==c and b[9]==c) or (b[6]==c and b[14]==c)):
            return True
        else:
            return False
    elif(location==11):
        if((b[7]==c and b[16]==c) or (b[12]==c and b[13]==c)):
            return True
        else:
            return False
    elif(location==12):
        if((b[5]==c and b[19]==c) or (b[11]==c and b[13]==c)):
            return True
        else:
            return False
    elif(location==13):                      
        if((b[11]==c and b[12]==c) or (b[2]==c and b[22]==c)):
            return True
        else:
            return False
    elif(location==14): 
        if((b[17]==c and b[20]==c) or (b[15]==c and b[16]==c) or (b[6]==c and b[10]==c)):
            return True
        else:
            return False
    elif(location==15):
        if((b[14]==c and b[16]==c) or (b[18]==c and b[21]==c)):
            return True
        else:
            return False
    elif(location==16):
        if((b[14]==c and b[15]==c) or (b[19]==c and b[22]==c) or (b[7]==c and b[11]==c)):
            return True
        else:
            return False
    elif(location==17):
        if((b[3]==c and b[9]==c) or (b[14]==c and b[20]==c) or (b[18]==c and b[19]==c)):
            return True
        else:
            return False
    elif(location==18):
        if((b[17]==c and b[19]==c) or (b[15]==c and b[21]==c)):
            return True
        else:
            return False
    elif(location==19):
        if((b[17]==c and b[18]==c) or (b[16]==c and b[22]==c) or (b[5]==c and b[12]==c) ):
            return True
        else:
            return False
    elif(location==20):
        if((b[0]==c and b[8]==c) or (b[14]==c and b[17]==c)or (b[21]==c and b[22]==c)):
            return True
        else:
            return False
    elif(location==21):
        if((b[20]==c and b[22]==c) or (b[15]==c and b[18]==c)):
            return True
        else:
            return False
    elif(location==22):
        if((b[2]==c and b[13]==c) or (b[16]==c and b[19]==c) or (b[20]==c and b[21]==c) ):
            return True
        else:
            return False
    else:
        return False
   
 
def generate_remove(b,listofpositions):
    for location in range(0,len(b)):
        if(b[location]=="B"):
            if(close_mill(location,b)==False):
                b1 = deepcopy(b)
                b1[location]="x"
                listofpositions.append(b1)
    return listofpositions

def generate_moves_midgameEndgame(boardPosition):
    cntw = 0
    l = list()
    for position in range(0,len(boardPosition)):
        if(boardPosition[position]=="W"):
            cntw+=1
    if(cntw==3):
        l = generate_hopping_sequence(boardPosition)
    else:
        l = generate_move(boardPosition)
    return l


def generate_moves_midgameEndgame_black(boardPosition):
    
    temp = switchToBlack(boardPosition)
    listofpositions = generate_moves_midgameEndgame(temp)
    l = list()
    for i in range(0,len(listofpositions)):
        b = listofpositions[i]
        l.insert(i,switchToBlack(b))
    return l

# find all places where a white piece can be moved to . Basically generate all moves 
#for midgame endgame
def generate_hopping_sequence(boardPosition):
    listofPositions = list()
    
    for position1 in range(0,len(boardPosition)):
        if(boardPosition[aposition]=="W"):
            for position2 in range(0,len(boardPosition)):
                if(boardPosition[position2]=="x"):
                    b = deepcopy(boardPosition)
                    b[position1]="x"
                    b[position2]="W"
                    if(close_mill(bposition,b)):
                        listofPositions = generate_remove(b,listofPositions)
                    else:
                        listofPositions.append(b)
    return listofPositions

#calculate neighbour positions
def neighbors(position):
    n = list()
    if(position==0):
        n = [1,3,8]
        return n
    elif(position==1):
        n = [0,2,4]
        return n
    elif(position==2):
        n = [1,5,13]
        return n
    elif(position==3):
        n = [0,4,6,9]
        return n
    elif(position==4):
        n = [1,3,5]
        return n
    elif(position==5):
        n = [2,4,7,12]
        return n
    elif(position==6):
        n = [3,7,10]
        return n
    elif(position==7):
        n = [5,6,11]
        return n
    elif(position==8):
        n = [0,9,20]
        return n
    elif(position==9):
        n = [3,8,10,17]
        return n
    elif(position==10):
        n = [6,9,14]
        return n
    elif(position==11):
        n = [7,12,16]
        return n
    elif(position==12):
        n = [5,11,13,19]
        return n
    elif(position==13):
        n = [2,12,22]
        return n
    elif(position==14):
        n = [10,15,17]
        return n
    elif(position==15):
        n = [14,16,18]
        return n
    elif(position==16):
        n = [11,15,19]
        return n
    elif(position==17):
        n = [9,14,18,20]
        return n
    elif(position==18):
        n = [15,17,19,21]
        return n
    elif(position==19):
        n = [12,16,18,22]
        return n
    elif(position==20):
        n = [8,17,21]
        return n
    elif(position==21):
        n = [18,20,22]
        return n
    elif(position==22):
        n = [13,19,21]
        return n
    else:
        return n
    
def generate_move(boardPosition):
    listofPositions = list()
    
    for position in range(0,len(boardPosition)):
        if(boardPosition[position]=="W"):
            n = neighbors(position)
            for j in n:
                if(boardPosition[j]=="x"):
                    b = deepcopy(boardPosition)
                    b[position] = "x"
                    b[j] = "W"
                    if(close_mill(j,b)):
                        listofPositions = generate_remove(b,listofPositions)
                    else:
                        listofPositions.append(b)
    return listofPositions