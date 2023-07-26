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


def yTukrozes(megoldas: list):
    tukrozott = []
    for i in range(-1, -len(megoldas) - 1, -1):
        tukrozott.append(megoldas[i])
    return tukrozott


teszt(yTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [3, 1, 6, 2, 5, 7, 4, 0])
teszt(not yTukrozes([0, 4, 7, 5, 2, 6, 1, 3]) == [0, 6, 4, 7, 1, 3, 5, 2])
teszt(yTukrozes([7, 3, 0, 2, 5, 1, 6, 4]) == [4, 6, 1, 5, 2, 0, 3, 7])


"""
b. Írj egy függvényt, amely egy megoldást tükröz az X tengelyre.
"""

def