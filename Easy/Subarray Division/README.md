# Subarray Division
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

Example

$$s=[2,2,1,3,2]$$

$$d=4$$

$$m=2$$

Lily wants to find segments summing to Ron's birth day, d=4  with a length equalling his birth month, m=2 . In this case, there are two segments meeting her criteria:[2,2] and [1,3].

# Solution
This case want us to help share the chocolate with several condition where:
- each bar of chocolate have own value 
- when they want to share the chocolate the length of chocolate must be same as m (birth month)
- after getting how much the length of chocolate bar must be share, they need sum value of length chocolate bar and must be same with d (Ron's birth day)

After we understand with the condition we can continue to solve this.

To solve this you can divide the array by value of m so it can be like this.

$$s=[2,2,1,3,2]$$

- The first chank [2,2]
- The second chank [2,1]
- The third chank [1,3]
- The forth chank [3,2]

But if you divide like that and store to array it will took much of memory, so we can use method called [Sliding Window Algorithm](https://medium.com/@rishu__2701/mastering-sliding-window-techniques-48f819194fd7)

To use that we need to use slicing method from python.

So first we need to define startPointer and endPointer, we need that for slicing the array so later we can use sliding window algorithm.

As you can see we initial startPointer as 0 and endPointer as m-1, maybe some of you wondering why endPointer must be m-1 not just m.

Since array is start from 0 so we need to substract the m with 1 so we can get the length we want.

```python
startPointer = 0
endPointer = m-1
```

After we initial the startPointer and endPointer we can continue to looping, because we need to read all value from the array.

**Rembeber startPointer and endPointer must increment each loop**

```python
while endPointer <= len(s)-1:
  if sum(s[startPointer:endPointer+1]) == d:
    res += 1
  startPointer += 1
  endPointer += 1
```

And this is the full result:

```python
def birthday(s, d, m):
    startPointer = 0
    endPointer = m-1
    res = 0
    while endPointer <= len(s)-1:
        if sum(s[startPointer:endPointer+1]) == d:
            res += 1
        startPointer += 1
        endPointer += 1
    return res
```


