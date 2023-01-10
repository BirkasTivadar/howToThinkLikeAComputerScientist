# 6 .Készíts egy szabalyos_haromszog_rajzolas(t, sz) fejlécű void függvényt, mely az előző feladatban szereplő poligon_rajzolas függvényt meghívva egy szabályos háromszöget rajzoltat a teknőccel.

import turtle
from turtle import Screen, Turtle
from poligon_rajzolas import sokszog_rajzolas

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)
drawer.color("pink3")

def szabalyos_haromszog_rajzolas(t: Turtle, sz: int):
    sokszog_rajzolas(drawer, 3, sz)

szabalyos_haromszog_rajzolas(drawer, 80)

ablak.mainloop()
