# This question want you to sum the array to get the maximum output of sum and
# minumum output of sum
# if the length of array is 5 so you must sum 4 value from array
# where it's mean len(arr) - 1
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


arr = [1,2,3,4,5]
minimaxsum(arr)
