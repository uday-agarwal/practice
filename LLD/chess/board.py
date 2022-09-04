from enum import Enum
from piece import Piece, Rook, Knight, Bishop, King, Queen, Pawn
from square import Square

BOARD_DIMENSION = 8

class Player(Enum):
    BLACK = 0
    WHITE = 1

class Position:
    def __init__(self, piece : Piece = None, player: Player = None):
        self.piece = piece
        self.player = player

    def __str__(self):
        return str(self.player.name) + " " + str(self.piece)

class Board:
    """Chess board definition
    
    8 x 8 matrix of squares. Each square can contain a black or white piece.
    The matrix looks like initially:
       0     1      2      3     4     5      6      7
    0  Rook  Knight Bishop Queen King  Bishop Knight Rook <- Player: Black
    1  Pawn  Pawn   Pawn   Pawn  Pawn  Pawn   Pawn   Pawn <- Player: Black
    2  Empty Empty  Empty  Empty Empty Empty  Empty  Empty
    3  Empty Empty  Empty  Empty Empty Empty  Empty  Empty
    4  Empty Empty  Empty  Empty Empty Empty  Empty  Empty
    5  Empty Empty  Empty  Empty Empty Empty  Empty  Empty
    6  Pawn  Pawn   Pawn   Pawn  Pawn  Pawn   Pawn   Pawn <- Player: White
    7  Rook  Knight Bishop Queen King  Bishop Knight Rook <- Player: White
    """
    def __init__(self):
        self.positions = [[None for i in range(BOARD_DIMENSION)] for i in range(BOARD_DIMENSION)]

        # Initialize positions
        for row, player in {0: Player.BLACK, 7: Player.WHITE}.items():
            self.positions[row][0] = Position(Rook(), player)
            self.positions[row][1] = Position(Knight(), player)
            self.positions[row][2] = Position(Bishop(), player)
            self.positions[row][3] = Position(Queen(), player)
            self.positions[row][4] = Position(King(), player)
            self.positions[row][5] = Position(Bishop(), player)
            self.positions[row][6] = Position(Knight(), player)
            self.positions[row][7] = Position(Rook(), player)

        for j in range(BOARD_DIMENSION):
            self.positions[1][j] = Position(Pawn(), Player.BLACK)
            self.positions[6][j] = Position(Pawn(), Player.WHITE)

    def filter_positions(self, candidate_squares: set(), piece: Piece, player: Player):
        filtered_positions = set()
        for square in candidate_squares:
            # The square should be on the board
            if square.row_id < 0 or square.row_id >= BOARD_DIMENSION or \
                square.column_id < 0 or square.column_id >= BOARD_DIMENSION:
                continue

            # If the square is empty, you can go ahead
            if self.positions[square.row_id][square.column_id] == None:
                filtered_positions.add(square)
                continue

            # Cannot move to any square that has another piece of the same player
            if self.positions[square.row_id][square.column_id].player == player:
                continue

            # Pawn rules - can only move forward
            pass

            # Cannot move in a row, column, or diagonal beyond a blockage
            pass

            filtered_positions.add(square)

        return filtered_positions

    def move_piece(self, current_square: Square, target_square: Square):
        self.positions[target_square.row_id][target_square.column_id] = \
            self.positions[current_square.row_id][current_square.column_id]
        self.positions[current_square.row_id][current_square.column_id] = None

    def __str__(self):
        output = "   "
        for i in range(8):
            output += str(i) + "\t\t"
        output += "\n"
        for id, position_row in enumerate(self.positions):
            output += str(id) + ": "
            for position in position_row:
                output += str(position) + '\t'
            output += '\n'
        return output
    
    def get_positions(self):
        return self.positions
