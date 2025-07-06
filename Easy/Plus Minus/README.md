# Plus Minus
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example
$$arr = [1,1,0,-1,-1]$$

There are 5 elements: two positive, two negative and one zero. Their ratios are
$\frac{2}{5} = 0.40000$
,
$\frac{2}{5} = 0.40000$
,
$\frac{1}{5} = 0.20000$

```
0.400000
0.400000
0.200000
```
# Solution
```python
def plusminus(arr):
    pos = len([i for i in arr if i > 0])/len(arr)
    neg = len([i for i in arr if i < 0])/len(arr)
    net = len([i for i in arr if i == 0])/len(arr)
    print(pos)
    print(neg)
    print(net)
```
