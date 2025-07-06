# The question want to calculate how many apples and oranges will fall on Sam's house.
"""
    s and t is distance of Sam's house where s is start point and t is end point of Sam's house.
    a and b is where the apple tree and orange tree located, a is apple tree located and b is orange tree located.
    apples and oranges is array that distance of apples from apple tree and oranges from orange tree.
"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
        To search the coordinate of each apple and orange.
        we just need to adding each apple and orange distance to their tree position,
    """
    apples = [a + i for i in apples]
    oranges = [b + i for i in oranges]
    resAp = 0
    for i in apples:
        if(i >= s and i <= t):
            resAp += 1
    print(resAp)
    resOr = 0
    for i in oranges:
        if(i >= s and i <= t):
            resOr += 1
    print(resOr)

countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])
