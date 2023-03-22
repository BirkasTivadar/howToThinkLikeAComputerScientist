import turtle
from turtle import Screen, Turtle

"""
12. Sok érdekes alakzat kirajzolható a teknőcökkel, ha a fentihez hasonló adatpárokat adunk nekik, ahol az első érték egy szög a második pedig egy távolság. Készítsd el az értékpár listát, és rajzoltasd ki a teknőccel a 12.png kñpen bemutatott házat! Ez elkészíthető anélkül, hogy egyszer is felemelnénk a tollat vagy egy vonalat duplán rajzolnánk.
"""
ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)

tess_house = [(50, 90), (50, 30), (50, 120), (50, 30), (50, 135), (5000 ** 0.5, 135), (50, 135), (5000 ** 0.5, 45)]
for (distance, angle) in tess_house:
    drawer.forward(distance)
    drawer.left(angle)

ablak.mainloop()
