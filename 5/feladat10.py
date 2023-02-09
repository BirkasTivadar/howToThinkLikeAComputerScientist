# 10. Írj egy atfogo függvényt, amely megkapja egy derékszögű háromszög két befogójának a hosszát és visszaadja az átfogó hosszát! (Segítség: az x ** 0.5 a négyzetgyököt adja vissza.)

import math


def atfogo(befogo_egy: float, befogo_ketto: float):
    return math.sqrt(befogo_egy ** 2 + befogo_ketto ** 2)


print(atfogo(3, 4.0))
