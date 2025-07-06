# Apple and Orange 
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:

<ul>
<li>The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
<li>Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
<li>When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. 
</ul>

<img src="https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png">

Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

For example, Sam's house is between s = 7 and t = 10. The apple tree is located at a = 4  and the orange at b = 12. Apples are thrown apples = [2,3,-4] units distance from a, and oranges = [3,-2,-4] units distance. Adding each apple distance to the position of the tree, they land at [4+2, 4+3, 4+(-4)] = [6, 7, 0]. Oranges land at [12+3, 12+(-2), 12+(-4)] = [15, 10, 8]. One apple and two oranges land in the inclusive range 7 - 10 so we print

```
1 
2 
```

# Solution
From the case we know that to decide the location of each apples and oranges by using 

$
apples = [a+apples[0], a+apples[1], a+apples[2], a+...apples[n]]
$

$
oranges = [b+oranges[0], b+oranges[1], b+oranges[2], b+...oranges[n]]
$

```python
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [a + i for i in apples]
    oranges = [b + i for i in oranges]
    resAp = 0
    for i in apples:
        if(i >= s and i <= t):
            resAp += 1
    print(resAp)
    resOr = 0
    for i in oranges:
        if(i >= s and i <= t):
            resOr += 1
    print(resOr)
```
