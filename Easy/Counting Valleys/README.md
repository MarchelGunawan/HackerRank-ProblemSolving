# Counting Valleys
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly $steps$ steps, for every step it was noted if it was an uphill, $U$, or a downhill, $D$ step. Hikes always start and end at sea level, and each step up or down represents a $1$ unit change in altitude. We define the following terms:

- A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
- A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Solution
For this case they want us to count how many valley that we through with condition where valley is steps below sea level.uphill

This is the example of the one case:

$steps = 8$ and $path="UDDDUDUU"$

First we need make the path become array by using list() function
```python
arrStep = list(path)
```

After that we need to initial movementStep for calculate each movement UP and DOWN also downValley for count how many valleys that we through.
```python
arrStep = list(path)
movementStep = 0
downValley = 0
```

Next we need loop each path that we made before in variable arrStep. 
Remember the sea level in here we initial as 0, so if movementStep is 0 and movementStep - 1 less than 0 we can say we start through the valley.
```python
arrStep = list(path)
    movementStep = 0
    downValley = 0
    for i in arrStep:
        if i == "D":
            if( movementStep == 0 and movementStep-1 < 0):
                movementStep -= 1
                downValley += 1
            else:
                movementStep -= 1
        else:
            movementStep += 1 
```

Lastly after we did the looping we just need return the value of downValley.
Here the full code of counting valleys:
```python
def countingValleys(steps, path):
    arrStep = list(path)
    movementStep = 0
    downValley = 0
    for i in arrStep:
        if i == "D":
            if( movementStep == 0 and movementStep-1 < 0):
                movementStep -= 1
                downValley += 1
            else:
                movementStep -= 1
        else:
            movementStep += 1 
    return downValley
```

The time complexity is $O(n)$
