pos = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
k_cor = []
k_cor.append(input("What is the starting column for your piece? (letters A-H)").upper())
k_cor.append(int(input("What is the starting row for your piece? (letters 1-8)")))      #gets the starting coordinate values of  the knight in [letter,number] notation
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
            while(not [k_cor[0] + moves[move[i]][0], k_cor[1] + moves[move[i]][1]] in board):     #checks if points + move is not in board if so, increases move value by one, checks if no moves
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
