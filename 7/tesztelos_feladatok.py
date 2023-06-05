from test import *

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
14. Mit fog a szamjegy_szam(0) függvényhívás visszaadni? Módosítsd, hogy 1-et adjon vissza ebben az esetben! Miért okoz a szamjegy_szam(-24) hívás végtelen ciklust? (Segítség: -1//10 eredménye -1) Módosítsd a szamjegy_szam függvényt, hogy jól működjön bármely egész szám esetén! Add hozzá ezeket a teszteket:
"""


def szamjegy_szam(n):
    if n == 0:
        return 1
    szamlalo = 0
    n = abs(n)
    while n != 0:
        szamlalo += 1
        n = n // 10
    return szamlalo


teszt(szamjegy_szam(0) == 1)
teszt(szamjegy_szam(4) == 1)
teszt(szamjegy_szam(-12345) == 5)

"""
15. Írj egy paros_szamjegy_szam(n) függvényt, amely megszámolja a páros számjegyeket az n számban. Ezeken a teszteken át kell mennie:
"""


def paros_szamjegy_szam(n):
    if n == 0:
        return 1
    szamlalo = 0
    n = abs(n)
    while n != 0:
        if n % 2 == 0:
            szamlalo += 1
        n = n // 10
    return szamlalo


teszt(paros_szamjegy_szam(123456) == 3)
teszt(paros_szamjegy_szam(2468) == 4)
teszt(paros_szamjegy_szam(1357) == 0)
teszt(paros_szamjegy_szam(0) == 1)

"""
16. Írj egy negyzetosszeg(xs) függvényt, amely visszaadja a paraméterként kapott listában szereplő számok négyzetének összegét! Például a negyzetosszeg([2, 3, 4]) hívás eredménye 4+9+16, azaz 29 kell legyen.
"""


def negyzetosszeg(xs: list):
    return sum(x ** 2 for x in xs)


teszt(negyzetosszeg([2, 3, 4]) == 29)
teszt(negyzetosszeg([]) == 0)
teszt(negyzetosszeg([2, -3, 4]) == 29)
