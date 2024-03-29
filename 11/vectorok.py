"""
5. A listákat használhatjuk matematikai vektorok ábrázolására.
Ebben és az ezt követő néhány gyakorlatban olyan függvényeket írunk le, amelyek végrehajtják a vektorok alapvető műveleteit.
Hozz létre egy vectorok.py szkriptet, és írd bele az alábbi Python kódot, hogy mindegyiket letesztelhesd!

Írj egy vektorok_osszege(u, v) függvényt, amely paraméterként két azonos hosszúságú listát kap, és adjon vissza egy új listát, mely tartalmazza a megfelelő elemek összegét:
"""

from egyseg_teszt import *


def vektorok_osszege(vektor1: list, vektor2: list):
    eredmeny: list = []
    for i in range(len(vektor1)):
        eredmeny.append(vektor1[i] + vektor2[i])
    return eredmeny


teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

"""
6. Írj egy szorzas_skalarral(s, v) függvényt, amely paraméterként egy s számot, és egy v listát kap, és visszatér a függvény a v lista s skalárral való szorzatával.
"""


def szorzas_skalarral(szam: int, vektor: list):
    eredmeny: list = []
    for elem in vektor:
        eredmeny.append(szam * elem)
    return eredmeny


teszt(szorzas_skalarral(5, [1, 2]) == [5, 10])
teszt(szorzas_skalarral(3, [1, 0, -1]) == [3, 0, -3])
teszt(szorzas_skalarral(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

"""
7. Írj egy skalaris_szorzat(u, v) függvényt, amely paraméterként megkap két azonos hosszúságú számokat tartalmazó listát, és visszaadja a megfelelő elemek skaláris szorzatát.
"""


def skalaris_szorzat(vektor1: list, vektor2: list):
    eredmeny: int = 0
    for i in range(len(vektor1)):
        eredmeny += vektor1[i] * vektor2[i]
    return eredmeny


teszt(skalaris_szorzat([1, 1], [1, 1]) == 2)
teszt(skalaris_szorzat([1, 2], [1, 4]) == 9)
teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)

"""
8. Extra matematikai kihívások: Írj egy vektorialis_szorzat(u, v) függvényt, 
amely paraméterként megkap két 3 hosszúságú számokból álló listát, 
és visszatér a vektoriális szorzatukkal. 
Írd meg a saját tesztjeid!
c1 = a2*b3 - a3*b2
c2 = a3*b1 - a1*b3
c3 = a1*b2 - a2*b1
"""


def vektorialis_szorzat(vektor1: list, vektor2: list):
    c1 = vektor1[1] * vektor2[2] - vektor1[2] * vektor2[1]
    c2 = vektor1[2] * vektor2[0] - vektor1[0] * vektor2[2]
    c3 = vektor1[0] * vektor2[1] - vektor1[1] * vektor2[0]
    return [c1, c2, c3]


teszt(vektorialis_szorzat([2, 2, 2], [3, 3, 3]) == [0, 0, 0])
teszt(vektorialis_szorzat([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
teszt(vektorialis_szorzat([0, 2, -5], [-1, 3, -8]) == [-1, 5, 2])

"""
9. Írd le a " ".join(nota.split()) és nota közötti kapcsolatot az alábbi kódrészletben. 

nota = "Esik eső, szép csendesen csepereg..."

Ugyanazok a sztringek vannak hozzárendelve a nota-hoz? 
Igen, ugyanazok.

Mikor lennének különbözőek?

Ha a 

" ".join(nota.split()

helyett a 

" ".join("Esik eső, szép csendesen csepereg...".split()

kifejezést használnák
"""

"""
10. Írj egy cserel(s, regi, uj) függvényt, 
amely kicseréli a regi összes előfordulását a uj-ra az s szrtingben.
Tipp: Használd a split és join metódusokat.
"""


def cserel(szoveg, regi, uj):
    return uj.join(szoveg.split(regi))


teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")

s = "Kerek a gömb, gömbszerű!"
teszt(cserel(s, "öm", "om") ==
      "Kerek a gomb, gombszerű!")

teszt(cserel(s, "o", "ö") ==
      "Kerek a gömb, gömbszerű!")

"""
Tegyük fel, hogy két változó értékét akarjuk felcserélni. 
Újra felhasználható függvényt hozz létre, írd bele az alábbi kódot:


def csere(x, y):      # Hibás változat
    print("csere utasítás előtt: x:", x, "y:", y)
    (x, y) = (y, x)
    print("csere utasítás után: x:", x, "y:", y)

a = ["Ez", "nagyon", "érdekes"]
b = [2,3,4]
print("csere függvény hívása előtt: a:", a, "b:", b)
csere(a, b)
print("csere függvény hívása után: a:", a, "b:", b)
Futtasd a fenti programot, és írd le az eredményeket. 
Hoppá! Nem azt tette, amit szerettünk volna! Magyarázd el miért nem. 

Mert csak a listák referenciáit cseréli fel, és ez a csere csak a függvény törzsén belül érvényes.

Használd a Python megjelenítőt, amely segítségével építs egy működő koncepcionális modellt! 
Mi lesz az a és b értéke a csere függvény hívása után?
"""


# def csere(x, y):  # Hibás változat
#     print("csere utasítás előtt: x:", x, "y:", y)
#     (x, y) = (y, x)
#     print("csere utasítás után: x:", x, "y:", y)
#
# a = ["Ez", "nagyon", "érdekes"]
# b = [2, 3, 4]
# print("csere függvény hívása előtt: a:", a, "b:", b)
# csere(a, b)
# print("csere függvény hívása után: a:", a, "b:", b)

def csere(x, y):  # jó változat:
    print("csere utasítás előtt: x:", x, "y:", y)
    for i in range(len(a)):
        x[i], y[i] = y[i], x[i]
    print("csere utasítás után: x:", x, "y:", y)
    return x, y


a = ["Ez", "nagyon", "érdekes"]
b = [2, 3, 4]
print("csere függvény hívása előtt: a:", a, "b:", b)
csere(a, b)
print("csere függvény hívása után: a:", a, "b:", b)
