def getTotal(a, b):
    import math 
    lcma = math.lcm(*a)
    gcdb = math.gcd(*b)
    count = 0
    increment = 1
    while True:
        divider = lcma*increment
        if gcdb % divider == 0:
            count += 1
        if gcdb < divider:
            break
        increment += 1
    return count

print(getTotal([2,6],[24,36])) # result should be 2
print(getTotal([2,4],[16,32,96])) # result should be 3

