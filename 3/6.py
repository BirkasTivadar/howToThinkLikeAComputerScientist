# 6. Használd a for ciklust, hogy egy teknőccel kirajzoltasd ezeket a szabályos sokszögeket (a szabályos azt jelenti, hogy minden oldala egyforma hosszú és minden szöge azonos):
#
# Egyenlő oldalú háromszög
# Négyzet
# Hexagon (hatszög)
# Oktagon (nyolcszög)

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()
drawer.pensize(2)

# Egyenlő oldalú háromszög
drawer.color("red")
for i in range(3):
    drawer.forward(50)
    drawer.left(120)

# Négyzet
drawer.color("blue")
for i in range(4):
    drawer.forward(70)
    drawer.left(90)

# Hexagon (hatszög)
drawer.color("green")
for i in range(6):
    drawer.forward(100)
    drawer.left(60)

# Oktagon (nyolcszög)
drawer.color("purple")
for i in range(8):
    drawer.forward(120)
    drawer.left(45)

ablak.mainloop()