# Breaking the Records

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Example

$scores=[12,24,10,24]$

Scores are in the same order as the games played. She tabulates her results as follows:
```
                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

```
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# Solution
The case just want us to counting the maximum score and Minimum score from each game by taking the biggest and lowest score from last round of game.

And they also want us to return it into an array where array[0] is count of breaks scores and array[1] is count of least scores.

Since the first round is the starting point for break score or least score so we can define it first before we do looping.

```python
arr = [0,0] # <-- initial count for break and least
maxScore = scores[0] # <-- initial for maximum score
minScore = scores[0] # <-- initial for minimum score
```

After we initial the array and the first score, we can do the loop for read score each round.

And here the full code of breaking records:

```python
def breakingRecords(scores):
    arr = [0,0]
    maxScore = scores[0]
    minScore = scores[0]
    for i in range(len(scores)):
        if i == 0:
            continue
        if scores[i] > maxScore:
            arr[0] += 1
            maxScore = scores[i]
        elif scores[i] < minScore:
            arr[1] += 1
            minScore = scores[i]
    return arr
```
