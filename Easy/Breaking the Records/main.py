def breakingRecords(scores):
    arr = [0,0]
    maxScore = scores[0]
    minScore = scores[0]
    for i in range(len(scores)):
        if i == 0:
            continue
        if scores[i] > maxScore:
            arr[0] += 1
            maxScore = scores[i]
        elif scores[i] < minScore:
            arr[1] += 1
            minScore = scores[i]
    return arr

print(breakingRecords([10,5,20,20,4,5,2,25,1])) # result must be [2,4]
print(breakingRecords([3,4,21,36,10,28,35,5,24,42])) # result must be [4,0]
