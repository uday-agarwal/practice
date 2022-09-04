"""Given an image of MxN pixels, clicking one pixel should flood fill
all other adjacent pixels of the same color.
"""

test_data = [[1, 2, 2, 2, 1, 0, 2],
             [1, 1, 2, 2, 1, 1, 0],
             [1, 2, 2, 1, 1, 0, 0],
             [1, 2, 0, 2, 1, 1, 1],
             [1, 0, 2, 0, 0, 1, 0]]

def flood_fill(matrix: list(list()), pixel: tuple(int, int), new_color: int):
    m = len(matrix)
    n = len(matrix[0])


def print_test_data():
    for row in test_data:
        for column in row:
            print(column, end = ' ')
        print('')

if __name__ == '__main__':
    print_test_data()
    flood_fill(test_data, 3)
    print_test_data()
