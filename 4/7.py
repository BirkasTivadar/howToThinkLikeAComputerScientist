# 7. Készíts egy osszeg(n) fejlécű produktív függvényt , amely összegzi az 1 és n közé eső egész számokat, a határokat is beleértve. Például osszeg(10) hívás esetében az 1+2+3…+10 eredményét, vagyis 55-öt kell visszaadni a függvénynek.

def osszeg(n: int):
    sum: int = 0
    for i in range(n + 1):
        sum += i
    return sum


print(osszeg(10))
