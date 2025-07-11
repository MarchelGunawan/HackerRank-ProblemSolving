# Sales by Match
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example

$$n = 7$$ and $$ar = [1,2,1,2,1,3,2]$$

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

# Solution
This case want us to count of pair socks in ar. Since socks must pair so it's mean the number of sock must 2.

If the number of pair socks is 3 so the result must 1 and pair socks is 4 so the result 2 because human just use 2 socks on their feet.

So first we need to know each type of pair in the ar.

```python
# ar = [1,2,1,2,1,3,2]
pair = list(set(ar)) # <- this will result pair = [1,2,3]
```

After that we need to store each pair that wo have more than 1 sock

```python
count = [ar.count(i) for i in pair if ar.count(i) > 1] # <- this will store the number pair of sock more than 1.
```

Lastly we need to count pair of sock by divide by 2 

```python
res = 0 # <- to store pair of sock
for i in count:
  res += i//2  
```

Here the full code of this case:

```python
def sockMerchant(n, ar: list):
    pair = list(set(ar))
    count = [ar.count(i) for i in pair if ar.count(i) > 1]
    res = 0
    for i in count:
        res += i//2
    return res

```
