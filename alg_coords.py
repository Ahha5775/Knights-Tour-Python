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
