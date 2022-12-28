# 4. Rajzold meg a 4.png képen látható gyönyörű ábrát.

import turtle
from turtle import Screen, Turtle

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(2)
drawer.color("blue")


def negyzet_rajzolas(teknoc: Turtle, oldal: int):
    for i in range(4):
        teknoc.forward(oldal)
        teknoc.left(90)


def negyzethalo_rajzolas(teknoc: Turtle, kis_oldal: int):
    for i in range(4):
        negyzet_rajzolas(teknoc, kis_oldal)
        teknoc.left(90)


def abra_rajzolas(teknoc: Turtle, kis_oldal: int):
    for i in range(5):
        negyzethalo_rajzolas(teknoc, kis_oldal)
        teknoc.left(18)


abra_rajzolas(drawer, 60)

ablak.mainloop()
