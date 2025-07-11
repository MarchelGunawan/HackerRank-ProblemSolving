def sockMerchant(n, ar: list):
    pair = list(set(ar))
    count = [ar.count(i) for i in pair if ar.count(i) > 1]
    res = 0
    for i in count:
        res += i//2
    return res

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n,ar))
