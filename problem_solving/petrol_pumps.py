def optimalPoint(magic, dist):
    left_index = 0
    right_index = 0
    
    sum = 0
    for i in range(len(magic)):
        if right_index == len(magic):
            right_index = 0

        if left_index >= len(magic):
            return -1
            
        sum += magic[right_index] - dist[right_index]
        if sum < 0:
            if left_index > right_index:
                return -1
            left_index = right_index + 1
            right_index = right_index + 1
            sum = 0

    return left_index

magic = [2, 3, 1, 4]
dist = [3, 2, 2, 5]

print(optimalPoint(magic, dist))
