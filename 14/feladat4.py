"""
4. A sakktáblák szimmetrikusak: ha megoldást keresünk a királynő problémára, akkor a tükörképe is megoldás lesz
– vagy az x vagy az y tengely szerinti tükrözés, szintén megoldás.
A tábla 90, 180 vagy 270 fokos forgatása szintén megoldása lesz.
Bizonyos értelemben olyan megoldások, amelyek tükörképei vagy forgatásai a megoldásoknak
– ugyanabban a családban – kevésbé érdekesek, mint az egyedi „alapvető esetek”.
A 8 királynő probléma 92 megoldásából csak 12 egyedi család létezik, ha figyelembe vesszük a forgatásokat és a tükrözéseket.
A Wikipédián néhány lenyűgöző dolgot találhatunk ezzel kapcsolatosan.
"""

"""
a. Írj egy függvényt, amely egy megoldást tükröz az Y tengelyre.
"""
from egyseg_teszt import *


def yTukrozes(alapFelallas: list):
    tukrozott: list = []
    for i in range(-1, -len(alapFelallas) - 1, -1):
        tukrozott.append(alapFelallas[i])
    return tukrozott


teszt(yTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [3, 1, 6, 2, 5, 7, 4, 0])
teszt(not yTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [0, 6, 4, 7, 1, 3, 5, 2])
teszt(yTukrozes([7, 3, 0, 2, 5, 1, 6, 4]) == [4, 6, 1, 5, 2, 0, 3, 7])

"""
b. Írj egy függvényt, amely egy megoldást tükröz az X tengelyre.
"""


def xTukrozes(alapFelallas: list):
    tukrozott: list = []
    for number in alapFelallas:
        tukrozott.append(7 - number)
    return tukrozott


teszt(xTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [7, 3, 0, 2, 5, 1, 6, 4])
teszt(not xTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [2, 5, 3, 1, 7, 4, 6, 0])
teszt(xTukrozes([5, 2, 4, 6, 0, 3, 1, 7]) == [2, 5, 3, 1, 7, 4, 6, 0])

"""
c. Írj egy függvényt, amely a megoldást elforgatja 90 fokkal az óra járásának ellentétesen, 
és használja a 180 és 270 fokos forgatásokat is.
"""


def elforgatasBalra(alapFelallas: list):
    tukrozott: list = [0, 0, 0, 0, 0, 0, 0, 0]
    for number in alapFelallas:
        tukrozott[number] = 7 - alapFelallas.index(number)
    return tukrozott


teszt(elforgatasBalra([0, 4, 7, 5, 2, 6, 1, 3]) == [7, 1, 3, 0, 6, 4, 2, 5])
teszt(not elforgatasBalra([0, 4, 7, 5, 2, 6, 1, 3]) == [2, 5, 3, 1, 7, 4, 6, 0])


def elforgatasJobbra(alapFelallas: list):
    tukrozott: list = [0, 0, 0, 0, 0, 0, 0, 0]
    for number in alapFelallas:
        tukrozott[7 - number] = alapFelallas.index(number)
    return tukrozott


teszt(elforgatasJobbra([0, 4, 7, 5, 2, 6, 1, 3]) == [2, 5, 3, 1, 7, 4, 6, 0])
teszt(not elforgatasJobbra([0, 4, 7, 5, 2, 6, 1, 3]) == [7, 1, 3, 0, 6, 4, 2, 5])
