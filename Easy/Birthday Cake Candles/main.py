# This question want to return value of highest array (candles)
def birthdayCakeCandles(arr):
    # So we just need to count the max value of array (candles)
    return arr.count(max(arr))

arr = [3,2,1,3]
print(birthdayCakeCandles(arr))
