# Írj egy programot, amely egy olya alakzatot rajzol, mint a 11.png ábrán.


import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()

for i in range(5):
    drawer.forward(100)
    drawer.right(144)

ablak.mainloop()