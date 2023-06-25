"""
3. Az egyik korábbi fejezetben találkoztunk a hideturtle és a showturtle metódusokkal, amelyekkel elrejthetők, illetve megjeleníthetők a teknőcök.
A két metódus lehetővé teszi, hogy egy másik megközelítést alkalmazzunk a közlekedési lámpa vezérlésére készített program fejlesztésénél.
Egészítsd ki a programod a következőkkel. Rajzolj egy második dobozt az újabb lámpák tárolására.
Készíts három különböző teknőcöt a zöld, sárga és a zöld lámpák reprezentálásához, és tedd őket az új lámpadobozba.
Az állapotváltáskor csak tegyél egy teknőcöt láthatóvá a háromból. Amikor készen vagy dőlj hátra, és mélyedj el a gondolataidban.
Két különböző megoldásod van, mindkettő működőképesnek látszik.
Jobb-e valamilyen szempontból az egyik megoldás, mint a másik?
Melyik áll közelebb a valósághoz?
Melyik hasonlít jobban a városodban lévő közlekedési lámpák működéséhez?
"""

import turtle  # Eszti és Sanyi közlekedési lámpává válik.

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Két közlekedési lámpa összehasonlítása")
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
    Sanyi.hideturtle()


dobozRajzolasEszti()
dobozRajzolasSanyi()

Eszti.penup()
Eszti.forward(40)
Eszti.left(90)
Eszti.forward(50)
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
# Yellow pozícionálása oda, ahol a sárga lámpának kell lennie
Yellow.forward(140)
Yellow.left(90)
Yellow.forward(120)
# Yellowt egy nagy sárga körré alakítjuk át
Green.hideturtle()
Yellow.shape("circle")
Yellow.shapesize(3)
Yellow.fillcolor("orange")

Red.penup()
# Red pozícionálása oda, ahol a piros lámpának kell lennie
Red.forward(140)
Red.left(90)
Red.forward(190)
# Redet egy nagy piros körré alakítjuk át
Yellow.hideturtle()
Red.shape("circle")
Red.shapesize(3)
Red.fillcolor("red")

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
