"""
4. A közlekedési lámpák fényeit most már különböző teknőcök jelenítik meg a programban.
A látható/nem látható trükk nem volt túl jó ötlet.
Ha megnézünk egy közlekedési lámpát, akkor azt látjuk, hogy a különböző színű lámpák bekapcsolnak majd lekapcsolódnak, de akkor is látszanak, amikor éppen nem világítanak, csak egy kicsit sötétebb a színűk.
Módosítsd úgy a programot, hogy ne tűnjenek el a lámpák sem kikapcsolt, sem bekapcsolt állapotban.
Kikapcsolt állapotban is lehessen valamennyire látni a lámpákat.
"""

import turtle

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Életszerűbb közlekedési lámpa.")
ablak.bgcolor("lightgreen")
Lampa = turtle.Turtle()
Green = turtle.Turtle()
Yellow = turtle.Turtle()
Red = turtle.Turtle()


def lampaRajzolas():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Lampa.pensize(3)
    Lampa.color("black", "darkgrey")
    Lampa.begin_fill()
    Lampa.forward(80)
    Lampa.left(90)
    Lampa.forward(200)
    Lampa.circle(40, 180)
    Lampa.forward(200)
    Lampa.left(90)
    Lampa.end_fill()


lampaRajzolas()

Red.penup()
# Red pozícionálása oda, ahol a zöld lámpának kell lennie
Red.forward(40)
Red.left(90)
Red.forward(190)
# Redet egy nagy zöld körré alakítjuk át
Red.shape("circle")
Red.shapesize(3)
Red.fillcolor("red")

Green.penup()
# Green pozícionálása oda, ahol a zöld lámpának kell lennie
Green.forward(40)
Green.left(90)
Green.forward(50)
# Greent egy nagy zöld körré alakítjuk át
Red.color("DarkRed")
Green.shape("circle")
Green.shapesize(3)
Green.fillcolor("green")

Yellow.penup()
# Yellow pozícionálása oda, ahol a zöld lámpának kell lennie
Yellow.forward(40)
Yellow.left(90)
Yellow.forward(120)
# Yellowt egy nagy zöld körré alakítjuk át
Green.color("DarkGreen")
Yellow.shape("circle")
Yellow.shapesize(3)
Yellow.fillcolor("orange")

# A közlekedési lámpa egyfajta állapotautomata, három állapottal:
#  zölddel, sárgával és pirossal. Az állapotokat rendre
#  0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:  # Átmenet a 0. állapotból az 1. állapotba
        Green.color("DarkGreen")
        Yellow.color("orange")
        allapot_sorszam = 1
    elif allapot_sorszam == 1:  # Átmenet az 1. állapotból a 2. állapotba
        Yellow.color("DarkOrange4")
        Red.color("red")
        allapot_sorszam = 2
    else:  # Átmenet a 2. állapotból az 0. állapotba
        Red.color("DarkRed")
        Green.color("green")
        allapot_sorszam = 0
    ablak.ontimer(allapot_automata_esemenykezeloje, 1000)


allapot_automata_esemenykezeloje()
ablak.mainloop()
