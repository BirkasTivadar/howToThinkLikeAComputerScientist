"""
2. Módosítsd a királynő programot 4, 12 és 16-os méretű sakktáblák megoldására.
Mekkora a legnagyobb méretű sakktábla, melyet az algoritmus egy perc alatt meg tud oldani?
"""

from kiralyno import *


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


# Időméréses
def mainIdomereses():
    i = 4
    while True:
        bd = list(range(i))  # Generálja a kezdeti permutációt
        vege = megoldasKereses(bd)
        i += 1
        if vege:
            return


def megoldasKereses(bd):
    import time
    import random
    rng = random.Random()
    start = time.time()
    proba = 0
    while True:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
            return False
        if time.time() - start > 60:
            print("Nincs megoldás egy perc alatt {0} méretű sakktáblára".format(len(bd)))
            return True


mainIdomereses()
