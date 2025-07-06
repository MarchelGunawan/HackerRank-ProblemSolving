# Mini-Max Sum 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
$$
arr = [1,3,5,7,9]
$$

The minimum sum is 
$
1+3+5+7 = 16
$
and the maximum sum is 
$
3+5+7+9 = 24
$. The function prints
```
16 24
```

# Solution
This solution by using pointer to get all number with size array - 1.
Since size of array is = n, so many number must be taken is n-1.

From the code below we need to define maxOutput and minOutput to negative infinite and positive infinite.

The pointer will point to first index of array, so when do itteration we will skip the number.

With that pointer we can get all possibilities number with out using library.
```python
def minimaxsum(arr):
    """
        first we need to create the variable to store value infinite and 
        minus infinite so later we can use function max and min for change the value 
    """
    maxOutput = float('-inf')
    minOutput = float('inf')
    pointer = 0
    while pointer < len(arr):
        # We need to set variable result so later we can compare the result of calculation
        result = 0
        for i in range(len(arr)):
            # This if statement for avoid sum all array so we can take value len(arr) - 1
            if(i != pointer):
                result += arr[i]
        """
            After done sum, it will compare the result sum with the variable maxOutput and minOutput
            so later we can get the maximum sum and minumum sum each itteration
        """
        maxOutput = max(result, maxOutput)
        minOutput = min(result, minOutput)
        # Don't forget to increment the pointer so it not in forever loop
        pointer += 1
    print(minOutput, maxOutput)

```
