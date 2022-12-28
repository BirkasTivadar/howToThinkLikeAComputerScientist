# 8. Fejleszd a programod, hogy a végén azt is megmondja, milyen irányba néz a pityókás kalóz a botorkálása végén! (Tételezzük fel, hogy a 0 irányból indul.)

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()

angles: list[int] = [160, -43, 270, -97, -43, 200, -940, 17, -86]

direction = 0

for angle in angles:
    direction += angle
    drawer.left(angle)
    drawer.forward(100)

print(direction % 360)

ablak.mainloop()