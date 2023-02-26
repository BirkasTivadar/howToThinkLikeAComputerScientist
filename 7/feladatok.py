import sys


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
