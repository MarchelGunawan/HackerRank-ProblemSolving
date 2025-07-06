# Staircase
Staircase detail

This is a staircase of size 
$n = 4$
:
```
   #
  ##
 ###
####
```

Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .
# Solution
```python
def staircase(n: int):
    for i in range(n,0,-1):
        """
            This step is for make the hollow staircase
        """
        for j in range(1,i):
            print(" ", end="")
        """
            This step us for make the staircase 
        """
        for j in range(n+1,i,-1):
            print("#", end="")
        print("")
```
