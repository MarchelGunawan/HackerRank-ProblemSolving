# Birthday Cake Candles
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.

Example
$$candles = [4,4,1,3]$$

The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.

# Solution
```python
def birthdayCakeCandles(arr):
    # So we just need to count the max value of array (candles)
    return arr.count(max(arr))
```
