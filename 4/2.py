# 2.Írj egy programot, mely a 2.png megfelelő alakzatot rajzolja ki. A legbelső négyzet minden oldala 20 egység hosszú. A többi négyzet oldalhosszúsága minden esetben 20 egységgel nagyobb, mint az általa tartalmazott legnagyobb négyzet oldalhosszúsága.

import turtle
from turtle import Screen, Turtle

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)
drawer.color("pink3")


def negyzet_rajzolas(teknoc: Turtle, oldal: int):
    for i in range(4):
        teknoc.forward(oldal)
        teknoc.left(90)


def egyre_nagyobb_negyzetek(teknoc: Turtle, meret: int, darab: int):
    noveles: int = meret
    tav: int = meret // 2
    for i in range(darab):
        teknoc.pendown()
        negyzet_rajzolas(teknoc, meret)
        teknoc.penup()
        teknoc.backward(tav)
        teknoc.right(90)
        teknoc.forward(tav)
        teknoc.left(90)
        meret += noveles


egyre_nagyobb_negyzetek(drawer, 20, 5)

ablak.mainloop()
