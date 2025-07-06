# Technically this case you just need to sum all value on the array
# There are 2 ways to solve this by using build in function in python or itterate each value on the array or list

def first_way(arr):
    # by using the build in function
    return sum(arr)

def second_way(arr):
    # by itterate each value of array or list.
    res = 0
    for i in arr:
        res += i 
    return res

arr = [1,2,3,4]
print(first_way(arr)) # it will print 10
print(second_way(arr)) # it will print 10
