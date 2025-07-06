# Compare the Triplets
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to calculate their comparison points by comparing each category:
<ul>
<li>If a[i] > b[i], then Alice is awarded 1 point.
<li>If a[i] < b[i], then Bob is awarded 1 point.
<li></b>If a[i] = b[i], then neither person receives a point.
Example
</ul>

a = [1, 2, 3]
b = [3, 2, 1]

For elements *0*, Bob is awarded a point because a[0] < b[0].
For the equal elements a[1] and b[1], no points are earned.
Finally, for elements 2, a[2] > b[2] so Alice receives a point.
The return array is [1, 1] with Alice's score first and Bob's second.

# Solutions
The difference about the first way and the second way is just how to manage the result, either you define array first or define array later in the end.
## First solution
The first solution you define the array in the end when you want to return the value into the array.

If you see it clearly there is build in function from python called zip() you can see the example of using zip in this <a href="https://www.w3schools.com/python/ref_func_zip.asp">link</a>
```python
# define start point of alice and bob
alice = 0
bob = 0
# a is for alice and b is for bob
for a, b in zip(arr1, arr2):
    if a < b:
        bob += 1
    elif b < a:
        alice += 1
return [alice, bob]

```
And if you still don't understand how that works you can click this <a href="https://staying.fun/en/features/algorithm-visualize?code=e0d659f4db78b18e9cdc39cf17a36d31a70c96161d3a94416fa3b3dbb67b469f">link</a> to see how the code works.

## Second solution
The second solution you define the array first, and later you access the array and change the value of array if the condition is fulfill.

```python
# make variable of result, result is array
# result [0] for alice
# result [1] for bob
result = [0,0]
for a, b in zip(arr1, arr2):
    if a < b:
        result[1] += 1
    elif b < a:
        result[0] += 1
return result
```
