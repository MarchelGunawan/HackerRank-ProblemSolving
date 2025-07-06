"""
    The question want us to figure out a way 
    to get both kangaroos at the same location
    at the same time.

    x1 = start position of kangaroo1
    v1 = how long kangaroo1 can jump
    x2 = start positino of kangaroo2
    v2 = how long kangaroo2 can jump
"""
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return 'YES'
    return 'NO'
print(kangaroo(0,3,4,2))
print(kangaroo(0,2,5,3))

