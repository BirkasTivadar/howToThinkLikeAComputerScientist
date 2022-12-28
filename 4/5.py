# 5. Az 5.png ábrán lévő két spirál csak a fordulási szögben tér el. Rajzold meg mind a kettőt.

import turtle
from turtle import Screen, Turtle

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")


def spiral_rajzolas(teknoc: Turtle, meret: int, fok: int):
    teknoc.right(90)
    noveles: int = meret
    for i in range(99):
        teknoc.forward(meret)
        teknoc.right(fok)
        meret += noveles


sima_spiral_drawer: Turtle = turtle.Turtle()
sima_spiral_drawer.pensize(2)
sima_spiral_drawer.color("blue")
sima_spiral_drawer.speed(0)

sima_spiral_drawer.penup()
sima_spiral_drawer.backward(300)
sima_spiral_drawer.pendown()

ferde_spiral_drawer: Turtle = turtle.Turtle()
ferde_spiral_drawer.pensize(2)
ferde_spiral_drawer.color("blue")
ferde_spiral_drawer.speed(0)

ferde_spiral_drawer.penup()
ferde_spiral_drawer.forward(300)
ferde_spiral_drawer.pendown()

# elso ábra
spiral_rajzolas(sima_spiral_drawer, 4, 90)

# második ábra
spiral_rajzolas(ferde_spiral_drawer, 4, 89)

ablak.mainloop()
