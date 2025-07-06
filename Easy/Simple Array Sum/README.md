# Simple Array Sum 
Given an array of integers, find the sum of its elements.

For example, if the array arr = [1,2,3], 1+2+3 so return 6.

# Solution
## First way
The first solution is using buildin function from python <a href="https://www.w3schools.com/python/ref_func_sum.asp">sum()</a>
```python
# by using the sum() function you just need to put the array/list
# into the buildin function
arr = [1,2,3]
sum(arr) # --> resulting 1+2+3 = 6
```

## Second way 
The second solution is using for loop 
The visualization for this u can click this <a href="https://staying.fun/en/features/algorithm-visualize?code=26a25c0cf2252b706760ec651e110307d9ccfc6173f0e676228f2f14915a81b8">link</a>
```python
arr = [1,2,3]
res = 0
for i in arr:
  res += i # --> so basically this will do 0+1+2+3
```
