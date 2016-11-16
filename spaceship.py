#Bryson Vogel
#Comp. Prog. 1
#17-10-16

def intro ():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
    print("Your starting planet is Earth.")    #the intro
intro()
def inputs():
    x=str(input("What is your name? ").title)
    y=float(input("What is your ship's weight?"))
   #the values for the speeds
def values ():
    print("The planet code is the order of the plantes in the solar system from 1-9 [skipping earth, the sun is 10]")
    v=int(input("Where do you want to go in planet code? "))

    if(1>=v<=10):
        escape_planet(v)
    else:
        print("Error")
def escape_planet(v):
    earth=40000
    mars=15200
    venus=36400
    mercury=15200
    jupiter=96000
    saturn=36400
    neptune=35600
    uranus=44000
    pluto=3333
    sol=1120000 

