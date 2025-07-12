def pageCount(n, p):
    bookPage = []
    if n % 2 == 0:
        for i in range(n+2):
            bookPage.append(i)
    else:
        for i in range(n+1):
            bookPage.append(i)
    i = 0
    count = 0
    while True:
        if p in bookPage[i:i+2]:
            return count
        elif p in bookPage[len(bookPage)-2-i:len(bookPage)-i]:
            return count
        i += 2
        count += 1

def pageCountTwo(n, p):
    if n % 2 == 0:
        n = n//2
    else:
        n = (n-1)//2

    if p % 2 == 0:
        p = p//2
    else:
        p = (p-1)//2
    return min(abs(0-p),abs(n-p))

n = 6
p = 2
print(pageCount(n,p))
print(pageCountTwo(n,p))
