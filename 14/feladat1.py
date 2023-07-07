"""
1. Ez a rész az Alice Csodaországban, ismét! fejezetről szól, azzal az észrevétellel kezdődött,
hogy az összefésüléses algoritmus egy olyan mintát használ, melyet más helyzetben újra használhatunk.
Módosítsd az összefésülés algoritmusát, és írd meg az alábbi függvényeket, ahogyan itt javasoljuk:
"""
from egyseg_teszt import *

list1 = ["alma", "banán", "barack", "dió", "körte", "narancs", "szilva"]
list2 = ["alma", "banán", "citrom", "dió", "egres", "körte", "naspolya", "szilva"]
list1.sort()
list2.sort()


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

        if yi >= len(ys):  # Ha az ys lista végére értünk
            return eredmeny  # Készen vagyunk

        # Ha mindkét listában vannak még elemek
        if xs[xi] == ys[yi]:  # Ha az elem mindkét listában megvan
            eredmeny.append(xs[xi])  # Bemásoljuk az eredmény listába
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:  # Ha az elem az xs listában van meg csak
            xi += 1  # Továáblépünk
        elif ys[yi] < xs[xi]:  # Ha az elem az ys listában van meg csak
            yi += 1  # Továáblépünk


teszt(mindketListaban(list1, list2) == ['alma', 'banán', 'dió', 'körte', 'szilva'])


# b. Csak azokat az elemeket adja vissza, melyek benne vannak az első listában, de nincsenek benne a másodikban.
def elsoListabanCsak(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat. Visszatér azokkal az elemekkel,
    amelyek benne vannak az első listában, de nincsenek benne a másodikban.
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # Ha az xs lista végére értünk
            return eredmeny  # Készen vagyunk

        if yi >= len(ys):  # Ha az ys lista végére értünk
            eredmeny.extend(xs[xi:])  # A maradék xs-t hozzámásoljuk az eredményhez
            return eredmeny  # Készen vagyunk

        # Ha mindkét listában vannak még elemek
        if xs[xi] == ys[yi]:  # Ha az elem mindkét listában benne van
            xi += 1  # Továbblépünk
            yi += 1
        elif xs[xi] < ys[yi]:  # Ha az elem csak az xs listában van csak meg
            eredmeny.append(xs[xi])  # Bemásoljuk az eredmény listába
            xi += 1
        elif ys[yi] < xs[xi]:  # Ha az elem a ys listában van csak meg
            yi += 1


teszt(elsoListabanCsak(list1, list2) == ["barack", "narancs"])
teszt(elsoListabanCsak(list2, list1) == ["citrom", "egres", "naspolya"])


# c. Csak azokat az elemeket adja vissza, melyek benne vannak a második listában, de nincsenek az elsőben.
def masodikListabanCsak(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat. Visszatér azokkal az elemekkel,
    amelyek benne vannak a második listában, de nincsenek benne az elsőben.
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # Ha az xs lista végére értünk
            eredmeny.extend(ys[yi:])  # A maradék ys-t hozzámásoljuk az eredményhez
            return eredmeny  # Készen vagyunk

        if yi >= len(ys):  # Ha az ys lista végére értünk
            return eredmeny  # Készen vagyunk

        # Ha mindkét listában vannak még elemek
        if xs[xi] == ys[yi]:  # Ha az elem mindkét listában benne van
            xi += 1  # Továbblépünk
            yi += 1
        elif xs[xi] < ys[yi]:  # Ha az elem csak az xs listában van csak meg
            xi += 1
        elif ys[yi] < xs[xi]:  # ha az elem a ys listában van csak meg
            eredmeny.append(ys[yi])  # Bemásoljuk az eredmény listába
            yi += 1


teszt(masodikListabanCsak(list1, list2) == ["citrom", "egres", "naspolya"])
teszt(masodikListabanCsak(list2, list1) == ["barack", "narancs"])


# d. Csak azokat az elemeket adja vissza, melyek vagy az elsőben vagy a másodikban vannak benne.
def egyikListabanCsak(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat. Visszatér azokkal az elemekkel,
    amelyek vagy az elsőben vagy a másodikban vannak csak benne.
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # Ha az xs lista végére értünk
            eredmeny.extend(ys[yi:])  # A maradék ys-t hozzámásoljuk az eredményhez
            return eredmeny  # Készen vagyunk

        if yi >= len(ys):  # Ha az ys lista végére értünk
            eredmeny.extend(xs[xi:])  # A maradék xs-t hozzámásoljuk az eredményhez
            return eredmeny  # Készen vagyunk

        # Ha mindkét listában vannak még elemek
        if xs[xi] == ys[yi]:  # Ha az elem mindkét listában benne van
            xi += 1  # Továbblépünk
            yi += 1
        elif xs[xi] < ys[yi]:  # Ha az elem csak az xs listában van csak meg
            eredmeny.append(xs[xi])  # Bemásoljuk az eredmény listába
            xi += 1
        elif ys[yi] < xs[xi]:  # ha az elem a ys listában van csak meg
            eredmeny.append(ys[yi])  # Bemásoljuk az eredmény listába
            yi += 1


teszt(egyikListabanCsak(list1, list2) == ["barack", "citrom", "egres", "narancs", "naspolya"])
