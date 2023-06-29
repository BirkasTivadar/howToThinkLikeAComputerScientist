"""
Az összes feladatot egyetlen szkriptben írd meg, és a szkripthez add hozzá a korábban látott teszt és tesztkeszlet függvényeket is. Amint megoldasz egy feladatot, adj új, a feladatnak megfelelő teszteseteket a tesztkészletedhez.
Az összes feladat megoldása után ellenőrizd, hogy minden teszt sikeres-e.
"""

from egyseg_teszt import *

"""
1. A négy tájegységet rövidítse: „K” , „Ny” , „É”, „D”. Írj egy fordulj_orajarasi_iranyba függvényt, amely egy tájegységet leíró karakter rövidítését várja, és visszaadja az órajárási irányban nézve szomszédos égtáj rövidítését. Itt van néhány tesztest, melyre működnie kell a függvényednek:
Talán most azt kérdezed magadban: „Mi legyen, ha az argumentum nem is egy égtáj rövidítése?” Minden más esetben None értékkel térjen vissza a függvény:
"""


def fordulj_orajarasi_iranyba(egtaj: str):
    egtajak: list = ["É", "K", "D", "Ny", "É"]
    if egtaj not in egtajak:
        return
    return egtajak[egtajak.index(egtaj) + 1]


teszt(fordulj_orajarasi_iranyba("É") == "K")
teszt(fordulj_orajarasi_iranyba("Ny") == "É")
teszt(fordulj_orajarasi_iranyba(42) == None)
teszt(fordulj_orajarasi_iranyba("ostobaság") == None)

"""
2. Írj egy nap_nev függvényt, amely a [0, 6] tartományba eső egész számot vár paraméterként, és visszaadja az adott sorszámú nap nevét. A 0. nap a hétfő. Még egyszer leírjuk, ha nem várt érték érkezik, akkor None értékkel térj vissza. Néhány teszt, melyen át kell mennie a függvényednek:
"""


def nap_nev(nap_szama: int):
    if nap_szama > 6 or nap_szama < 0:
        return
    het_napjai: list = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    return het_napjai[nap_szama]


teszt(nap_nev(3) == "csütörtök")
teszt(nap_nev(6) == "vasárnap")
teszt(nap_nev(42) == None)

"""
3. Írd meg az előző függvény fordítottját, amely egy nap neve alapján adja meg annak sorszámát:
Még egyszer: ha a függvény érvénytelen argumentumot kap, akkor None értéket adj vissza:
"""


def nap_sorszam(nap: str):
    het_napjai: list = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    if nap not in het_napjai:
        return
    return het_napjai.index(nap)


teszt(nap_sorszam("péntek") == 4)
teszt(nap_sorszam("hétfő") == 0)
teszt(nap_sorszam(nap_nev(3)) == 3)
teszt(nap_nev(nap_sorszam("csütörtök")) == "csütörtök")
teszt(nap_sorszam("Halloween") == None)

"""
4. Írj egy függvényt, amely segít megválaszolni az ehhez hasonló kérdéseket: „Szerda van. 19 nap múlva nyaralni megyek. Milyen napra fog esni?” A függvénynek tehát egy nap nevét és egy „hány nap múlva” értéket vár argumentumként, és egy nap nevét adja vissza:
(Segítség: Érdemes felhasználni az előző két feladatban megírt függvényt a napok_hozzaadasa függvény megírásához.)
"""


def napok_hozzaadasa(nap_neve: str, nap_szam: int):
    ma_index: int = nap_sorszam(nap_neve)
    indulas_index: int = (ma_index + nap_szam) % 7
    return nap_nev(indulas_index)


teszt(napok_hozzaadasa("hétfő", 4) == "péntek")
teszt(napok_hozzaadasa("kedd", 0) == "kedd")
teszt(napok_hozzaadasa("kedd", 14) == "kedd")
teszt(napok_hozzaadasa("vasárnap", 100) == "kedd")

"""
5. Működik a napok_hozzaadasa függvényed negatív értékekre, „hány nappal korábban” kérdésekre is? Például a -1 a tegnapi napot, a -7 az egy héttel ezelőttit jelenti:
"""

teszt(napok_hozzaadasa("vasárnap", -1) == "szombat")
teszt(napok_hozzaadasa("vasárnap", -7) == "vasárnap")
teszt(napok_hozzaadasa("kedd", -100) == "vasárnap")

"""
Ha már működik a függvényed, akkor magyarázd meg miért. Ha még nem, akkor old meg, hogy működjön.
Segítség: Játszadozz néhány esettel a maradékos osztás (%) műveletet használva. (Az előző fejezet elején mutattuk be.) Különösen azt érdemes kiderítened, hogy mi történik, amikor az x % 7 kifejezésben az x negatív.
"""
# Válasz: mert a listák indexelése negatív számok esetén a végéről iterálva működik

