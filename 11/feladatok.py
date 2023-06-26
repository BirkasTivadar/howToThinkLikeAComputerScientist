"""
1. Mi lesz a Python kód eredménye a következő utasítás esetén?

list(range(10, 0, -2))
[10,8,6,4,2]

A range függvény három argumentuma a start, stop és step.
Ebben a példában a start nagyobb, mint a stop.
Mi történik, ha a start < stop és a step < 0?
üres listát kapunk

Írj egy szabályt a start, a stop és a step közötti kapcsolatokra.
 1. Ha start < stop és step > 0 a lista tartalmazza start-tól a step-el növekvő számokat stop-ig
 2. Ha start > stop és step > 0 a lista tartalmazza start-tól a step-el csökkenő számokat stop-ig
 3. Egyéb esetekben üres listát kapunk.
"""

"""
2. Tekintsük a következő kódrészletet:

import turtle

Eszti = turtle.Turtle()
Sanyi = Eszti
Sanyi.color("hotpink")

Ez a kódrészlet egy vagy két teknőc példányt hoz létre? 
Egyet.

A Sanyi színének megváltoztatása Eszti színét is meg fogja változtatni?
Igen
Magyarázd el részletesen!
Azért, mert Sanyi és Eszti referenciája ugyanarra az objektumra mutat, a kettő valójában egy objektum két fedőnévvel.
"""

"""
3. Rajzolj az a és b számára egy pillanatképet, a következő Python kód 3. sorának végrehajtása előtti és utáni állapotában:

a = [1, 2, 3]
b = a[:]
b[0] = 5

Előtte:
a = [1, 2, 3]
b = [1, 2, 3]

Utána:
a = [1, 2, 3]
b = [5, 2, 3]
"""

"""
4. Mi lesz a következő programrészlet kimenete?

ez = ["Én", "nem", "vagyok", "egy", "csodabogár"]
az = ["Én", "nem", "vagyok", "egy", "csodabogár"]
print("Test 1: {0}".format(ez is az))
ez = az
print("Test 2: {0}".format(ez is az))

Test 1: False
Test 2: True

Adj részletes magyarázatot az eredményekről.

Az elején ez két különböző lista, uyanazzal a tartalommal, de két különböző objektum.
Az 'ez = az' utasítást kövtően viszont egy lista, két fedőnévvel, de a két név ugyanarra az objektumra mutat.
"""