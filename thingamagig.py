#Bryson Vogel
#Comp. Prog. 1
#17-10-16
def intro ():
    print("Hello, welcome to the space jumping game!")
    print("The object is to get your custom ship to each planet in the solar system by manipulating the weight and speed")
    print("Your starting planet is earth.")
intro()
x=str(input("What is your name? "))
y=(int(input("how heavy is your ship? ")
z=(int(input("How fast do you want to go? ")))
earth = int(40000)
mercury = int(15200)
venus = int(36400)
mars = int(15200)
jupiter = int(96000)
saturn = int(36400)
uranus = int(35600)
neptune = int(44000)
pluto = int(3333)
sol = int(1120000)
b=earth
a=((b/10)+b)
d=mercury
c=((d/10)+d)
f=venus
e=((f/5)+f)
h=mars
g=((h/10)+h)
j=jupiter
i=((j/10)+j)
l=saturn
k=((l/10)+l)
n=uranus
m=((n/10)+n)
p=neptune
o=((p/10)+p)
r=pluto
q=((r/10)+r)
planet = str(input("Which planet do you want to go to (of the 8, plus pluto and the sun [called sol])? "))
def escape_earth (b,a,y,z):
  	if z>a:
  		print("You went to fast! You lose "+x+"!")
       break()
	  else:      
		  if z>=b:
    	  print("You win and escape earth "+x+"!")
    	  print(x)
		  else:
    	  print("You went to slow! You lose "+x+"!")
			  break()
exept TypeError:
  print("Stop is mr. davis!")
  break()
if planet==mars:
  	def escape_mars (h,g,z,y):
		if z>g:
      print("You fail because you went too fast!")
      break()
		else:
			if z>=h:
      	print("you win and escape mars "+x+"!")
      	print(x)
			else:
				print("You went too slow! You lose!")
				break()
	escape_mars()
elif planet==venus:
	def escape_venus:
		if z>e:
      print("You fail because you went too fast!")
      break()
		else:
			if z>=f:
      	print("you win and escape venus "+x+"!")
      	print(x)
			else:
				print("You went too slow! You lose!")
				break()
	escape_venus()
elif planet==mercury:
	def escape_mercury:
		if z>c:
      print("You fail because you went too fast!")
      break()
		else:
			if z>=d:
      	print("you win and escape mercury "+x+"!")
      	print(x)
			else:
				print("You went too slow! You lose!")
				break()
	escape_mercury()
elif planet==jupiter:
    def escape_jupiter:
			if z>g:
        print("You fail because you went too fast!")
        break()
			else:
				if z>=h:
      		print("you win and escape jupiter!")
      		print(x)
				else:
					print("You went too slow! You lose!")
					break()
	escape_jupiter()
elif planet==saturn:
	def escape_saturn:
	  if z>k:
	    print("You are too fast, you lose!")
	    break()
    else:
      if z>=l:
        print("you win saturn!")
        print(x)
      else:
        print("too slow, you lose!")
        break()
elif planet==neptune:
	def escape_neptune:
	  if z>p:
	    print("too fast, you lose!")
	    break()
    else:
      if z>=o:
        print("you win neptune!")
        print(x)
      else:
        print("too slow, you lose!")
        break()
elif planet==uranus:
	def escape_uranus:
	  if z>r:
	    print("too fast, you lose!")
	    break()
    else:
      if z>=q:
        print("you win uranus!")
        print(x)
      else:
        print("too slow, you lose!")
        break()
elif planet==pluto:
	def escape_pluto:
	  if z>t:
	    print("too fast, you lose")
	    break()
    else:
      if z>=s:
        print("you win pluto!")\
        print(x)
      else:
        print("too slow, you lose!")
        break()
elif planet==sol:
	global def escape_sol:
    if z==sol:
      print("you win the expert level!")
      break()
    else:
      print("you lose, no suprize there.")
      break()
elif planet==sun:
escape_sol()
else:
  print("You entered the planet in wrong!!!")
  print("Horrible goblin!")
  break()
