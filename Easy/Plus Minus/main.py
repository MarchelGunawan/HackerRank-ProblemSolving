# This question want to count the positive number, negative number and neutral number then devide it by
# len of array

def plusminus(arr):
    pos = len([i for i in arr if i > 0])/len(arr)
    neg = len([i for i in arr if i < 0])/len(arr)
    net = len([i for i in arr if i == 0])/len(arr)
    print(pos)
    print(neg)
    print(net)

arr = [-4,3,-9,0,4,1]
plusminus(arr)
