from board import Board, Square, Player
from enum import Enum
from piece import Piece, Rook, Knight, Bishop, King, Queen, Pawn
import sys

class GameState(Enum):
    ONGOING = 0
    DRAW = 1
    WON = 2

class GameController:
    state = GameState.ONGOING

    def __init__(self):
        self.board = Board()
        self.player_turn = Player.WHITE
    
    def move(self, player: Player, piece: Piece, current_square: Square, target_square: Square):
        # it should be the player's chance to move
        if self.player_turn != player:
            raise ValueError("This is not your chance!")

        # current square must be holding the piece in question
        if type(self.board.positions[current_square.row_id][current_square.column_id].piece) != piece:
            raise ValueError("The piece is not on the square mentioned")
        
        # the piece should belong to the player in question
        if self.board.positions[current_square.row_id][current_square.column_id].player != player:
            raise ValueError("This piece does not belong to you!")

        possible_squares = piece.get_valid_moves(current_square)
        for p in possible_squares:
            print(p.row_id, p.column_id, p.color.name)
        filtered_squares = self.board.filter_positions(possible_squares, piece, player)
        for p in filtered_squares:
            print(p.row_id, p.column_id, p.color.name)
        for position in filtered_squares:
            if position.row_id == target_square.row_id and \
                position.column_id == target_square.column_id:
                self.__move(piece, current_square, target_square)

    def __move(self, piece: Piece, current_square: Square, target_square: Square):
        self.board.move_piece(current_square, target_square)

        # After a move is complete, change the player
        if self.player_turn == Player.WHITE:
            self.player_turn = Player.BLACK
        else:
            self.player_turn = Player.WHITE
        print(self.board)

    def play(self):
        print("Start of the game!")
        print("Pieces: P (Pawn), Kt (Knight), R (Rook), B (Bishop), K (King), Q (Queen)")

        piece = {
            'P': Pawn,
            'Kt': Knight,
            'R': Rook,
            'B': Bishop,
            'K': King,
            'Q': Queen,
        }

        while self.state == GameState.ONGOING:
            print(self.board)
            print(self.player_turn.name + "'s chance.")
            user_input = input("Enter your piece, start square (x,y), end square(x,y), separated by comma (eg: P (6,0) (5,0)): ").split()
            starting_square = Square(int(user_input[1][1]), int(user_input[1][3]))
            target_square = Square(int(user_input[2][1]), int(user_input[2][3]))
            try:
                self.move(self.player_turn, piece[user_input[0]], starting_square, target_square)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    game = GameController()
    game.play()

    sys.exit(0)
