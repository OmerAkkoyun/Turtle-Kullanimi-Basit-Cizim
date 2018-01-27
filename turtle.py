import turtle
import random

star = turtle.Turtle()
star.speed(0.2)
renk=("yellow","blue","cyan","red","green","orange","pink")

a=0
arti=80
yon=144
while a<750:
    rastgele = random.choice(renk)
    star.forward(arti)
    star.color(rastgele)
    star.right(yon)
    star.color(rastgele)
    a+=1
    arti+=0.3
    yon+=0.2
turtle.done()