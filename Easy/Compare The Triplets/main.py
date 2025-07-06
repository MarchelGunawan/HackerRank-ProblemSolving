# This question just want you to compare each value of first array(Alice) with second array(Bob)

def first_way(arr1, arr2):
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

def second_way(arr1, arr2):
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

arr1 = [1,2,3]
arr2 = [3,2,1]
print(first_way(arr1, arr2)) # resulting [1,1]
print(second_way(arr1, arr2)) # resulting [1,1]
