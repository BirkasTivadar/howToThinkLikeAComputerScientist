# 12. Írj egy programot, ami rajzol egy olyan óralapot, mint a 12.png ábrán

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.color("blue")
drawer.shape("turtle")
drawer.pensize(3)

drawer.stamp()

for i in range(12):
    drawer.penup()
    drawer.forward(100)
    drawer.pendown()
    drawer.forward(10)
    drawer.penup()
    drawer.forward(20)
    drawer.stamp()
    drawer.backward(130)
    drawer.left(30)

ablak.mainloop()