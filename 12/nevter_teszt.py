"""
4. Hozd létre a sajatmodul1.py-t!
Az sajatev attribútumhoz rendeld hozzá az életkorod, és az ev-hez az aktuális évet! Hozd létre egy másik sajatmodule2.py-t!
A sajatev attribútumot állítsd 0-ra, és az ev attribútumot arra az évre, amikor születtél! Most hozd létre a nevter_teszt.py fájlt!
Importáld mindkét fent megadott modult, és futtasd a következő utasítást:

print( (sajatmodul2.sajatev - sajatmodul1.sajatev) == (sajatmodul2.ev - sajatmodul1.ev)  )
A nevter_teszt.py futtatásakor True vagy False kimenet jelenik meg, attól függően, hogy az idén volt-e már születésnapod.

Ez a példa szemlélteti, hogy a különböző modulok egyaránt rendelkezhetnek sajatev és ev nevű attribútumokkal.
Mivel különböző névtérben vannak, ezért nem ütköznek egymással.
Amikor a nevter_teszt.py-t megírjuk, pontosan meghatározzuk, hogy melyik ev és sajatev változókra hivatkozunk.
"""

import sajatmodul1
import sajatmodul2

print((sajatmodul2.sajatev - sajatmodul1.sajatev) ==
      (sajatmodul2.ev - sajatmodul1.ev))

"""
Írd a következő utasításokat a sajatmodul1.py, a sajatmodul2.py és a nevter_teszt.py fájlokhoz az előző gyakorlatból:

print("Az én nevem", __name__)
Futtassuk a nevter_teszt.py-t! Mi történik? Miért? Most adjuk hozzá a következőket a sajatmodul1.py végére:

if __name__ == "__main__":
    print("Ez nem fog futni, ha importálok.")
Futtasd újra a sajatmodul1.py és nevter_teszt.py-t! Mely esetben látod az új kiíratást?
"""