def countingValleys(steps, path):
    arrStep = list(path)
    movementStep = 0
    downValley = 0
    for i in arrStep:
        if i == "D":
            if( movementStep == 0 and movementStep-1 < 0):
                movementStep -= 1
                downValley += 1
            else:
                movementStep -= 1
        else:
            movementStep += 1 
    return downValley

steps = 8
path = "UDDDUDUU"
print(countingValleys(steps, path)) # the result should be 1
