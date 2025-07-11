def bonAppetit(bill: list, k: int, b: int):
    annaBill = (sum(bill)-bill.pop(k))//2
    if(annaBill == b):
        print("Bon Appetit")
    else:
        print(b-annaBill)

bill = [3,10,2,9]
k = 1
b = 12
bonAppetit(bill, k, b)
