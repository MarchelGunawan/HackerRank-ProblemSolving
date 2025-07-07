# Between Two Sets
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

- The elements of the first array are all factors of the integer being considered
- The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
$$a=[2,6]$$
$$b=[24,36]$$

There are two numbers between the arrays: 6 and 12

$6\bmod2=0,6\bmod6=0,24\bmod6=0,36\bmod6=0$ for the first value 

$12\bmod2=0,12\bmod6=0,24\bmod12=0,36\bmod12=0$ for the second value.

so return 2.

# Solution
The solution we need to use LCM (Least Common Multiple) and GCD (Greatest Common Divisor) where we can find it by using math library from python (You can read more about [LCM and GCD Documentation](https://note.nkmk.me/en/python-gcd-lcm/))

if we took example from above where a = [2,6] and b = [24,36]. the LCM of a is {6,12,18,24,30,...} and GCD of b is {1,2,3,4,6,12} from that we know slice of LCM a and GCD b is {6,12} so the result is 2.

```python
def getTotalX(a, b):
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
```

