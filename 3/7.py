# 7. Egy részeg kalóz véletlenszerűen fordul egyet majd megy 100 lépést, tesz még egy véletlen fordulatot és még 100 lépést, és így tovább. Egy bölcsész hallgató feljegyzi az összes fordulat szögét mielőtt a kalóz megtenné a következő 100 lépést. Az ő kísérletének adatai [160, -43, 270, -97, -43, 200, -940, 17, -86]. (A pozitív szögek az óra járásával ellentétes irányúak.) Használj egy teknőcöt, hogy kirajzold részeg barátunk útvonalát!

import turtle
from turtle import Turtle, Screen

ablak: Screen = turtle.Screen()
drawer: Turtle = turtle.Turtle()

angles: list[int] = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in angles:
    drawer.left(i)
    drawer.forward(100)

ablak.mainloop()