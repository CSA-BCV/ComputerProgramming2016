#Bryson Vogel
#Comp. Prog. 1
#11-15-16
def divis():
    num=int(input("What is your number? "))
    if num%2==0:
        print(int(num/2))
    else:
        print("Not divisible by 2")
    if num%5==0:
        print(int(num/5))
    else:
        print("Is not divisible by 5")
    if num%6==0:
        print(int(num/6))
    else:
        print("is not divisible by 6")
divis()
