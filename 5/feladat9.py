# 9. A teknőcös oszlopdiagram rajzoló programban mit gondolsz, mi történik, ha egy vagy több érték a listán negatív? Próbáld ki! Változtasd meg a programot úgy, hogy a negatív értékű oszlopok felirata az oszlop alá essen.

import turtle


def magassag_iras(t: turtle, magassag: int):
    if magassag < 0:
        t.penup()
        t.backward(15)
        t.write("  " + str(magassag))
        t.forward(15)
        t.pendown()
    else:
        t.write("  " + str(magassag))


def rajzolj_oszlopot(t: turtle, magassag: int):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    magassag_iras(t, magassag)
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

xs = [48, 117, -200, 240, -160, 260, 220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)

ablak.mainloop()
