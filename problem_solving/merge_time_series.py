# Merge time series
def mergeTimeSeries(t1, t2):
    p1 = 0
    p2 = 0
    output = []
    t1Spike = 0
    t2Spike = 0

    while p1 < len(t1) and p2 < len(t2):
        if t1[p1][0] == t2[p2][0]:
            t1Spike = t1[p1][1]
            t2Spike = t2[p2][1]
            output.append((t1[p1][0], t1Spike + t2Spike))
            p1 += 1
            p2 += 1
        elif t1[p1][0] < t2[p2][0]:
            t1Spike = t1[p1][1]
            output.append((t1[p1][0], t1Spike + t2Spike))
            p1 += 1
        else:
            t2Spike = t2[p2][1]
            output.append((t2[p2][0], t1Spike + t2Spike))
            p2 += 1

    if p1 < len(t1):
        output.append([(x, y+t2Spike) for (x,y) in t1[p1:]])

    if p2 < len(t2):
        output.append([(x, y+t1Spike) for (x,y) in t2[p2:]])

    return output

# Inputs: Each has (start time, spike value)
# No end time until next start time available
T1 = [ (0,1) , (3,5) , (7,2) ]
T2 = [ (2,2) , (3,3) , (6,1) ]

# Expected Output:
# [ (0,1) , (2,3) , (3,8) , (6,6) , (7,3) ]

result = mergeTimeSeries(T1, T2)
print(result)
