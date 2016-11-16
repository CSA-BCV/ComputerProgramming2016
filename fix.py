#Bryson Vogel
#Comp. Prog. 1
#17-10-16
def intro():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
intro()
n=str(input("What is your name? "))
w=int(input("What is your ship's weight? "))
print("Your options of planets are the numbers 1-9, with 1 being Mercury, 2-8 being the rest of the planets and Pluto in order outwards, and the Sun being 9.")    
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
points=0
def escape_earth():
    s=float(input("How fast do you want to go[in km/s]? "))
    if (pearth+earth)>=s or s<=(earth-pearth):
        print("You escape earth!")
        global points print("you have "+str(points+earthp)+" points!")
    else:
        print("you have "+str(points-earthp)+" points!")
        if s>(earth+pearth):
            print("You went too fast!")
        else:
            print("You went too slow!")
        quit()
    return points
def nquit():
    q=input("If you want to quit, enter quit. If not, enter literally anything else. ")
    if q==("quit"):
        print(points)
        quit()
    else:
        print("Moving on then...")
escape_earth()
nquit()
def escape_planet():
   p=int(input("What planet do you want to go to? "))
   if p==1:
       s=float(input("How fast do you want to go[in km/s]? "))
       if (pmercury+mercury)>=s or s<=(mercury-pmercury):
           print("You escape from Mercury "+n+"!")
           nquit()
           global points print("you have "+str(points+mercuryp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
           
       else:
           global points print("you have "+str(points-mercuryp)+" points!")
           if s>(pmercury+mercury):
               print("you went too fast!")
           else:
               print("You went too slow!")
       quit()
       return points
   elif p==2:
       s=float(input("How fast do you want to go[in km/s]? "))
       if (pvenus+venus)>=s or s<=(venus-pvenus):
           print("You escape from Venus "+n+"!")
           nquit()
           global points print("you have "+str(points+venusp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
       else:
           global points print("you have "+str(points-venusp)+" points!")
           if s>(pvenus+venus):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
       return points
   elif p==3:
       s=float(input("How fast do you want to go[in km/s]? "))
       if (pmars+mars)>=s or s<=(mars-pmars):
           print("You escape from Mars "+n+"!")
           nquit()
           global points print("you have "+str(points+marsp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
       else:
            global points print("you have "+str(points-marsp)+" points!")
            if s>(pmars+mars):
                print("You went too fast!")
            else:
                print("You went too slow!")
            quit()
       return points
   elif p==4:
       s=float(input("How fast do you want to go[in km/s]? "))
       if (pjupiter+jupiter)>=s or s<=(jupiter-pjupiter):
           print("You escape from Jupiter "+n+"!")
           nquit()
           global points print("you have "+str(points+jupiterp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
       else:
          global points print("you have "+str(points-jupiterp)+" points!")
          if s>(pjupiter+jupiter):
               print("you went too fast!")
          else:
               print("You went too slow!")
          quit() 
       return points
   elif p==5:
     s=float(input("How fast do you want to go[in km/s]? "))
     if (psaturn+saturn)>=s or s<=(saturn-psaturn):
           print("You escape from Saturn "+n+"!")
           nquit()
           global points print("you have "+str(points+saturnp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
     else:
           global points print("you have "+str(points-saturnp)+" points!")
           if s>(psaturn+saturn):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
     return points
   elif p==6:
        s=float(input("How fast do you want to go[in km/s]? "))
        if (pneptune+neptune)>=s or s<=(neptune-pneptune):
            print("You escape from Neptune "+n+"!")
            nquit()
            global points print("you have "+str(points+neptunep)+" points!")
            p=int(input("What planet do you want to go to? "))
            escape_planet()
        else:
           global points print("you have "+str(points-neptunep)+" points!")
           if s>(pneptune+neptune):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
        return points
   elif p==7:
        s=float(input("How fast do you want to go[in km/s]? "))
        if (puranus+uranus)>=s or s<=(uranus-puranus):
           print("You escape from Uranus "+n+"!")
           nquit()
           global points print("you have "+str(points+uranusp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
        else:
           print("you have "+str(global points-uranusp)+" points!")
           if s>(puranus+uranus):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
        return points
   elif p==8:
     s=float(input("How fast do you want to go[in km/s]? "))
     if (ppluto+pluto)>=s or s<=(pluto-ppluto):
           print("You escape from Pluto "+n+"!")
           nquit()
           print("you have "+str(global points+plutop)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
     else:
           print("you have "+str(global points-plutop)+" points!")
           if s>(ppluto+pluto):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
     return points
   elif p==9:
     s=float(input("How fast do you want to go[in km/s]? "))
     if (psol+sol)>=s or s<=(sol-psol):
           print("You escape from The Sun "+n+"!")
           nquit()
           print("you have "+str(global points+sunp)+" points!")
           p=int(input("What planet do you want to go to? "))
           escape_planet()
     else:
           print("you have "+str(global points-sunp)+" points!")
           if s>(psol+sol):
               print("you went too fast!")
           else:
               print("You went too slow!")
           quit()
     return points
   else:
       print("Error.")
escape_planet()
