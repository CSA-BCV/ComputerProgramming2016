#Bryson Vogel
#Comp. Prog. 1
#10-31-16
def intro():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
intro()
p=("earth")
def inputs():
    n=str(input("What is your name? "))
    w=int(input("What is your ship's weight? "))
    print("Your options of planets are the numbers 1-9, with 1 being Mercury, 2-8 being the rest of the planets and Pluto in order outwards, and the Sun being 9.")    
    p=int(input("What is your planet [in planet code]? "))
    s=float(input("How fast do you want to go in k/s [for earth]? "))
inputs()
def values():
    earth=11.2
    mercury=4.3
    venus=10.4
    mars=5.0
    jupiter=59.5
    saturn=35.5
    neptune=23.5
    uranus=21.3
    pluto=1.21
    sun=617.6
    pearth=earth+(earth*.1)
    pmercury=mercury+(mercury*.1)
    pvenus=venus+(venus*.1)
    pmars=mars+(mars*1)
    pjupiter=jupiter+(jupiter*.1)
    psaturn=saturn+(saturn*.1)
    pneptune=neptune+(neptune*.1)
    puranus=uranus+(uranus*.1)
    ppluto=pluto+(pluto*.1)
    psun=sun+(sun*.1)
def points():
    earthp=5
    mercuryp=2
    venusp=4
    marsp=3
    jupiterp=9
    saturnp=8
    neptunep=7
    uranusp=6
    plutop=1
    sunp=10
    points
    points=0
global values
global points
def escape_planet(s,p,points,values):
    if p==("earth")
        if s<=(earth+pearth) or s<=(earth-pearth):
            print("You beat earth "+x+"!")
            print("You have "+str(points+earthp)+".")
        else:
        if
