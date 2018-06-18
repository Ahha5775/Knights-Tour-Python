board=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

kn_coor=[0,0]

def add_coor(a,b):
    """Adds coordinate lists a and b."""
    return [a[0]+b[0],a[1]+b[1]]

def sub_coor(a,b):
    """Subtracts coordinate lists a and b."""
    return [a[0]-b[0],a[1]-b[1]]

def exists(coords):
    """Returns True if coords on board."""
    x=coords[0]
    y=coords[1]
    if x in range(8):
        if y in range(8):
            return True
    return False

def test_legal(move):
    """Tests if move in the form of a proposed chess coordinate list for the knight is valid.
    returns True if legal and False if illegal or already visited."""
    global kn_coor #This is where the knight is
    global board
    legal_moves=[[1,2],[1,-2],[-1,2],[-1,-2],
                 [2,1],[2,-1],[-2,1],[-2,-1]]
    if sub_coor(move,kn_coor) not in legal_moves:
        return False
    elif not exists(move):
        return False
    elif board[move[0]][move[1]]=='M': #M means that the space was already visited
        return False
    else:
        return True


