#Bryson Vogel
#Comp. Prog. 1
#17-10-16
def intro ():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
    print("Your starting planet is Earth.")
intro()
x=str(input("What is your name? ")).title()
y=int(input("How heavy is your ship? "))
z=int(input("How fast do you want to go[in kilometers per hour]? "))
v=str(input("Which of the 7 planets [not Earth], Pluto, and the Sun do you want to go to [if and when you beat earth][the Sun is Sol]? ")).lower()
earth=int(40000)
mars=int(15200)
venus=int(36400)
mercury=int(15200)
jupiter=int(96000)
saturn=int(36400)
neptune=int(35600)
uranus=int(44000)
pluto=int(3333)
sol=int(1120000)
b=earth
d=mars
f=venus
h=mercury
j=jupiter
l=saturn
n=neptune
p=uranus
r=pluto
a=((b/10)+b)
c=((d/10)+d)
e=((f/5)+f)
g=((h/10)+h)
i=((j/10)+j)
k=((l/10)+l)
m=((n/10)+n)
o=((p/10)+p)
q=((r/10)+r)
def escape_earth ():
    print("You land on Earth; planet code 1")
    if z>a:
        print("You went to fast! You lose "+x+"!")
        quit
    else:      
        if z>=b:
            print("You win and escape earth "+x+"!")
            w=str("If you want to stop, enter q. ")
            if w==("q"):
                quit
            else:
                print(v)
        else:
            print("You went to slow! You lose "+x+"!")
            quit
escape_earth()
if v==("mars"):
    def escape_mars ():
       print("You land on Mars; planet code 2")
       z=int(input("How fast do you want to go? "))
       if z>g:
            print("You fail because you went too fast!")
            quit
       else:
            if z>=h:
                print("You win and escape Mars "+x+"!")
                w=strinput(("If you want to stop, enter q. "))
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_mars()
elif v==("venus"):
    def escape_venus():
       print("You land on Venus; planet code 3")
       z=int(input("How fast do you want to go? "))
       if z>e:
            print("You fail because you went too fast!")
            quit
       else:
            if z>=f:
                print("You win and escape Venus "+x+"!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_venus()
elif v==("mercury"):
    def escape_mercury():
       print("You land on Mercury; planet code 4")
       z=int(input("How fast do you want to go? "))
       if z>c:
            print("You fail because you went too fast!")
            quit
       else:
            if z>=d:
                print("You win and escape Mercury "+x+"!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_mercury()
elif v==("jupiter"):
    def escape_jupiter():
       print("You land on Jupiter; planet code 5")
       z=int(input("How fast do you want to go? "))
       if z>g:
            print("You fail because you went too fast!")
            quit
       else:
            if z>=h:
                print("You win and escape Jupiter!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_jupiter()
elif v==("saturn"):
    def escape_saturn():
       print("You land on Saturn; planet code 6")
       z=int(input("How fast do you want to go? "))
       if z>k:
            print("You are too fast, you lose!")
            quit
       else:
            if z>=l:
                print("You win Saturn!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("Too slow, you lose!")
                quit
    escape_saturn()
elif v==("neptune"):
    def escape_neptune():
       print("You land on Neptune; planet code 7")
       z=int(input("How fast do you want to go? "))
       if z>p:
            print("Too fast, you lose!")
            quit
       else:
            if z>=o:
                print("You win Neptune!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("Too slow, you lose!")
                quit
    escape_neptune()
elif v==("uranus"):
    def escape_uranus():
       print("You land on Uranus; planet code 8")
       z=int(input("How fast do you want to go? "))
       if z>r:
            print("Too fast, you lose!")
            quit
       else:
            if z>=q:
                print("You win uranus!")
                w=str(input("If you want to stop, enter q"))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("Too slow, you lose!")
                quit
    escape_uranus()
elif v==("pluto"):
    def escape_pluto():
       print("You land on Pluto; planet code 9")
       z=int(input("how fast do you want to go? "))
       if z>t:
            print("Too fast, you lose")
            quit
       else:
            if z>=s:
                print("You win pluto!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    print(v)
            else:
                print("Too slow, you lose!")
                quit
    escape_pluto()
elif v==("sol"):
    def escape_sol():
       print("You land on Sol; planet code 10")
       z=int(input("How fast do you want to go? "))
       if z==sol:
            print("You win the expert level!")
            quit
       else:
            print("You lose, no suprise there.")
            quit
    escape_sol()
else:
  print("You entered the planet in wrong!!!")
  print("Horrible goblin!")
  quit
