import sys
import turtle
from turtle import Screen, Turtle


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


"""
1. Írj egy függvényt, ami megszámolja hány páratlan szám van egy listában!
"""


def countOdds(ints: list):
    return sum(i % 2 != 0 for i in ints)
    # result = 0
    # for i in ints:
    #     if i % 2 != 0:
    #         result += 1
    # return result


teszt(countOdds([1, 2, 3, 4, 5]) == 3)
teszt(countOdds([1, 2, -3, 44, -25, 5]) == 4)
teszt(countOdds([13]) == 1)
teszt(countOdds([2, 24]) == 0)

"""
2. Add össze az összes páros számot a listában!
"""


def sumEvens(ints: list):
    return sum(i for i in ints if i % 2 == 0)
    # result = 0
    # for i in ints:
    #     if i % 2 == 0:
    #         result += i
    # return result


teszt(sumEvens([1, 2, 3, 4, 5]) == 6)
teszt(sumEvens([1, 2, -44, -25, 5]) == -42)
teszt(sumEvens([1, -2, 44, -25, 5]) == 42)
teszt(sumEvens([13]) == 0)
teszt(sumEvens([2, 24]) == 26)

"""
3. Összegezd az összes negatív számot a listában!
"""


def sumNegatives(ints: list):
    return sum(i for i in ints if i < 0)
    # result = 0
    # for i in ints:
    #     if i < 0:
    #         result += i
    # return result


teszt(sumNegatives([1, 2, -44, -25, 5]) == -69)
teszt(sumNegatives([1, -2, 44, -25, -5]) == -32)
teszt(sumNegatives([13]) == 0)

"""
4. Számold meg hány darab 5 betűs szó van egy listában!
"""


def countFiveLettersWord(words: list):
    return sum(len(word) == 5 for word in words)
    # result = 0
    # for word in words:
    #     if len(word) == 5:
    #         result += 1
    # return result


teszt(countFiveLettersWord(['five', 'six', 'seven', 'hello']) == 2)
teszt(countFiveLettersWord(['five', 'six']) == 0)
teszt(countFiveLettersWord(['one', 'two', 'three', 'five', 'six']) == 1)

"""
5. Összegezd egy lista első páros száma előtti számokat! (Írd meg az egységtesztedet! Mi van, ha nincs egyáltalán páros szám?)
"""


def sumAllBeforeFirstEven(ints: list):
    result = 0
    for i in ints:
        if i % 2 == 0:
            return result
        result += i
    return result


teszt(sumAllBeforeFirstEven([1, 2, -44, -25, 5]) == 1)
teszt(sumAllBeforeFirstEven([1, 15, 3, -44, -25, 5]) == 19)
teszt(sumAllBeforeFirstEven([-1, 15, 4, -25, 5]) == 14)
teszt(sumAllBeforeFirstEven([-1, -15, 4, -25, 5]) == -16)
teszt(sumAllBeforeFirstEven([4, -25, 5]) == 0)

"""
6. Számold meg, hány szó szerepel egy listában az első „nem” szóig (beleértve magát a „nem” szót is! (Írd meg itt is az egységtesztedet! Mi van, ha a „nem” szó egyszer sem jelenik meg a listában?)
"""


def countWordsBeforeNo(words: list):
    sum: int = 0
    for word in words:
        sum += 1
        if word == "no":
            return sum
    return sum


teszt(countWordsBeforeNo(["hello", "no", "hola", "yes"]) == 2)
teszt(countWordsBeforeNo(["no", "hola", "yes"]) == 1)
teszt(countWordsBeforeNo(["hello", "hola", "yes"]) == 3)
teszt(countWordsBeforeNo(["hello", "hola", "yes", "no"]) == 4)

"""
7. Adj egy print függvényt a Newton-féle gyok függvényhez, amely kiíratja a jobb változó értékét minden cikluslépésben! Hívd meg a módosított függvényt a 25 aktuális paraméterrel, és jegyezd fel az eredményt!
"""


def gyok(n: int):
    kozelites: float = n / 2.0  # Kezdjük egy alap sejtéssel
    while True:
        jobb: float = (kozelites + n / kozelites) / 2.0
        print(jobb)
        if abs(kozelites - jobb) < 0.001:
            return jobb
        kozelites = jobb


print(gyok(25))

"""
8. Kövesd nyomon a szorzotabla_kiiras függvény legutóbbi változatát és találd ki, hogyan működik!
"""


def tobbszorosok_kiirasa(n: int, magassag: int):
    for i in range(1, magassag):
        print(n * i, end="   ")
    print()


def szorzotabla_kiiras(magassag: int):
    for i in range(1, magassag + 1):
        tobbszorosok_kiirasa(i, i + 1)


szorzotabla_kiiras(5)

"""
9. Írj egy haromszogszamok nevű függvényt, amely kiírja az első n darab háromszögszámot! A haromszogszamok(5) hívás ezt a kimenetet eredményezi:
"""


def printTriangularNumbers(n: int):
    sum: int = 0
    for i in range(1, n + 1):
        sum += i
        print(i, "   ", sum)


printTriangularNumbers(5)

"""
10. Írj egy prim_e függvényt, amely kap egy egészet paraméterként és True értéket ad vissza, ha a paramétere egy prímszám és False értéket különben! Adj hozzá ilyen teszteket:
"""


def prim_e(number):
    if number == 1 or number == 2:
        return True
    for i in range(2, number + 1 // 2):
        if number % i == 0:
            return False
    return True


teszt(prim_e(11))
teszt(not prim_e(35))
teszt(not prim_e(19730421))

"""
11. Emlékezz a részeg kalóz problémára a 3. fejezet feladataiból! Most a részeg kalóz tesz egy fordulatot és pár lépést előre, majd ezt ismételgeti. A bölcsészhallgatónk feljegyzi a mozgás adatpárjait: az elfordulás szöge és az ezt követő lépések száma. A kísérleti adatai ezek: [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Használj egy teknőcöt a pityókás barátunk útvonalának megjelenítéséhez!
"""

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)

movingDatas = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (distance, angle) in movingDatas:
    drawer.forward(distance)
    drawer.left(angle)

ablak.clear()

"""
12. Sok érdekes alakzat kirajzolható a teknőcökkel, ha a fentihez hasonló adatpárokat adunk nekik, ahol az első érték egy szög a második pedig egy távolság. Készítsd el az értékpár listát, és rajzoltasd ki a teknőccel a 12.png kñpen bemutatott házat! Ez elkészíthető anélkül, hogy egyszer is felemelnénk a tollat vagy egy vonalat duplán rajzolnánk.
"""

ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)

tess_house = [(50, 90), (50, 30), (50, 120), (50, 30), (50, 135), (5000 ** 0.5, 135), (50, 135), (5000 ** 0.5, 45)]
for (distance, angle) in tess_house:
    drawer.forward(distance)
    drawer.left(angle)

ablak.mainloop()
