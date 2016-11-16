#Bryson Vogel
#Comp. Prog. 1
#12-10-16
x=float(input("What is your first side? "))
y=float(input("What is your second side? "))
z=float(input("What is your third side? "))
if (x-y)<=.001:
    x==y
if x**2+y**2==z**2:
    print("Your triangle is a right triangle!!!")
else:
    print("Your triangle is either not a right trangle or an error occured.")
