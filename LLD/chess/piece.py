from abc import ABC, abstractmethod
from square import Square

class Piece(ABC):
    @abstractmethod
    def get_valid_moves(current_square: Square):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Rook(Piece):
    def get_valid_moves(current_square: Square):
        pass

    def __str__(self):
        return "Rook"

class King(Piece):
    def get_valid_moves(current_square: Square):
        pass

    def __str__(self):
        return "King"

class Knight(Piece):
    def get_valid_moves(current_square: Square):
        pass

    def __str__(self):
        return "Knight"

class Bishop(Piece):
    def get_valid_moves(current_square: Square):
        pass

    def __str__(self):
        return "Bishop"

class Queen(Piece):
    def get_valid_moves(current_square: Square):
        pass

    def __str__(self):
        return "Queen"

class Pawn(Piece):
    def get_valid_moves(current_square: Square):
        moves = set()
        moves.add(Square(current_square.row_id + 1, current_square.column_id))
        moves.add(Square(current_square.row_id + 1, current_square.column_id + 1))
        moves.add(Square(current_square.row_id + 1, current_square.column_id - 1))
        moves.add(Square(current_square.row_id - 1, current_square.column_id))
        moves.add(Square(current_square.row_id - 1, current_square.column_id + 1))
        moves.add(Square(current_square.row_id - 1, current_square.column_id - 1))

        return moves

    def __str__(self):
        return "Pawn"
