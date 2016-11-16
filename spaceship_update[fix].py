#Bryson Vogel
#Comp. Prog. 1
#17-10-16
def intro ():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
    print("Your starting planet is earth.")
intro()
x=str(input("What is your name? "))
y=int(input("how heavy is your ship? "))
z=int(input("How fast do you want to go? "))
v=str(input("Which of the 8 planets, pluto, and the sun do you want to go to [if and when you beat earth][the sun is sol]? "))
b=int(40000)
d=int(15200)
f=int(36400)
h=int(15200)
j=int(96000)
l=int(36400)
n=int(35600)
p=int(44000)
r=int(3333)
sol=int(1120000)
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
  print("you land on earth planet code 1")
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
       print("you land on mars planet code 2")
        z=int(input("how fast do you want to go? "))
        if z>g:
            print("You fail because you went too fast!")
            quit
        else:
            if z>=h:
                print("you win and escape mars "+x+"!")
                w=str("If you want to stop, enter q. ")
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
       print("you land on venus planet code 3")
        z=int(input("how fast do you want to go? "))
        if z>e:
            print("You fail because you went too fast!")
            quit
        else:
            if z>=f:
                print("you win and escape venus "+x+"!")
                w=str("If you want to stop, enter q. ")
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
       print("you land on mercury planet code 4")
        z=int(input("how fast do you want to go? "))
        if z>c:
            print("You fail because you went too fast!")
            quit
        else:
            if z>=d:
                print("you win and escape mercury "+x+"!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_mercury()
elif v==("jupiter"):
    def escape_jupiter():
       print("you land on jupiter planet code 5")
        z=int(input("how fast do you want to go? "))
        if z>g:
            print("You fail because you went too fast!")
            quit
        else:
            if z>=h:
                print("you win and escape jupiter!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("You went too slow! You lose!")
                quit
    escape_jupiter()
elif v==("saturn"):
    def escape_saturn():
       print("you land on saturn planet code 6")
        z=int(input("how fast do you want to go? "))
        if z>k:
            print("You are too fast, you lose!")
            quit
        else:
            if z>=l:
                print("you win saturn!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("too slow, you lose!")
                quit
    escape_saturn()
elif v==("neptune"):
    def escape_neptune():
       print("you land on neptune planet code 7")
        z=int(input("how fast do you want to go? "))
        if z>p:
            print("too fast, you lose!")
            quit
        else:
            if z>=o:
                print("you win neptune!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("too slow, you lose!")
                quit
    escape_neptune()
elif v==("uranus"):
    def escape_uranus():
       print("you land on uranus planet code 8")
        z=int(input("how fast do you want to go? "))
        if z>r:
            print("too fast, you lose!")
            quit
        else:
            if z>=q:
                print("you win uranus!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("too slow, you lose!")
                quit
    escape_uranus()
elif v==("pluto"):
    def escape_pluto():
       print("you land on pluto planet code 9")
        z=int(input("how fast do you want to go? "))
        if z>t:
            print("too fast, you lose")
            quit
        else:
            if z>=s:
                print("you win pluto!")
                w=str("If you want to stop, enter q. ")
                if w==("q"):
                    quit
                else:
                    print(v)
            else:
                print("too slow, you lose!")
                quit
    escape_pluto()
elif v==("sol"):
    def escape_sol():
       print("you land on sol planet code 10")
        z=int(input("how fast do you want to go? "))
        if z==sol:
            print("you win the expert level!")
            quit
        else:
            print("you lose, no suprise there.")
            quit
    escape_sol()
else:
  print("You entered the planet in wrong!!!")
  print("Horrible goblin!")
  quit
