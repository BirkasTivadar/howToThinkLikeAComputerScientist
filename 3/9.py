# 9. Ha egy szabályos 18 oldalú sokszöget szeretnél rajzolni, hány fokkal kellene elfordulnia a teknőcnek minden csúcsnál?
# 20

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()

for i in range(18):
    drawer.forward(50)
    drawer.left(20)

ablak.mainloop()
