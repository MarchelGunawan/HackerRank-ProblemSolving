def divisibleSumPairs(n: int, k: int, ar: list):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i]+ar[j])%k == 0):
                count += 1
    return count

def divisibleSumPairsTwo(n: int, k: int, ar: list):
    from itertools import combinations
    
    comb = combinations(ar,2)
    count = 0
    for i in comb:
        print(i)
        if (sum(i)%k == 0):
            count += 1

    return count

n = 6
k = 3
ar = [1,3,2,6,1,2]
print(divisibleSumPairs(n, k, ar))
print(divisibleSumPairsTwo(n, k, ar))
