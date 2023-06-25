"""
6. Ha nem tudod, hogyan történik a pontozás a teniszben, kérdezd meg egy barátodat, vagy nézd meg a Wikipédián.
Az egyszemélyes tenisz játszmákat (melyek A és B játékos között folynak) mindig pontra játsszák.
A játék állására gondoljunk állapotautomataként. A játék a (0, 0) állapotból indul, ami azt jelenti, hogy az egyik játékosnak sincs még pontja.
Feltételezzük, hogy az értékpár első tagja az A játékos pontszáma.
Ha az A játékos nyeri az első pontot, akkor az állás (15, 0), ha a B játékos nyeri, akkor (0, 15) lesz.
Az alábbi ábrán látható az első néhány állapot és állapotátmenet.
Az összes diagramon látható állapotban két lehetséges kimenet van (vagy A nyeri a következő pontot, vagy B).
A felső nyíl által jelzett átvitel mindig akkor lép életbe, ha az A játékos nyeri a pontot.
Egészítsd ki a diagramot úgy, hogy az összes állapot, és az összes állapotátmenet szerepeljen rajta.
(Segítség: összesen 20 állapot van, beleszámítva az előny állapotokat, a döntetlent és az „A nyert” és a „B nyert” állapot is.)
"""

allapot = (0, 0)
aElony = "Előny A-nál"
bElony = "Előny B-nél"

aGyoztes = "Ezt a gémet az A játékos nyerte"
bGyoztes = "Ezt a gémet az B játékos nyerte"


def allapot_automata_esemenykezeloje():
    global allapot
    jatszmaGyoztes = input("Ki nyerte a menetet: ")
    jatszmaGyoztes = jatszmaGyoztes.upper()
    if jatszmaGyoztes == "Q":
        return
    elif allapot == (0, 0):
        if jatszmaGyoztes == "A":
            allapot = (15, 0)
        else:
            allapot = (0, 15)
    elif allapot == (15, 0):
        if jatszmaGyoztes == "A":
            allapot = (30, 0)
        else:
            allapot = (15, 15)
    elif allapot == (30, 0):
        if jatszmaGyoztes == "A":
            allapot = (40, 0)
        else:
            allapot = (30, 15)
    elif allapot == (40, 0):
        if jatszmaGyoztes == "A":
            allapot = (0, 0)
            print(aGyoztes)
        else:
            allapot = (40, 15)
    elif allapot == (0, 15):
        if jatszmaGyoztes == "A":
            allapot = (15, 15)
        else:
            allapot = (0, 30)
    elif allapot == (0, 30):
        if jatszmaGyoztes == "A":
            allapot = (15, 30)
        else:
            allapot = (0, 40)
    elif allapot == (0, 40):
        if jatszmaGyoztes == "A":
            allapot = (15, 40)
        else:
            allapot = (0, 0)
            print(bGyoztes)
    elif allapot == (15, 15):
        if jatszmaGyoztes == "A":
            allapot = (30, 15)
        else:
            allapot = (15, 30)
    elif allapot == (30, 15):
        if jatszmaGyoztes == "A":
            allapot = (40, 15)
        else:
            allapot = (30, 30)
    elif allapot == (40, 15):
        if jatszmaGyoztes == "A":
            allapot = (0, 0)
            print(aGyoztes)
        else:
            allapot = (40, 30)
    elif allapot == (15, 30):
        if jatszmaGyoztes == "A":
            allapot = (30, 30)
        else:
            allapot = (15, 40)
    elif allapot == (15, 40):
        if jatszmaGyoztes == "A":
            allapot = (30, 40)
        else:
            allapot = (0, 0)
            print(bGyoztes)
    elif allapot == (30, 30):
        if jatszmaGyoztes == "A":
            allapot = (40, 30)
        else:
            allapot = (30, 40)
    elif allapot == (40, 30):
        if jatszmaGyoztes == "A":
            allapot = (0, 0)
            print(aGyoztes)
        else:
            allapot = (40, 40)
    elif allapot == (30, 40):
        if jatszmaGyoztes == "A":
            allapot = (40, 40)
        else:
            allapot = (0, 0)
            print(bGyoztes)
    elif allapot == (40, 40):
        if jatszmaGyoztes == "A":
            allapot = aElony
        else:
            allapot = bElony
    elif allapot == aElony:
        if jatszmaGyoztes == "A":
            allapot = (0, 0)
            print(aGyoztes)
        else:
            allapot = (40, 40)
    elif allapot == bElony:
        if jatszmaGyoztes == "A":
            allapot = (40, 40)
        else:
            allapot = (0, 0)
            print(bGyoztes)
    print("Állás: ", allapot)
    allapot_automata_esemenykezeloje()


allapot_automata_esemenykezeloje()
