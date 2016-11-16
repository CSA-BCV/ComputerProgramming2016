#Bryson Vogel
#Comp. Prog. 1
#10-5-16
import turtle
wn=turtle.Screen()
x=turtle.Turtle()
x.lt(90)
x.speed(.5)
b=15
def draw_flower ():    
    for i in range (4):
        for i in range (180):
            x.fd(1)
            x.right(.6)
        x.rt(70)
        for i in range (180):
            x.fd(1)
            x.right(.6)
        x.left(b)
        x.up()
        x.setx(0.0)
        x.sety(0.0)
        x.down()
draw_flower()
p=turtle.Turtle()
def drawp():
    for i in range(6):
        p.fd(75)
        p.lt(120)
        p.fd(75)
        p.lt(120)
        p.fd(75)
        p.lt(180)
