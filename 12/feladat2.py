"""
Nyisd meg a math modul dokumentációját.

Hány függvényt tartalmaz a math modul?
"""
# Jelenleg 55-öt (11.4)

"""
Mit csinál a math.ceil? 
Mit a math.floor? 
(Tipp: mindkettő a floor és a ceil valós értéket vár argumentumként.)
"""
import math

print(math.ceil(2.16))
print(math.ceil(-5.16))
# A math.ceil() az argumentumként átadott valós számot felfelé kerekíti függetlenül a tizedes pont utáni értéktől

print(math.floor(5.96))
print(math.floor(-2.16))
# A math.floor() az argumentumként átadott valós számot lefelé kerekíti függetlenül a tizedes pont utáni értéktől

"""
Írd le, hogyan számoltuk ki ugyanazt az értéket, mint a math.sqrt, a math modul használata nélkül.
"""
print(math.sqrt(25) == 25 ** 0.5)

"""
Mi a math modul két adat konstansa?
"""
# Jelenleg már három van:
#                         math.pi
#                         math.e
#                         math.tau