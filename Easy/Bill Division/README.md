# Bill Division
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6]. Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3. If he includes the cost of bill[2], he will calculate (2+4+6)/2 = 6. In the second case, he should refund 3 to Anna.

# Solution 
This case just want us to calculate the anna's actual bill if brian's charge and the anna's actual bill is same we need print "Bon Appetit" but if not 
we need to print brian's charge - anna's actual bill.

From here we know that anna will not eat 1 of many item in bill so we need remove the item by using pop function.

take the example from top if

$$bill = [2,4,6]$$ and anna don't eat $$k=2 or k=bill[2]$$ which is 6

So by using bill.pop(2) it will remove 6 from the array.
From that we can conclude anna's actual bill = (total all of bill - bill.pop(k))/2

```python
annaBill = (usm(bill)-bill.pop(k))//2
```

The case want us to print the whether "Bon Appetit" or integer of bill - anna's actual bill
so that's why we using "//"" not  "/"

```python
def bonAppetit(bill: list, k: int, b: int):
    annaBill = (sum(bill)-bill.pop(k))//2
    if(annaBill == b):
        print("Bon Appetit")
    else:
        print(b-annaBill)

```