"""
Írj egy honap_napja függvényt, mely egy hónap neve alapján megadja, hogy hány nap van a hónapban. (A szökőévekkel ne foglalkozz.):
Érvénytelen argumentum esetén None értéket kell visszaadnia a függvénynek.
"""


def honap_napja(honap: str):
    harminc_napos: list = ["április", "június", "szeptember", "november"]
    harmincegy_napos: list = ["Január", "március", "július", "augusztus", "október", "december"]

    if honap in harmincegy_napos:
        return 31

    elif honap in harminc_napos:
        return 30

    elif honap == "február":
        return 28

    return


teszt(honap_napja("február") == 28)
teszt(honap_napja("november") == 30)
teszt(honap_napja("december") == 31)

"""
7. Írj egy masodpercre_valtas függvényt, mely órákat, perceket és másodperceket kap meg argumentumként, és kiszámolja hány másodpercnek felelnek meg összesen. Néhány teszteset:
"""


def masodpercre_valtas(ora: int, perc: int, masodperc: int):
    return ora * 3600 + perc * 60 + masodperc


teszt(masodpercre_valtas(2, 30, 10) == 9010)
teszt(masodpercre_valtas(2, 0, 0) == 7200)
teszt(masodpercre_valtas(0, 2, 0) == 120)
teszt(masodpercre_valtas(0, 0, 42) == 42)
teszt(masodpercre_valtas(0, -10, 10) == -590)

"""
8. Egészítsd ki a masodpercre_valtas függvényt úgy, hogy valós számok érkezése esetén is helyesen működjön. A végeredményt egészre vágva (ne kerekítve) add meg:
"""


def masodpercre_valtas2(ora: float, perc: float, masodperc: float):
    return int(ora * 3600 + perc * 60 + masodperc)


teszt(masodpercre_valtas2(2.5, 0, 10.71) == 9010)
teszt(masodpercre_valtas2(2.433, 0, 0) == 8758)

"""
9. Írj három függvényt, melyek a masodpercre_valtas fordítottját valósítják meg:
orakra_valtas: az argumentumként átadott másodperceket órákra váltja. A teljes órák számával tér vissza.
percekre_valtas: az argumentumként átadott másodpercekből leszámítja a teljes órákat, a maradékot pedig percekbe váltja. A teljes percek számával tér vissza.
masodpercekre_valtas: visszatér az argumentumként kapott másodpercekből fennmaradó másodpercekkel.
Feltételezheted, hogy az átadott másodpercek száma egész érték. Néhány teszt:
"""


def orakra_valtas(masodperc):
    return masodperc // 3600


def percekre_valtas(masodperc):
    return (masodperc % 3600) // 60


def masodpercekre_valtas(masodperc):
    return masodperc % 60


teszt(orakra_valtas(9010) == 2)
teszt(percekre_valtas(9010) == 30)
teszt(masodpercekre_valtas(9010) == 10)

"""
10. Melyik teszt lesz sikeretlen és miért?:
"""

