"""
2. Változtasd meg úgy a közlekedési lámpa vezérlő programot, hogy automatikusan váltson, egy időzítő hatására.
"""

import turtle  # Eszti közlekedési lámpává válik.

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Eszti közlekedési lámpává válik.")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Sanyi = turtle.Turtle()
Green = turtle.Turtle()
Yellow = turtle.Turtle()
Red = turtle.Turtle()


def dobozRajzolasEszti():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Eszti.pensize(3)
    Eszti.color("black", "darkgrey")
    Eszti.begin_fill()
    Eszti.forward(80)
    Eszti.left(90)
    Eszti.forward(200)
    Eszti.circle(40, 180)
    Eszti.forward(200)
    Eszti.left(90)
    Eszti.end_fill()


def dobozRajzolasSanyi():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Sanyi.forward(100)
    Sanyi.pensize(3)
    Sanyi.color("black", "darkgrey")
    Sanyi.begin_fill()
    Sanyi.forward(80)
    Sanyi.left(90)
    Sanyi.forward(200)
    Sanyi.circle(40, 180)
    Sanyi.forward(200)
    Sanyi.left(90)
    Sanyi.end_fill()


dobozRajzolasEszti()
dobozRajzolasSanyi()

Eszti.penup()
# Eszti pozícionálása oda, ahol a zöld lámpának kell lennie
Eszti.forward(40)
Eszti.left(90)
Eszti.forward(50)
# Esztit egy nagy zöld körré alakítjuk át
Eszti.shape("circle")
Eszti.shapesize(3)
Eszti.fillcolor("green")

Green.penup()
# Green pozícionálása oda, ahol a zöld lámpának kell lennie
Green.forward(140)
Green.left(90)
Green.forward(50)
# Greent egy nagy zöld körré alakítjuk át
Green.shape("circle")
Green.shapesize(3)
Green.fillcolor("green")

Yellow.penup()
# Yellow pozícionálása oda, ahol a zöld lámpának kell lennie
Yellow.forward(140)
Yellow.left(90)
Yellow.forward(120)
# Yellowt egy nagy zöld körré alakítjuk át
Yellow.shape("circle")
Yellow.shapesize(3)
Yellow.fillcolor("orange")

Red.penup()
# Red pozícionálása oda, ahol a zöld lámpának kell lennie
Red.forward(140)
Red.left(90)
Red.forward(190)
# Redet egy nagy zöld körré alakítjuk át
Red.shape("circle")
Red.shapesize(3)
Red.fillcolor("red")

# A közlekedési lámpa egyfajta állapotautomata, három állapottal:
#  zölddel, sárgával és pirossal. Az állapotokat rendre
#  0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:  # Átmenet a 0. állapotból az 1. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        Green.hideturtle()
        Yellow.showturtle()
        allapot_sorszam = 1
    elif allapot_sorszam == 1:  # Átmenet az 1. állapotból a 2. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("red")
        Yellow.hideturtle()
        Red.showturtle()
        allapot_sorszam = 2
    else:  # Átmenet a 2. állapotból az 0. állapotba
        Eszti.back(140)
        Eszti.fillcolor("green")
        Red.hideturtle()
        Green.showturtle()
        allapot_sorszam = 0
    ablak.ontimer(allapot_automata_esemenykezeloje, 1000)


allapot_automata_esemenykezeloje()
ablak.mainloop()
