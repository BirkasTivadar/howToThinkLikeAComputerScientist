"""
8.19. Feladatok
Javasoljuk, hogy egy fájlban készítsd el az alábbi feladatokat, az előző feladatokban látott tesztelő függvényeket is bemásolva a fájlba.
"""

from test import *

"""
1. Milyen eredményt adnak az alábbi kifejezések? (Ellenőrizd a válaszaid a print függvény segítségével.)

"Python"[1]
"A sztringek karaktersorozatok."[5]
len("csodálatos")
"Rejtély"[:4]
"k" in "Körte"
"barack" in "sárgabarack"
"körte" not in "Ananász"
"barack" > "sárgabarack"
"ananász" < "Barack"
"""

teszt("Python"[1] == "y")
teszt("A sztringek karaktersorozatok."[5] == "r")
teszt(len("csodálatos") == 10)
teszt("Rejtély"[:4] == "Rejt")
teszt(("k" in "Körte") == False)
teszt(("barack" in "sárgabarack") == True)
teszt(("körte" not in "Ananász") == True)
teszt(("barack" > "sárgabarack") == False)
teszt(("ananász" < "Barack") == False)

"""
2. Javítsd ki úgy az alábbi programot, hogy Törpapa és Törpicur neve is helyesen jelenjenek meg:

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    print(elotag + utotag)
"""

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    if (utotag[0] == "p"):
        utotag = utotag[1:]
    print(elotag + utotag)

"""
3. Ágyazd be az alábbi kódrészletet egy karakter_szamlalas nevű függvénybe, majd általánosítsd úgy, hogy a sztringet és a számlálandó karaktert is paraméterként várja. A függvény adja vissza a karakter sztringbeli előfordulásainak számát, ne írassa ki. Az érték megjelenítése a függvény hívójának feladata.

gyumolcs = "banán"
darab = 0
for karakter in gyumolcs:
    if karakter == "a":
        darab += 1
print(darab)
"""


def karakter_szamlalas(szoveg: str, betu: str):
    darab = 0
    for karakter in szoveg:
        if karakter == betu:
            darab += 1
    return darab


teszt(karakter_szamlalas("Hello World", "l") == 3)
teszt(karakter_szamlalas("Hello World", "j") == 0)

"""
4. Most írd át úgy a karakter_szamlalas függvényt, hogy a sztring bejárása helyett a beépített find metódusát hívja meg újra és újra. A második paraméternek átadott értékkel biztosíthatod, hogy a metódus mindig új előfordulását találja meg a számlálandó karakternek.
"""


def karakter_szamlalas_find(szoveg: str, betu: str):
    darab = 0
    index = szoveg.find(betu)
    while index != -1:
        darab += 1
        szoveg = szoveg[index + 1:]
        index = szoveg.find(betu)
    return darab


teszt(karakter_szamlalas_find("Hello Worll", "l") == 4)
teszt(karakter_szamlalas_find("Hello World", "j") == 0)
