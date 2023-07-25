"""
3. Módosítsd a királynő programot,
hogy megtartsd a megoldások listáját, azért,
hogy ugyanazt a megoldást csak egyszer írja ki.
"""

from kiralyno import *


def main():
    import random
    rng = random.Random()  # A generátor létrehozása

    bd = list(range(8))  # Generálja a kezdeti permutációt
    talalatok = []
    talalat_szama = 0
    proba = 0
    while talalat_szama < 10:
        bdKevert = rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            if bd not in talalatok:
                talalatok.append(bdKevert)
                print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
                proba = 0
                talalat_szama += 1


main()
