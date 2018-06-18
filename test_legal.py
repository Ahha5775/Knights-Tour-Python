#NOTE: assumes board already exists and is only compatible with board as list of coordinates!
def coor_sub(a,b):
    """Subtracts coordinate list b from coordinate list a."""
    return [a[0]-b[0],a[1]-b[1]]

def test_legal(move,k_cor):
    """Checks proposed move to chess coordinates on chessboard for the knight at k_cor.
    returns True if legal and False if illegal or already visited."""
    global board
    poss=[[1,2],[1,-2],[-1,2],[-1,-2],
          [2,1],[2,-1],[-2,1],[-2,-1]]
    if coor_sub(k_cor,move) in poss:
        if move in board:
            return True
    return False

