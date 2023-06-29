"""
Olvasd el a calendar modul dokumentációját.

Próbáld ki a következőket:

import calendar
naptar = calendar.TextCalendar()      # Hozd létre egy példányát!
naptar.pryear(2017)                   # Mi történik itt?
Figyeld meg, hogy a hét hétfőn kezdődik!
A kalandvágyó informatikus hallgató azt gondolja, hogy jobb felosztás lenne, ha a hét csütörtökön kezdődne, mert csak két munkanap lenne a hétvégéig, és minden hét közepén szünetet tarthatnának.

Keress egy olyan függvényt, amelynek segítségével kiírhatod ebben az évben a születésnapodnak megfelelő hónapot!

Próbáld ki ezt:

d = calendar.LocaleTextCalendar(6, "HUNGARIAN")
d.pryear(2017)

Próbálj ki néhány más nyelvet, beleértve egyet, amelyen nem működik, és figyeld meg, mi történik!

Kísérletezz a calendar.isleap-el!
Milyen argumentumok kér?
Mi lesz a visszatérési értéke? Milyen függvény ez?

Készíts részletes jegyzetet arról, hogy mit tanultál ezekből a feladatokból!
"""

import calendar

naptar = calendar.TextCalendar()  # Hozd létre egy példányát!
print("1/a feladat: ")
naptar.pryear(2017)  # Mi történik itt?
# Kiírja az adott év naptrárát


print("\n1/b feladat: ")
calendar.setfirstweekday(calendar.THURSDAY)
print(calendar.firstweekday())

print("\n1/c feladat: ")
naptar.prmonth(2023, 4)

print("\n1/d feladat: ")
d = calendar.LocaleTextCalendar(6, "HUNGARIAN")
d.pryear(2017)

d = calendar.LocaleTextCalendar(6, "SPANISH")
d.pryear(2017)

# d = calendar.LocaleTextCalendar(6, "ABOLISH")
# d.pryear(2017)


print("\n1/e feladat: ")
print(calendar.isleap(2023))
print(calendar.isleap(2020))
# Boolean-nal tér vissza, attól függően, hogy a paraméteként átadott évszámnak megfelelő év szökőév e.
