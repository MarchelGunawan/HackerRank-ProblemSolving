# Number Line Jumps
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

<ul>
<li>The first kangaroo starts at location  and moves at a rate of  meters per jump.
<li>The second kangaroo starts at location  and moves at a rate of  meters per jump.
</ul>

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

# Solution
Since in this case have 2 kangaroos with different start point and move rate per jump.

The position of first kangaroo is:
$$x_1+n_{th}.v_1$$

The position of second kangaroo is:
$$x_2+n_{th}.v_2$$

So to make them meet each other we can use this equation:
$$x_1+n_{th}.v_1 = x_2+n_{th}.v_2$$
$$OR$$
$$n_{th} = \frac{x_2-x_1}{v_1-v_2}$$


```python
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return 'YES'
    return 'NO'
```

### Code Explanation
For the first if statement is used for if the movement rate per jump first kangaroo and second kangaroo is same and the starting point of 2 kangaroo is same.
```python
if v1 == v2:
  return 'YES' if x1 == x2 else 'NO'
```

For the second if statement is used for checking the movement is integer not float especially in $(x_2-x_1)\bmod(v_1-v_2)$ and to know the kangaroos meet each other on which n jump we can use equation $n_{th} = \frac{x_2-x_1}{v_1-v_2}$

which that state on second condition after checking movement is integer.
```python
if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return 'YES'
```
if the condition not meet just return no
```python
return 'NO'
```
