#Bryson Vogel
#Comp. Prog. 1
#17-10-16
def intro ():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
    print("Your starting planet is Earth.")    #the intro
intro()
x=str(input("What is your name? ")).title()
y=int(input("How heavy is your ship? ")) #the inputs
earth=int(40000)
mars=int(15200)
venus=int(36400)
mercury=int(15200)
jupiter=int(96000)
saturn=int(36400)
neptune=int(35600)
uranus=int(44000)
pluto=int(3333)
sol=int(1120000)     #the values for the speeds
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
q=((r/10)+r)      #the values for the max. speed and some varible assignments to mak things match up
points=0          #the beginning value for the points
earth_points=1
mars_points=2
venus_points=3
mercury_points=2
jupiter_points=5
saturn_points=4
neptune_points=4
uranus_points=3
pluto_points=1
sol_points=6
sol_defeat=3       #the point values for each planet
print("Your options for the planet code, in order from the one represented by the number 2 to the one represented by 10 are: mars, venus, mercury, jupiter, saturn, neptune, uranus, pluto, and the sun") 
def escape_earth ():
    print("You land on Earth")
    z=int(input("How fast do you want to go[in kilometers per hour]? "))
    if z>a:
        print("You went to fast! You lose "+x+"!")
        points-earth_points
        escape_earth()
    else:      
        if z>=b:
            print("You win and escape earth "+x+"!")
            print("You now have "+str(points+earth_points)+" points!")
            w=str(input("If you want to stop, enter q. ")).lower()
            if w==("q"):
                quit
            else:
                print("Moving on...")
        else:
            print("You went to slow! You lose "+x+"!")
            points-earth_points
            escape_earth()
escape_earth()    #the win/lose code for earth
v=int(input("Were do you want to go to now? "))
if v==(2): #It won't accept the value I enter for v here...
    def escape_mars():
        print("Welcome to Mars; planet code 2")
        z=int(input("How fast do you want to go? "))
        if z>c:
            print("You fail because you went too fast!")
            points-mars_points
            v=int(input("Which planet do you want to go to now? "))
        else:
            if z==d:
                print("You win and escape Mars "+x+"!")
                print("You now have "+str(points+mars_points)+" points!")
                w=str(input("If you want to stop, enter any letter or number. "))
                if w==(""):
                    v=int(input("Which planet do you want to go to now? "))
                else:
                    quit
            else:
                print("You went too slow!")
                points-mars_points
                v=int(input("Which planet do you want to go to now? ")) #the win/lose code for mars
if v==(3):
    def escape_venus():
       print("You land on Venus; planet code 3")
       z=int(input("How fast do you want to go? "))
       if z>e:
            print("You fail because you went too fast!")
            points-venus_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=f:
                print("You win and escape Venus "+x+"!")
                print("You now have "+str(points+venus_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q"):
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("You went too slow! You lose!")
                points-venus_points
                v=int(input("Which planet do you want to go to now? "))
    escape_venus() #the win/lose code for venus
elif v==(4):
    def escape_mercury():
       print("You land on Mercury; planet code 4")
       z=int(input("How fast do you want to go? "))
       if z>c:
            print("You fail because you went too fast!")
            points-mercury_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=d:
                print("You win and escape Mercury "+x+"!")
                print("You now have "+str(points+mercury_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("You went too slow! You lose!")
                points-mercury_points
                v=int(input("Which planet do you want to go to now? "))
    escape_mercury() #aaaaand so on, i'm sure you get it.
elif v==(5):
    def escape_jupiter():
       print("You land on Jupiter; planet code 5")
       z=int(input("How fast do you want to go? "))
       if z>g:
            print("You fail because you went too fast!")
            points-jupiter_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=h:
                print("You win and escape Jupiter!")
                print("You now have "+str(points+jupiter_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("You went too slow! You lose!")
                points-jupiter_points
                v=int(input("Which planet do you want to go to now? "))
    escape_jupiter()
elif v==(6):
    def escape_saturn():
       print("You land on Saturn; planet code 6")
       z=int(input("How fast do you want to go? "))
       if z>k:
            print("You are too fast, you lose!")
            points-saturn_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=l:
                print("You win Saturn!")
                print("You now have "+str(points+saturn_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("Too slow, you lose!")
                points-saturn_points
                v=int(input("Which planet do you want to go to now? "))
    escape_saturn()
elif v==(7):
    def escape_neptune():
       print("You land on Neptune; planet code 7")
       z=int(input("How fast do you want to go? "))
       if z>p:
            print("Too fast, you lose!")
            points-neptune_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=o:
                print("You win Neptune!")
                print("You now have "+str(points+neptune_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("Too slow, you lose!")
                points-neptune_points
                v=int(input("Which planet do you want to go to now? "))
    escape_neptune()
elif v==(8):
    def escape_uranus():
       print("You land on Uranus; planet code 8")
       z=int(input("How fast do you want to go? "))
       if z>r:
            print("Too fast, you lose!")
            points-uranus_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=q:
                print("You win uranus!")
                print("You now have "+str(points+uranus_points)+" points!")
                w=str(input("If you want to stop, enter q"))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("Too slow, you lose!")
                points-uranus_points
                v=int(input("Which planet do you want to go to now? "))
    escape_uranus()
elif v==(9):
    def escape_pluto():
       print("You land on Pluto; planet code 9")
       z=int(input("how fast do you want to go? "))
       if z>t:
            print("Too fast, you lose")
            points-pluto_points
            v=int(input("Which planet do you want to go to now? "))
       else:
            if z>=s:
                print("You win pluto!")
                print("You now have "+str(points+pluto_points)+" points!")
                w=str(input("If you want to stop, enter q. "))
                if w==("q").lower():
                    quit
                else:
                    v=int(input("Which planet do you want to go to now? "))
            else:
                print("Too slow, you lose!")
                points-pluto_points
                v=int(input("Which planet do you want to go to now? "))
    escape_pluto()
elif v==(10):
    def escape_sol():
       print("You land on Sol; planet code 10")
       z=int(input("How fast do you want to go? "))
       if z==sol:
            print("You win the expert level!")
            print("You now have "+str(points+sol_points)+" points!")
            v=int(input("Which planet do you want to go to now? "))
       else:
            print("You lose, no suprise there.")
            points-sol_defeat
            v=int(input("Which planet do you want to go to now? "))
    escape_sol()
else:
    print("You entered the planet in wrong!!!")
    print("Horrible goblin!")
    quit
