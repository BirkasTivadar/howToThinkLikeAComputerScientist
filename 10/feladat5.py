"""
5. A közlekedési lámpa vezérlő programod szabadalmaztatva lett, így arra számítasz, hogy nagyon gazdag leszel.
Egy új ügyfeled azonban változtatást igényel.
Négy állapotot akar az automatában: zöldet, zöldet és sárgát együtt, csak sárgát és csak pirosat.
Ráadásul azt is szeretné, ha a különböző állapotokhoz különböző időtartam társulna.
Az állapotautomatának 3 másodpercet kell a zöld állapotban töltenie, amit 1 másodperc zöld+sárga állapot követ.
Utána 1 másodperc sárga állapot jön, majd 2 másodperc piros következik.
Változtasd meg az automata működési logikáját!
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
    Lampa.hideturtle()


lampaRajzolas()

Red.penup()
# Red pozícionálása oda, ahol a piros lámpának kell lennie
Red.forward(40)
Red.left(90)
Red.forward(190)
# Redet egy nagy piros körré alakítjuk át
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
# Yellow pozícionálása oda, ahol a sárga lámpának kell lennie
Yellow.forward(40)
Yellow.left(90)
Yellow.forward(120)
# Yellowt egy nagy sárga körré alakítjuk át
Green.color("DarkGreen")
Yellow.shape("circle")
Yellow.shapesize(3)
Yellow.fillcolor("orange")

# A közlekedési lámpa egyfajta állapotautomata, négy állapottal:
#  zölddel, zöld és sárga együtt, sárgával és pirossal.
# Az állapotokat rendre 0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapotSorszam = 0
timer = 1000


def allapot_automata_esemenykezeloje():
    global allapotSorszam
    global timer
    if allapotSorszam == 0:  # Átmenet a 0. állapotból az 1. állapotba
        Green.color("DarkGreen")
        Yellow.color("orange")
        allapotSorszam = 1
    elif allapotSorszam == 1:  # Átmenet az 1. állapotból a 2. állapotba
        Yellow.color("DarkOrange4")
        Red.color("red")
        allapotSorszam = 2
        timer = 2000
    elif allapotSorszam == 2:  # Átmenet az 1. állapotból a 2. állapotba
        Red.color("DarkRed")
        Green.color("green")
        allapotSorszam = 3
        timer = 3000
    else:  # Átmenet a 2. állapotból az 0. állapotba
        Yellow.color("orange")
        allapotSorszam = 0
        timer = 1000
    ablak.ontimer(allapot_automata_esemenykezeloje, timer)


allapot_automata_esemenykezeloje()
ablak.mainloop()
