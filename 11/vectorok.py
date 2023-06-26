"""
5. A listákat használhatjuk matematikai vektorok ábrázolására.
Ebben és az ezt követő néhány gyakorlatban olyan függvényeket írunk le, amelyek végrehajtják a vektorok alapvető műveleteit.
Hozz létre egy vectorok.py szkriptet, és írd bele az alábbi Python kódot, hogy mindegyiket letesztelhesd!

Írj egy vektorok_osszege(u, v) függvényt, amely paraméterként két azonos hosszúságú listát kap, és adjon vissza egy új listát, mely tartalmazza a megfelelő elemek összegét:
"""

from test import *


def vektorok_osszege(vector1: list, vector2: list):
    eredmeny: list = []
    for i in range(len(vector1)):
        eredmeny.append(vector1[i] + vector2[i])
    return eredmeny


teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

"""
6. Írj egy szorzas_skalarral(s, v) függvényt, amely paraméterként egy s számot, és egy v listát kap, és visszatér a függvény a v lista s skalárral való szorzatával.
"""


def szorzas_skalarral(szam: int, vector: list):
    eredmeny: list = []
    for elem in vector:
        eredmeny.append(szam * elem)
    return eredmeny


teszt(szorzas_skalarral(5, [1, 2]) == [5, 10])
teszt(szorzas_skalarral(3, [1, 0, -1]) == [3, 0, -3])
teszt(szorzas_skalarral(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])


"""
7. Írj egy skalaris_szorzat(u, v) függvényt, amely paraméterként megkap két azonos hosszúságú számokat tartalmazó listát, és visszaadja a megfelelő elemek skaláris szorzatát.
"""


def skalaris_szorzat(vector1: list, vector2: list):
    eredmeny: int = 0
    for i in range(len(vector1)):
        eredmeny += vector1[i] * vector2[i]
    return eredmeny


teszt(skalaris_szorzat([1, 1], [1, 1]) == 2)
teszt(skalaris_szorzat([1, 2], [1, 4]) == 9)
teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)
