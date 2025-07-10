def migratoryBirds(arr):
    from collections import Counter

    count = Counter(arr)
    typeOfBird = [0,0]
    for key, value in count.items():
        if typeOfBird[1] < value:
            typeOfBird[0] = key
            typeOfBird[1] = value

    return typeOfBird[0]

arr = [1,2,3,4,5,4,3,2,1,3,4]
print(migratoryBirds(arr))
