# Írj egy sokszog_rajzolas(t, n, sz) fejlécű void függvényt, mely a teknőccel egy szabályos sokszöget rajzoltat. Ha majd meghívod a sokszog_rajzolas(Eszti, 8, 50) utasítással, akkor a 3.png képent láthatóhoz hasonló ábrát kell kapnod:

import turtle
from turtle import Screen, Turtle

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)
drawer.color("pink3")


def sokszog_rajzolas(t: Turtle, n: int, sz: int):
    fok: int = 360 // n
    for i in range(n):
        t.forward(sz)
        t.left(fok)


sokszog_rajzolas(drawer, 8, 50)

ablak.mainloop()
