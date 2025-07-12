# Drawing Book
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side:

<img src="https://s3.amazonaws.com/hr-challenge-images/0/1481920803-d2b54f38f0-book.png"></img>

When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a student wants to turn to page , what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.

# Solution
This case want us to count the minimum movement flip page from front of book or end of book.

For resolve this case we have 2 ways to do it:

- Using sliding window algorithm.
- Using math.

## Sliding window algorithm
To using the sliding window algorithm, first we need to image the book by this example

$n=6$ and $p=2$ (n is how many page and p is page we want to find)

From the explanation the page 1 always on the right side so it's mean the left side is none, so we can imagine before the first page is 0.
Even page 0 is not exist.

so later become like this:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| - | - | - | - | - | - | - |

But maybe some of you wondering if we use the sliding window algorithm it should divide evenly right?

Because the book just have left side and right side so it means the long the sliding window is 2.

But if we take look of that there is no pair of 6 

| $\textcolor{red}{0}$ | $\textcolor{red}{1}$ | $\textcolor{green}{2}$ | $\textcolor{green}{3}$ | $\textcolor{blue}{4}$ | $\textcolor{blue}{5}$ | $\textcolor{yellow}{6}$ |
| - | - | - | - | - | - | - |

So to solve that we just need to add 1 number for 6 is 7

| $\textcolor{red}{0}$ | $\textcolor{red}{1}$ | $\textcolor{green}{2}$ | $\textcolor{green}{3}$ | $\textcolor{blue}{4}$ | $\textcolor{blue}{5}$ | $\textcolor{yellow}{6}$ | $\textcolor{yellow}{7}$
| - | - | - | - | - | - | - | - |

Remember this just help you to use the sliding window, the actual page still from 1 until 6.

From that we can conclude if the n is even number so we need plus 1 and if n is odd number we don't need to add the number.

In the code it will become like this:
```python
bookPage = []
if n % 2 == 0:
  for i in range(n+2):
    bookPage.append(i)
else:
  for i in range(n+1): # need to remember loop start from 0 so we still need to + 1 to get the latest page.
    bookPage.append(i)
```

From that code the pages that we imagine before is created successfully.

Now we need to count flip page from the front page and end of page.

To do that we can do it one by one, let say you want count from the from page first, after you get the number you need to count from the end of page and compare which more less flip.

But since there is no rule how to do it you can count it from the first page and end of page in same time. 

And if the number of page we want found first just need return the flip number.

Here the code:

```python
i = 0 
count = 0 
while True:
  if p in bookPage[i:i+2]: # <- this first if is checking from the first page.
    return count
  elif p in bookPage[len(bookPage)-2-i:len(bookPage)-i]: # <- and this else if statement is checking from the end of page.
    return count
  i += 2 # <- remember the book have 2 page: left side and right side so we need increment it by 2.
  count += 1 # <- this will count each flip page if still not found.
```

and this is the full code:

```python
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

```
## Using math method
For this solution we will use the math approach.

So first I will show you how to imagine the pages
<table>
<tbody>
<tr>
<td>Index</td>
<td colspan=2> *0* </td>
<td colspan=2> *1* </td>
<td colspan=2> *2* </td>
<td colspan=2> *3* </td>
</tr>
<tr>
<td>Page</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
</tr>
</tbody>
</table>

There are index and page as you can see the index mean 1 index having 2 pages.

From that we know if we want to reach page 2 we just need to substract $index[1]-index[0]$ by that we know the flip page is 1 and if from the end of page $index[3]-index[1]$ the flip page is 2 so by comparing that the minimum flip page is 1.

But do we need define the index for each 2 pages? The answer is no, you can use math for this. 

You just need to see the even number from each page and divide it by 2 so it will be the index.

But what if $n=7$ and $p=3$ that 2 number is odd number. You just need substract the number with 1 and it will become the even number and it still in same index.

here the code:
```python
if n % 2 == 0:
  n = n//2 
else:
  n = (n-1)//2 

if p % 2 == 0:
  p = p//2 
else:
  p = (p-1)//2 
```

and lastly don't forget to substract the result of p to first of page and n.

So this is the full code:
```python
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

```
