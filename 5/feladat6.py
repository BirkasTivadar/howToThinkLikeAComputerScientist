"""
6. Írj egy függvényt, amely kap egy vizsgapontszámot és visszaadja az érdemjegyed nevét – az alábbi séma szerint:

Pont	Jegy
>= 90	jeles
[80-90)	jó
[70-80)	közepes
[60-70)	elégséges
< 60	elégtelen

A szögletes- és kerek zárójelek zárt és nyílt intervallumot jelölnek. A zárt intervallum tartalmazza a számot, a nyílt nem. Így az 59.99999 elégtelent jelent, de a 60.0 már elégséges.

Teszteld a függvényed azzal, hogy kiíratod az összes jegyet az alábbi sorozat elemei (pontszámai) esetén:

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
"""


def erdemjegy(pontszam: float):
    if (pontszam >= 90):
        return 'jeles'
    elif (pontszam >= 80):
        return 'jó'
    elif (pontszam >= 70):
        return 'közepes'
    elif (pontszam >= 60):
        return 'elégséges'
    else:
        return 'elégtelen'

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for pontszam in xs:
    print(erdemjegy(pontszam))