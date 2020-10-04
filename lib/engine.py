from enum import Enum
import random

def static_test_game():
    game_row = [0 for i in range(10)]
    game = [game_row for i in range(20)]
    game[0][0:4] = [1,1,3,1]
    return game

class Tetromino(Enum):
    oh = 1
    aye = 2
    tee = 3
    ell = 4
    jay = 5
    ess = 6
    zee = 7

class User_action(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    ROTATE = 4

class Direction(Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    def __init__(self, ro, co):
        self.row_offset = ro
        self.col_offset = co

class Piece:
    offset_lists = {
            Tetromino.oh:[[(0,0),(0,1),(1,0),(1,1)]],
            Tetromino.aye:[[(0,0),(0,-1),(0,1),(0,2)], [(0,0),(-1,0),(1,0),(2,0)]],
            Tetromino.tee:[[(0,0),(0,-1),(0,1),(1,0)],[(0,0),(-1,0),(0,-1),(1,0)],[(0,0),(0,-1),(0,1),(-1,0)], [(0,0),(0,1),(-1,0),(1,0)]],
            Tetromino.ell:[[(0,0),(0,-1),(0,1),(1,-1)],[(0,0),(1,0),(-1,0),(-1,-1)] ,[(0,0),(0,-1),(0,1),(-1,1)] ,[(0,0),(1,0),(-1,0),(1,1)]],
            Tetromino.jay:[[(0,0),(0,-1),(0,1),(1,1)],[(0,0),(1,0),(-1,0),(1,-1)] ,[(0,0),(0,-1),(0,1),(-1,-1)] ,[(0,0),(1,0),(-1,0),(-1,1)]],
            Tetromino.ess:[[(0,0),(1,0),(1,-1),(0,1)], [(0,0),(1,0),(0,-1),(-1,-1)]],
            Tetromino.zee:[[(0,0),(0,-1),(1,0),(1,1)], [(0,0),(0,1),(-1,1),(1,0)]]
    }
    def __init__(self, shape, location, offset_index):
        self.shape = shape
        self.row, self.col = location
        self.offset_index = offset_index

    def absolute_coordinates(self):
        coords = []
        for ro, co in Piece.offset_lists[self.shape][self.offset_index]:
            coords.append((self.row + ro, self.col + co))
        return coords

    @staticmethod
    def random_piece(row, col):
        shape = Tetromino(random.randint(1,7)) 
        return Piece(shape, (row, col), 0)

    def get_moved_piece(self, direction):
        return Piece(self.shape, (self.row + direction.row_offset, self.col + direction.col_offset), self.offset_index)

    def get_rotated_piece(self):
        new_offsets = (self.offset_index + 1) % len(Piece.offset_lists[self.shape])
        return Piece(self.shape, (self.row, self.col), new_offsets)

class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.start_row = 0
        self.start_col = (self.cols - 1)//2 
        self.piece = Piece.random_piece(self.start_row, self.start_col)

    def is_valid(self, piece):
        piece_location = piece.absolute_coordinates()
        for r, c in piece_location:
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.board[r][c]:
                return False
        return True

    def clear_rows(self):
        r = self.rows-1
        while r >= 0:
            if all(self.board[r]):
                self.board.pop(r)
                self.board.insert(0, [0 for i in range(self.cols)])
            else:
                r = r-1

    def freeze_current_piece(self):
        absolute_coords = self.piece.absolute_coordinates()
        for r,c in absolute_coords:
            self.board[r][c] = self.piece.shape.value

    def game_state(self):
        game_state = [x[:] for x in self.board]
        for r,c in self.piece.absolute_coordinates():
            game_state[r][c] = self.piece.shape.value
        return game_state

    def on_tick(self):
        #Check if move down is valid
        new_piece = self.piece.get_moved_piece(Direction.DOWN)
        if self.is_valid(new_piece):
            self.piece = new_piece
            return True
        else:
            self.freeze_current_piece()
            self.clear_rows()
            self.piece = Piece.random_piece(self.start_row, self.start_col)
            if not self.is_valid(self.piece):
                return False
            else:
                return True


    def on_input(self, action):
        if action == User_action.LEFT:
            new_piece = self.piece.get_moved_piece(Direction.LEFT)
            if self.is_valid(new_piece):
                self.piece = new_piece
        if action == User_action.RIGHT:
            new_piece = self.piece.get_moved_piece(Direction.RIGHT)
            if self.is_valid(new_piece):
                self.piece = new_piece
        if action == User_action.DOWN:
            new_piece = self.piece.get_moved_piece(Direction.DOWN)
            if self.is_valid(new_piece):
                self.piece = new_piece
        if action == User_action.ROTATE:
            new_piece = self.piece.get_rotated_piece()
            if self.is_valid(new_piece):
                self.piece = new_piece
