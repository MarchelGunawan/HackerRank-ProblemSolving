def birthday(s, d, m):
    startPointer = 0
    endPointer = m-1
    res = 0
    while endPointer <= len(s)-1:
        if sum(s[startPointer:endPointer+1]) == d:
            res += 1
        startPointer += 1
        endPointer += 1
    return res

print(birthday([1,2,1,3,2],3,2)) # Result must be 2
print(birthday([1,1,1,1,1,1],3,2)) # result must be 0
