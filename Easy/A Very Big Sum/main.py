# This question is same with simple array sum 
# You can just sum() function or itterate one by one

def first_way(arr):
    return sum(arr)

def second_way(arr):
    result = 0
    for i in arr:
        result += i 
    return result

arr = [1000000001,1000000002,1000000003,1000000004,1000000005]
print(first_way(arr)) # result 5000000015
print(second_way(arr)) # result 5000000015
