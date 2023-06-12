"""
1. Nem mondtunk semmit ebben a fejezetben arról, hogy vajon a rendezett n-esek átadhatóak-e függvénynek paraméterként.
Hozz létre egy kis Python példakódot ennek kiderítésére!
"""


def printName(nev: tuple):
    """
    Tuple-ban megkapja a nevet, és külön sorba kiírja a családi, majd a keszetnevet
    :param nev: két sztringből álló tuple
    :return: None
    """
    csaladiNev, keresztNev = nev
    print(csaladiNev)
    print(keresztNev)


humorista = ("Hofi", "Géza")
iro = ("Moldova", "György")

printName(humorista)
printName(iro)
