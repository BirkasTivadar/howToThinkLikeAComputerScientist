"""
1. Ez a rész az Alice Csodaországban, ismét! fejezetről szól, azzal az észrevétellel kezdődött,
hogy az összefésüléses algoritmus egy olyan mintát használ, melyet más helyzetben újra használhatunk.
Módosítsd az összefésülés algoritmusát, és írd meg az alábbi függvényeket, ahogyan itt javasoljuk:
"""
from egyseg_teszt import *


# a. Csak azokat az elemeket adja vissza, melyek mindkét listába benne vannak.

def mindketListaban(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat. Visszatér azokkal az elemekkel,
    amelyek mindkét listában benne vannak.
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # Ha az xs lista végére értünk
            return eredmeny  # Készen vagyunk

        if yi >= len(ys):  # Ugyanaz, csak fordítva
            return eredmeny

        # Ha mindkét listában vannak még elemek, akkor a kisebbik elemet másoljuk az eredmény listába
        if xs[xi] == ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        elif ys[yi] < xs[xi]:
            yi += 1


list1 = ["alma", "banán", "barack", "dió", "körte", "narancs", "szilva"]
list2 = ["alma", "banán", "citrom", "dió", "egres", "körte", "naspolya", "szilva"]
list1.sort()
list2.sort()

teszt(mindketListaban(list1, list2) == ['alma', 'banán', 'dió', 'körte', 'szilva'])
