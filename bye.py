def alg2coords(text):
    """Converts algebraic notation to list [x,y]."""
    x=text[0].lower()
    y=text[1]
    let2coords={"a":0,
                "b":1,
                "c":2,
                "d":3,
                "e":4,
                "f":5,
                "g":6,
                "h":7}
    y=int(y)-1 #a1 maps to [0,0] not [0,1]
    return [let2coords[x],y]

def coords2alg(coords):
    """Converts coordinates s a list [x,y] to algebraic notation."""
    x=coords[0]
    y=coords[1]
    x=chr(x+65).lower()
    y=str(y+1)
    return x+y

pos = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
place=input("What coordinates do you want? ")
k_cor=alg2coords(place)
move = []
board = []
for i in range(64):
    move.append(0)
for i in range(8):
    for x in range(8):
        board.append([i,x])
for i in range(len(board)):
    if(board[i] == [k_cor[0],k_cor[1]]):
        del(board[i])
        break              #makes board, deletes starting value
last_c = []
running = True
while(running == True):      #creates loop that runs program (necessary because have to define varaibles beforehand and run multiple times)
    prev = []
    re= 1
    n_move = 0
    while(re == 1):
        re = 0
        for i in range(len(move)):
            while(not [k_cor[0] + pos[move[i]][0], k_cor[1] + pos[move[i]][1]] in board):     #checks if points + move is not in board if so, increases move value by one, checks if no moves
                move[i] += 1
                re = 1
                if(move[i] > 7):
                    prev = move
                    prev[i-1]+=1
                    for x in range(len(move)-i):            #also checks if completed and prints results *kinda*
                        if(board == []):
                            print(last_c)
                        prev[i+x] = 0
                        n_move = 1          
                        break
            if(n_move == 0):
                k_cor[0],k_cor[1] = k_cor[0] + moves[move[i]][0], k_cor[1] + moves[move[i]][1]
                last_c.append([k_cor[0],k_cor[1]])
                for i in range(len(board)):
                    if(board[i] == [k_cor[0],k_cor[1]]):
                        del(board[i])
                        break
            if(n_move == 1):
                break
    it = len(prev)
    prev[it-1] += 1
    x=1
    while(move[it-x] > 7):    #puts next series into list
        prev[it-x] = 0
        x += 1
        prev[it-x] += 1
        if(x == it):
            print("No solution")
            break
    move = prev
    board = []
    for i in range(8):
        for x in range(8):
            board.append([i,x])
