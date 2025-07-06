# This question is to sum the diagonal from 2 dimentional array
# arr = [][]
# after sum the each diagonal we sum substract the result (the result should positive integer)
# Remember it always 3x3
def first_way(arr):
    # to get max len of arr
    n = len(arr)
    result = 0
    for i in range(n):
        tmp = arr[i][i] - arr[i][-i-1]
        result += tmp
    return abs(result)

arr = [[1,2,3],[4,5,6],[9,8,9]]
print(first_way(arr))
