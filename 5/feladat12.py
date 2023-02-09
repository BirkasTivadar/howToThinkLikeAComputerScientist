# 12. Egészítsd ki a 11. feladatot úgy, hogy tetszőleges sorrendű adatok megadása esetén is működjön!

import math


def atfogo(befogo_egy: float, befogo_ketto: float):
    return math.sqrt(befogo_egy ** 2 + befogo_ketto ** 2)


def derekszogu_e(a: float, b: float, c: float):
    return abs(c - atfogo(a, b)) < 0.0000001


def derekszogu_e_alt(a: float, b: float, c: float):
    atfogo = max(a, b, c)
    if atfogo == a:
        return derekszogu_e(b, c, a)
    elif atfogo == b:
        return derekszogu_e(c, a, b)
    else:
        return derekszogu_e(a, b, c)


print(derekszogu_e_alt(5, 3, 4))
print(derekszogu_e_alt(4, 4, 4))
print(derekszogu_e_alt(5, 13, 12))
