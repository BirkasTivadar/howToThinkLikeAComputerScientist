"""
2. Módosítsd a királynő programot 4, 12 és 16-os méretű sakktáblák megoldására.
Mekkora a legnagyobb méretű sakktábla, melyet az algoritmus egy perc alatt meg tud oldani?
"""


def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)  # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)  # Kiszámoljuk x távolságának abszolút értékét
    return dx == dy  # Ütköznek, ha dx == dy


def oszlop_utkozes(bs, c):
    """ True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik a tőle balra levőkkel. """
    for i in range(c):  # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False  # Nincs ütközés, a c oszlopban biztonságos helyen van


def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for oszlop in range(1, len(sakktabla)):
        if oszlop_utkozes(sakktabla, oszlop):
            return True
    return False


# 4-es sakktábla
def mainNegyes():
    import random
    rng = random.Random()  # A generátor létrehozása
    bd = list(range(4))  # Generálja a kezdeti permutációt
    proba = 0
    while True:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
            return


mainNegyes()


# 12-es sakktábla
def mainTizenkettes():
    import random
    rng = random.Random()  # A generátor létrehozása
    bd = list(range(12))  # Generálja a kezdeti permutációt
    proba = 0
    while True:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
            return


mainTizenkettes()


# 16-os sakktábla
def mainTizenhatos():
    import random
    rng = random.Random()  # A generátor létrehozása
    bd = list(range(16))  # Generálja a kezdeti permutációt
    proba = 0
    while True:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
            return


mainTizenhatos()
