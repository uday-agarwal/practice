# Requirements
1. 8x8 chess board with two sides - white (bottom) and black (top).
2. Each side to have the following pieces: 1 King, 1 Queen, 2 Knights, 2 Bishops, 2 Rooks, 8 Pawns.
   1. Initial positions of each square are defined.
3. Two players in the game - 1 each for White and Black.
4. Each player can move one piece at a time from start to end square.
5. When a player's piece reaches a square with opponent's piece, that piece is removed from the game.
6. Moves:
   1. Regular moves:
       1. King: 
          - 1 square left, right, up, down, diagonal, reverse diagonal
          - King can only move to a Square where it won't get a Check
       2. Queen: Any number of squares left, right, up, down, diagonal, reverse diagonal
       3. Rook: Any number of squares left, right, up, down
       4. Bishop: Any number of squares diagonal, reverse diagonal
       5. Knight: 2 squares in one direction + 1 square in perpendicular direction
       6. Pawn:
          - 1 square up (white), 1 square down (black)
          - Cannot move straight if blocked by opponent piece
          - Can move diagonal 1 square if opponent piece present on target square
   2. Special moves:
       1. Pawn can move 2 squares on its first move.
       2. Castling.
       3. Pawn can reach last square and transform to additional Queen.
7. Update game state after each move:
   1. Calculate if opponent is under Check or Checkmate.
   2. Calculate if game has reached Stalemate.
8. Check state:
   1. If a player has valid next move which can land a piece on the opponent King's square.
   2. How to remove the Check.
   3. Checkmate

# Classes
1. Board

2. Piece (interface)
   - Properties:
        1. Current position
        2. Valid moves
    - Methods: 
        1. Get current position
        2. Move
    - Implementations:
        1. King
        2. Queen
        3. Knight
        4. Rook
        5. Bishop
        6. Pawn
3. Player
    1. White
        1. Available pieces
    2. Black
        1. Available pieces
