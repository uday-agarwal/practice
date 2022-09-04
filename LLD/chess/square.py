from enum import Enum

class SquareColor(Enum):
    WHITE = 0
    BLACK = 1

class Square:
    def __init__(self, row: int, col: int):
        self.row_id = row
        self.column_id = col
    
        # Set color as per row and column
        color_inverted = (row % 2) == 0 # True for 0, 2, 4, 6. False for 1, 3, 5, 7
        if color_inverted:
            if (col % 2) == 0:
                self.color = SquareColor.BLACK
            else:
                self.color = SquareColor.WHITE
        else:
            if (col % 2) != 0:
                self.color = SquareColor.BLACK
            else:
                self.color = SquareColor.WHITE

    def __str__(self):
        return "(" + str(self.row_id) + ", " + str(self.column_id) + ", " + self.color.name + ")"
