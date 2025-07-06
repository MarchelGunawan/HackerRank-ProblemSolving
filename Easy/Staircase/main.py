# This question just want you to make staircase like This
#    #
#   ##
#  ###
# ####

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

staircase(4)
