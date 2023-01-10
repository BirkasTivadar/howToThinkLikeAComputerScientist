# 10. Bővítsd ki az előző feladatot programmá. Rajzolj öt csillagot, de minden egyes csillag rajzolása közt emeled fel a tollat, haladj előre 650 egységet és fordulj jobbra 144 fokkal, majd rakd le a tollat. Valami ilyesmit kell kapnod: 10.png

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")
drawer: Turtle = turtle.Turtle()
drawer.pensize(2)
drawer.color("pink3")

def csillag_rajzolas(t: Turtle):
    for i in range(5):
        t.forward(100)
        t.right(144)

def ot_cillag_rajzolas(t: Turtle):
    for i in range(5):
        csillag_rajzolas(t)
       # t.penup()
        t.forward(650)
        t.right(144)
       # t.pendown()


ot_cillag_rajzolas(drawer)

ablak.mainloop()