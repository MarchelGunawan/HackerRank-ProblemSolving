# Migratory Birds
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example

$$arr=[1,1,2,2,3]$$

There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

# Solution
The solution for this case first we need to count each type of birds. 
To count each type of birds you have two ways using function Counter() or manually count

Manually count:
```python3
arr = [1,1,2,2,3]
typeOfBird = list(set(arr)) # <- to drop duplicate number so it will be [1,2,3]
countEachBird = {i: arr.count(i) for i in typeOfBird} # <- {1: 2, 2: 2, 3: 1}
```

Using Counter():
```python3
from collections import Counter
arr = [1,1,2,2,3]
countEachBird = Counter(arr) <- {1: 2, 2: 2, 3: 1}
```

Here is full code:
```python3
def migratoryBirds(arr):
    from collections import Counter

    count = Counter(arr)
    typeOfBird = [0,0] # <- typeOfBird[0] is for type of bird and typeOfBird[1] is for result count of type birds
    for key, value in count.items():
        if typeOfBird[1] < value:
            typeOfBird[0] = key
            typeOfBird[1] = value

    return typeOfBird[0]
```