teszt(3 % 4 == 0)  # A maradék nem 0, hanem 3
teszt(3 % 4 == 3)
teszt(3 / 4 == 0)  # Az eredmény nem int, hanem float és így már nem 0, hanem 0.75 az eredméy
teszt(3 // 4 == 0)
teszt(3 + 4 * 2 == 14)  # Precedencia miatt a szorzás előbb kerül kiértékelésre, mint az összeadás, az eredmény: 11
teszt(
    4 - 2 + 2 == 0)  # Balról jobbra történik a kiértékelés, előbb 4-ből 2, majd ennek eredménéyhez adódik hozzá a kettő, az eredmény: 4
teszt(len("helló, világ!") == 13)

"""
11. Írj egy osszehasonlitas függvényt, amely 1-et ad vissza, ha a > b, 0-t ad vissza, ha a == b, és -1-t, ha a < b
"""


def osszehasonlitas(a: int, b: int):
    if a > b:
        return 1
    else:
        return (a == b) - 1


teszt(osszehasonlitas(5, 4) == 1)
teszt(osszehasonlitas(7, 7) == 0)
teszt(osszehasonlitas(2, 3) == -1)
teszt(osszehasonlitas(42, 1) == 1)

"""
12. Írj egy atfogo nevű függvényt, amely egy derékszögű háromszög két befogójának hossza alapján visszaadja az átfogó hosszát:
"""


def atfogo(a: int, b: int):
    return (a ** 2 + b ** 2) ** 0.5


teszt(atfogo(3, 4) == 5.0)
teszt(atfogo(12, 5) == 13.0)
teszt(atfogo(24, 7) == 25.0)
teszt(atfogo(9, 12) == 15.0)

"""
13. Implementáld a meredekseg(x1, y1, x2, y2) függvényt, úgy, hogy az (x1, y1) és (x2, y2) pontokon átmenő egyenes meredekségét határozza meg:
"""


def meredekseg(x1: int, y1: int, x2: int, y2: int):
    if (x2 - x1) == 0:
        return
    return (y2 - y1) / (x2 - x1)


teszt(meredekseg(5, 3, 4, 2) == 1.0)
teszt(meredekseg(1, 2, 3, 2) == 0.0)
teszt(meredekseg(1, 2, 3, 3) == 0.5)
teszt(meredekseg(2, 4, 1, 2) == 2.0)
teszt(meredekseg(2, 4, 2, 5) == None)

"""
14. Írj egy paros_e(n) függvényt, amely egy egészet vár argumentumként, és True-t ad vissza, ha az argumentum páros szám, és False-t, ha páratlan.
Adj a tesztkészlethez saját teszteseteket.
"""


def paros_e(num: int):
    return num % 2 == 0


teszt(paros_e(2))
teszt(paros_e(-24))
teszt(not paros_e(13))
teszt(paros_e(256))

"""
15. Most írj egy paratlen_e(n) függvényt is, amely akkor tér vissza True értékkel, ha n páratlan, és akkor False értékkel, ha páros.
Teszteket is készíts!
"""


def paratlan_e(num: int):
    return num % 2 != 0


teszt(not paratlan_e(256))
teszt(not paratlan_e(28))
teszt(paratlan_e(25))
teszt(paratlan_e(-5))

"""
16. Készíts egy tenyezo_e(t, n) fejlécű függvényt, amely átmegy az alábbi teszteken. (Ne csak a prímtényezőkre adjon vissza igazat a függvényed.)
"""


def tenyezo_e(oszto, osztando):
    return osztando % oszto == 0


teszt(tenyezo_e(3, 12))
teszt(not tenyezo_e(5, 12))
teszt(tenyezo_e(7, 14))
teszt(not tenyezo_e(7, 15))
teszt(tenyezo_e(1, 15))
teszt(tenyezo_e(15, 15))
teszt(not tenyezo_e(25, 15))
"""
Az egységteszt fontos szerepe, hogy „félreérhetetlen” követelmény megadásként viselkedjen. A tesztesetek megadják a választ arra a kérdésre, hogy magát az 1-et és a 15-öt is a 15 tényezőjének tekintsük-e.
"""

"""
17. Írj egy tobbszorose_e fejlécű függvényt, mely kielégíti az alábbi egységtesztet.
"""


def tobbszorose_e(osztando, oszto):
    return osztando % oszto == 0


"""
Fel tudnád-e használni a tenyezo_e függvényt a tobbszorose_e függvény megírásánál?
Igen:

def tobbszorose_e(osztando, oszto):
    return tenyezo_e(oszto, osztando)
"""

teszt(tobbszorose_e(12, 3))
teszt(tobbszorose_e(12, 4))
teszt(not tobbszorose_e(12, 5))
teszt(tobbszorose_e(12, 6))
teszt(not tobbszorose_e(12, 7))

"""
18. Írj egy celsiusra_valtas(f) függvényt, mely egy Fahrenheitben megadott értéket Celsius fokra vált át. A függvény a legközelebbi egész értéket adja vissza. (Segítség: Ha a beépített round függvényt szeretnéd használni, próbáld kiíratni a round.__doc__ -et a Python konzolban, vagy a függvény nevén állva nyomd le a Ctrl+Q billentyűkombinációt. Kísérletezz, ameddig rá nem jössz, hogyan működik. ):
"""


def celsiusra_valtas(fahrneheit):
    return round((fahrneheit - 32) / 1.8)


teszt(celsiusra_valtas(212) == 100)  # A víz forráspontja
teszt(celsiusra_valtas(32) == 0)  # A víz fagyáspontja
teszt(celsiusra_valtas(-40) == -40)  # Ó, micsoda érdekes eset!
teszt(celsiusra_valtas(36) == 2)
teszt(celsiusra_valtas(37) == 3)
teszt(celsiusra_valtas(38) == 3)
teszt(celsiusra_valtas(39) == 4)

"""
19. Most tedd az ellenkezőjét: írj egy celsiusra_valtas függvényt, mely egy Celsius-fokban megadott értéket Fahrenheit skálára vált át:
"""


def fahrenheitre_valtas(celsius):
    return round((celsius * 1.8) + 32)


teszt(fahrenheitre_valtas(0) == 32)
teszt(fahrenheitre_valtas(100) == 212)
teszt(fahrenheitre_valtas(-40) == -40)
teszt(fahrenheitre_valtas(12) == 54)
teszt(fahrenheitre_valtas(18) == 64)
teszt(fahrenheitre_valtas(-48) == -54)
