#Bryson Vogel
#Comp. Prog. 1
#11-15-16
import random
def randomness ():
    minnum=int(input("What is your minimum number? \n"))
    maxnum=int(input("What is your maximum number? \n"))
    nums=int(input("How many numbers do you want generated? \n"))
    if minnum<maxnum:
        for i in range(nums):
            print(random.randrange(minnum,maxnum))
    else:
        print("Your max number is less than or equal to your minimum number!!")
randomness()
