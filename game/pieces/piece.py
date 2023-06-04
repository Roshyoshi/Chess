WHITE = 1
BLACK = 2

class Piece:
    def  __init__(self,  color, type):
        self.moves = 0
        self.color = color
        self.t = t

    def move(self,start, end, board):
        if not self.valid(start, end):
            print("Invalid move.")
            return board
        init_board = board
        board[start[0]][start[1]] = 0
        board[[end[0]]][end[1]] = self
        if self.color == WHITE:
            if board.w_king.check:
                print("Invalid move")
                return init_board
        elif self.color == BLACK:
            if board.b_king.check:
                print("Invalid move")
                return init_board
        return board


