# 8. Módosítsd a teknőcös oszlopdiagram rajzoló programot, hogy a 200 és annál nagyobb értékű oszlopok kitöltése piros legyen, amelyek értéke a [100 és 200) intervallumban vannak, legyenek sárgák és a 100 alattiak zöldek.

import turtle


def szinbeallitas(t: turtle, magassag: int):
    if (magassag >= 200):
        t.color('blue', 'red')
    elif (magassag >= 100):
        t.color('blue', 'yellow')
    else:
        t.color('blue', 'green')


def rajzolj_oszlopot(t: turtle, magassag: int):
    szinbeallitas(t, magassag)
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write("  " + str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)

ablak.mainloop()
