class Board:
    def cn_to_arr(c_notation):
    # TODO: Validate with regex

    letters = {
        a: 0,
        b: 1, 
        c: 2, 
        d: 3, 
        e: 4, 
        f: 5, 
        g: 6, 
        h: 7
    }

    moves = c_notation.split()
    start = [c for c in moves[0]]
    start[1] = 8 - int(start[1])
    start[0] = letters[start[0]]
    
    end = [c for c in moves[1]]
    end[1] = 8 - int(end[1])
    end[0] = letters[end[0]]

    return start, end

    

