#Bryson Vogel
#Comp. Prog. 1
#11-1-16
s=float(input("What is your score? "))
p=float(input("How many points did you just make? "))
def total_thing():
    total=(s+p)
    return total
print("You have "+str(total_thing())+" points now!")
