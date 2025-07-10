# Divisible Sum Pairs
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

Example
$$ar=[1,2,3,4,5,6]$$
$$k=5$$

Three pairs meet the criteria: [1,4], [2,3] and [4,6].

# Solutions
To solve this case, we have 2 ways to solve it.
From the case we need to sum ar[i] and ar[j] after that divisible by k, if true so we can count it.

Since we need sum all of possibilities, we can use nested loop or even function to create all combination

Below I show you to get all combination by use nested loop:
```python3
def divisibleSumPairs(n: int, k: int, ar: list):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i]+ar[j])%k == 0):
                count += 1
    return count
```

And this by using function combination:
```python3
def divisibleSumPairsTwo(n: int, k: int, ar: list):
    from itertools import combinations

    comb = combinations(ar,2)
    count = 0
    for i in comb:
        if (sum(i)%k == 0):
            count += 1

    return count
```

From that two code it will go same to get all combination of ar we can use the example from the case and here the all combinations:
- (1, 3)
- (1, 2)
- (1, 6)
- (1, 1)
- (1, 2)
- (3, 2)
- (3, 6)
- (3, 1)
- (3, 2)
- (2, 6)
- (2, 1)
- (2, 2)
- (6, 1)
- (6, 2)
- (1, 2)

