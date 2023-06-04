import piece

ROW = 1
COLUMN = 0

class Pawn:
    def __init__(self, color):
        super().__init__(color, Pawn)

    def valid(self, start, end, board):
        if self.t == 2:
            if (self.moves == 0 and end[COLUMN] - start[COLUMN] > 2) or (end[COLUMN] - start[COLUMN]  > 1 and self.moves > 0):
                return False
            if start[1] == end[1]:
                for i in range(start[1], end[1]):
                    if board[start[0]][i] != 0:
                        return False
                if board[end[0]][end[1]] != 0:
                    return False
                if start[1] 
            elif abs(start[0] - end[0]

