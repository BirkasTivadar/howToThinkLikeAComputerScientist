# 9. Készíts egy void függvényt, mely egy olyan csillagot rajzol ki, melynek minden oldala pontosan 100 egység hosszúságú. (Segítség: 144 fokkal kell elforgatni a teknőcöt minden csúcsban.)

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()
drawer.pensize(2)


def csillag_rajzolas(t: Turtle):
    for i in range(5):
        t.forward(100)
        t.right(144)


csillag_rajzolas(drawer)

ablak.mainloop()
