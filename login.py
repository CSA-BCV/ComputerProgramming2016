#Bryson Vogel
#Comp. Prog. 1
#10-7-16
incorrect = 0
def login_correct (x):
    print("hi, "+x+"!")
def login_incorrect():
    incorrect=incorrect+1
    if incorrect>=3:
        print("You are not an employee, you shall not pass!")
        quit(1)
    return incorrect
def login():
    name=input("What is your name? ")
    pw=("bob")
    entry=input("password? ")
    if pw==entry:
        login_correct(name)
    else:
        login_incorrect()
        login()
login()
