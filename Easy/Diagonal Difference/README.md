# Diagonal Difference
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:
```
1 2 3 
4 5 6 
9 8 9 
```

<ul>
<li>The left-to-right diagonal = 1 + 5 + 9 = 15.
<li>The right-to-left diagonal = 3 + 5 + 9 = 17.
</ul>
Their absolute difference is |15-17| = 2.

# Solution
For this case you can sum the left to right diagonal and sum the right to left diagonal. After that subtract the result of both diagonal into absolute.

But there is another way to calculate that. Since we can see the pattern how takes value of diagonal, we can simplify it by subtract each line of diagonal. 

e.g:

This is the square matrix.
```
1 2 3 
4 5 6 
9 8 9 
```

The first diagonal of left to right is 1 and right to left is 3. 
<table>
  <tr>
    <td>$\textcolor{#ff0000}{1}$</td>
    <td>2</td>
    <td>$\textcolor{#ff0000}{3}$</td>
  </tr>
  <tr>
    <td>4</td>
    <td>5</td>
    <td>6</td>
  </tr>
  <tr>
    <td>9</td>
    <td>8</td>
    <td>9</td>
  </tr>
</table>

Which means we can subtract 1 - 3 = -2
after that it will go to 5 in the middle

<table>
  <tr>
    <td >$\textcolor{#00ff00}{1}$</td>
    <td>2</td>
    <td >$\textcolor{#00ff00}{3}$</td>
  </tr>
  <tr>
    <td>4</td>
    <th >$\textcolor{#ff0000}{5}$</th>
    <td>6</td>
  </tr>
  <tr>
    <td>9</td>
    <td>8</td>
    <td>9</td>
  </tr>
</table>

so 5 - 5 = 0

The last one is 9 and 9.
<table>
  <tr>
    <td >$\textcolor{#00ff00}{1}$</td>
    <td>2</td>
    <td >$\textcolor{#00ff00}{3}$</td>
  </tr>
  <tr>
    <td>4</td>
    <td >$\textcolor{#00ff00}{5}$</td>
    <td>6</td>
  </tr>
  <tr>
    <th>$\textcolor{#ff0000}{9}$</th>
    <td>8</td>
    <th>$\textcolor{#ff0000}{9}$</th>
  </tr>
</table>

so 9 - 9 = 0

Sum all of that and the result must absolute
$|-2 + 0 + 0| = 2$ 

This is the code
```python
def diagonalDifference(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        tmp = arr[i][i] - arr[i][-i-1]
        result += tmp
    return abs(result)
```


