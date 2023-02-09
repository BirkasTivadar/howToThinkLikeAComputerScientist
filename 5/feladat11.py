"""
Írj egy derekszogu_e függvényt, amely megkapja egy háromszög három oldalának a hosszát és meghatározza, hogy derékszögű háromszögről van-e szó! Tételezzük fel, hogy a harmadik megadott oldal mindig a leghosszabb. A függvény True értékkel térjen vissza, ha a háromszög derékszögű, False értékkel különben!
Segítség: A lebegőpontos aritmetika (azaz a valós számok használata) nem mindig pontos, így nem biztonságos a valós számok egyenlőségével való tesztelés. Ha a jó programozó azt akarja tudni, hogy x értéke egyenlő-e vagy nagyon közeli-e y értékéhez, valószínűleg ezt a kódot írják:
if  abs(x-y) < 0.000001:    # Ha x megközelítően egyenlő y-nal
    ...
"""
import math


def atfogo(befogo_egy: float, befogo_ketto: float):
    return math.sqrt(befogo_egy ** 2 + befogo_ketto ** 2)


def derekszogu_e(a: float, b: float, c: float):
    return abs(c - atfogo(a, b)) < 0.0000001


print(derekszogu_e(3, 4, 5))
print(derekszogu_e(4, 4, 5))
print(derekszogu_e(12, 5, 13))
