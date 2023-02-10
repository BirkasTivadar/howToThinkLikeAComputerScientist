"""
Az összes feladatot egyetlen szkriptben írd meg, és a szkripthez add hozzá a korábban látott teszt és tesztkeszlet függvényeket is. Amint megoldasz egy feladatot, adj új, a feladatnak megfelelő teszteseteket a tesztkészletedhez.
Az összes feladat megoldása után ellenőrizd, hogy minden teszt sikeres-e.
"""

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
