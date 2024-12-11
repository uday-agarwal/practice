'''
# q2

## question

Give a picture with M x N pixels.

Pixel is represented in 0 or 1. 1 means "shadow". 0 means "empty (nothing)"".

If one shadow block is connected with other shadow block in any one of (up, down, left, right) direction, we count them as one.

Detect how many shadows in the picture.

Examples:

'''

from collections import deque

def countShadows(picture):
    count = 0
    
    rows = len(picture)
    columns = len(picture[0])
    
    visitedShadowPixels = [[0] * columns] * rows
    
    for i in range(rows):
        for j in range(columns):
            if picture[i][j] == 1 and visitedShadowPixels[i][j] == 0:
                count += 1
                visitedShadowPixels[i][j] = 1

                # Queue that contains all the indexes whose neighbors 
                # are to be checked for shadow extension
                shadow = deque()
                shadow.append((i, j))
                
                while len(shadow):
                    pixel = shadow.popleft()
                    x = pixel[0]
                    y = pixel[1]
                    
                    for p,q in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if p >= 0 and p < rows and q >= 0 and q < columns and picture[p][q] == 1 and visitedShadowPixels[p][q] == 0:
                            visitedShadowPixels[p][q] = 1
                            shadow.append((p, q))

    return count

case1 = [
[1, 1, 0],
[0, 1, 0],
[0, 0, 0],
]

case2 = [
[1, 0, 1],
[0, 1, 1],
[0, 0, 0],
]

case3 = [
[0, 0, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 1, 1],
]

cases = (case1, case2, case3)
results = (1, 2, 4)

for i, case in enumerate(cases):
    print(countShadows(case))
