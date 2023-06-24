"""
1. Társíts még néhány billentyűt az első példaprogramhoz:

Az R, G és B billentyűk leütése változtassa meg Eszti színét pirosra (Red), zöldre (Green) és kékre (Blue).
A + és - billentyűk leütése növelje, illetve csökkentse Eszti tollának méretét. Biztosítsd, hogy a toll mérete 1 és 20 között maradjon (a határokat is beleértve).
Néhány más billentyűt is vezess be Eszti vagy az ablak különböző tulajdonságainak állítására, vagy adj Esztihez új, billentyűzettel vezérelhető viselkedést.
"""

import turtle

turtle.setup(400, 500)  # Az ablak méretének beállítása
ablak = turtle.Screen()  # Az ablak referenciájának lekérése
ablak.title("Billentyű leütés kezelése!")  # Az ablaknév módosítása
ablak.bgcolor("lightgreen")  # Háttér színének beállítása
Eszti = turtle.Turtle()  # A kedvenc teknőcünk elkészítése

size = 1


# A következő függvények az eseménykezelőink
def ek1():
    Eszti.forward(30)


def ek2():
    Eszti.left(45)


def ek3():
    Eszti.right(45)


def ekRed():
    Eszti.color("red")


def ekBlue():
    Eszti.color("blue")


def ekGreen():
    Eszti.color("green")


def ekPlusSize():
    global size
    if size < 20:
        size += 1
        Eszti.pensize(size)


def ekMinusSize():
    global size
    if size > 1:
        size -= 1
        Eszti.pensize(size)


def ek4():
    ablak.bye()  # A teknőc ablak bezárása


# Ezek a sorok rendelik össze a billentyű leütés eseményeket
#  az általunk definiált eseménykezelő függvényekkel
ablak.onkey(ek1, "Up")
ablak.onkey(ek2, "Left")
ablak.onkey(ek3, "Right")
ablak.onkey(ekRed, "r")
ablak.onkey(ekBlue, "b")
ablak.onkey(ekGreen, "g")
ablak.onkey(ekPlusSize, "+")
ablak.onkey(ekMinusSize, "-")
ablak.onkey(ek4, "q")

# Most megkérjük az ablakot, hogy kezdje el figyelni az eseményeket.
# Ha bármelyik általunk figyelt billentyűt lenyomja valaki, akkor
#  a hozzá tartozó eseménykezelő meghívásra kerül.
ablak.listen()
ablak.mainloop()
