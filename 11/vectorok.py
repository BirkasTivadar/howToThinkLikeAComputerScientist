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
