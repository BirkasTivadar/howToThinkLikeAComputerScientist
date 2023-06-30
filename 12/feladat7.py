"""
7. Add meg a következő Python kód válaszát az utasítások mindegyikére, folyamatosan a végrehajtás során:

s = "Esik eső csendesen, lepereg az ereszen..."
print(type(s.split()))
print(s.split("e"))
print(s.split("s"))
print("0".join(s.split("e")))
"""
s = "Esik eső csendesen, lepereg az ereszen..."
# print(s.split())
# ['Esik', 'eső', 'csendesen,', 'lepereg', 'az', 'ereszen...']

# print(type(s.split()))
# <class 'list'>

# print(s.split("e"))
# ['Esik ', 'ső cs', 'nd', 's', 'n, l', 'p', 'r', 'g az ', 'r', 'sz', 'n...']

# print(s.split("s"))
# ['E', 'ik e', 'ő c', 'ende', 'en, lepereg az ere', 'zen...']

# print("0".join(s.split("e")))
# Esik 0ső cs0nd0s0n, l0p0r0g az 0r0sz0n...


"""
Győződj meg arról, hogy megértetted miért kaptad az eredményeket! 
Ezután alkalmazd a tanultakat, és töltsd ki az alábbi függvény törzsét, használva a spilt, join metódusokat és az str objektumotokat:


def cserel(regi, uj, s):
  # Cseréld az s-ben a regi paraméter összes előfordulását az uj-ra.
   ...

A megoldásoknak át kell mennie a teszteken.
"""
from egyseg_teszt import *


def cserel(regi: str, uj: str, s: str):
    if regi == " ":
        return uj.join(s.split())
    else:
        return uj.join(s.split(regi))


teszt(cserel(",", ";", "ez, az, és valami más dolog") ==
      "ez; az; és valami más dolog")
teszt(cserel(" ", "**", "A szavak  most     csillaggal vannak elválasztva.") ==
      "A**szavak**most**csillaggal**vannak**elválasztva.")
