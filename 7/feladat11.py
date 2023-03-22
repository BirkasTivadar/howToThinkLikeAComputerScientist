import turtle
from turtle import Screen, Turtle

"""
11. Emlékezz a részeg kalóz problémára a 3. fejezet feladataiból! Most a részeg kalóz tesz egy fordulatot és pár lépést előre, majd ezt ismételgeti. A bölcsészhallgatónk feljegyzi a mozgás adatpárjait: az elfordulás szöge és az ezt követő lépések száma. A kísérleti adatai ezek: [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Használj egy teknőcöt a pityókás barátunk útvonalának megjelenítéséhez!
"""

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)

movingDatas = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (distance, angle) in movingDatas:
    drawer.forward(distance)
    drawer.left(angle)

ablak.mainloop()
