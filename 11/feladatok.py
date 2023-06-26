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