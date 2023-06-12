"""
8.19. Feladatok
Javasoljuk, hogy egy fájlban készítsd el az alábbi feladatokat, az előző feladatokban látott tesztelő függvényeket is bemásolva a fájlba.
"""

from test import *

"""
1. Milyen eredményt adnak az alábbi kifejezések? (Ellenőrizd a válaszaid a print függvény segítségével.)

"Python"[1]
"A sztringek karaktersorozatok."[5]
len("csodálatos")
"Rejtély"[:4]
"k" in "Körte"
"barack" in "sárgabarack"
"körte" not in "Ananász"
"barack" > "sárgabarack"
"ananász" < "Barack"
"""

teszt("Python"[1] == "y")
teszt("A sztringek karaktersorozatok."[5] == "r")
teszt(len("csodálatos") == 10)
teszt("Rejtély"[:4] == "Rejt")
teszt(("k" in "Körte") == False)
teszt(("barack" in "sárgabarack") == True)
teszt(("körte" not in "Ananász") == True)
teszt(("barack" > "sárgabarack") == False)
teszt(("ananász" < "Barack") == False)

"""
2. Javítsd ki úgy az alábbi programot, hogy Törpapa és Törpicur neve is helyesen jelenjenek meg:

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    print(elotag + utotag)
"""

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    if (utotag[0] == "p"):
        utotag = utotag[1:]
    print(elotag + utotag)

"""
3. Ágyazd be az alábbi kódrészletet egy karakter_szamlalas nevű függvénybe, majd általánosítsd úgy, hogy a sztringet és a számlálandó karaktert is paraméterként várja. A függvény adja vissza a karakter sztringbeli előfordulásainak számát, ne írassa ki. Az érték megjelenítése a függvény hívójának feladata.

gyumolcs = "banán"
darab = 0
for karakter in gyumolcs:
    if karakter == "a":
        darab += 1
print(darab)
"""


def karakter_szamlalas(szoveg: str, karakter: str):
    darab = 0
    for k in szoveg:
        if k == karakter:
            darab += 1
    return darab


teszt(karakter_szamlalas("Hello World", "l") == 3)
teszt(karakter_szamlalas("Hello World", "j") == 0)

"""
4. Most írd át úgy a karakter_szamlalas függvényt, hogy a sztring bejárása helyett a beépített find metódusát hívja meg újra és újra. A második paraméternek átadott értékkel biztosíthatod, hogy a metódus mindig új előfordulását találja meg a számlálandó karakternek.
"""


def karakter_szamlalas_find(szoveg: str, karakter: str):
    darab = 0
    index = szoveg.find(karakter)
    while index != -1:
        darab += 1
        szoveg = szoveg[index + 1:]
        index = szoveg.find(karakter)
    return darab


teszt(karakter_szamlalas_find("Hello Worll", "l") == 4)
teszt(karakter_szamlalas_find("Hello World", "j") == 0)

"""
5. Adj értékül egy bekezdést a kedvenc szövegedből – egy beszédből, egy süteményes receptkönyvből, vagy egy inspiráló versből, stb. – egy változónak. A szöveget tripla idézőjelek közé zárd.

Írj egy függvényt, amely eltávolítja az összes írásjelet a sztringből, és a szöveget szavak listájára bontja. Számold meg, hány olyan szó van a szövegben, melyben szerepel az „e” betű. Jeleníts meg egy alábbihoz hasonló elemzést a szövegedről:

A szövegben 243 szó áll, melyből 109 (44.8%) tartalmaz "e" betűt.
"""

szoveg = """
Mikszáth Kálmán

A KASZÁT VÁSÁRLÓ PARASZT •
1885
(36. kötet)
Tanúja voltam egyszer, midőn Csomák Gergely uram benyitott a vaskereskedésbe.
– Szerencsés jó napot! – mondá.
– Mi tetszik?
– Kasza kellenék.
A kereskedő ugrik, és egy csomó kaszát tesz eléje. Csomák uram ellenséges szemmel bandzsít a kaszák felé.
– Ágyú-jegyűt adjék az úr – szól megvetőleg elfordulva a kaszáktól.
A kereskedő visszarakja a bika-jegyű kaszákat, s az ágyú-jegyűekből hoz nehányat.
– Termett ott még több is – szólt oda félvállról.
A kereskedő türelmesen eléje szállítja minden ágyújegyű kaszáját.
Csomák Gergely szeme végigsiklik valamennyin, de a világért sem nyúlna egyikhez sem. Elkezdi a fejét vakarni.
– No, mi a baj még?
– Hogy voltaképpen mégiscsak hadd lám a bika-jegyűeket.
Mit lehetett tenni egyebet, mint újra visszahurcolni a bika-jegyű kaszákat.
Gergely gazda most már szinte maga is röstelli a dolgot, s csak úgy találomra látszik a sok közül kezébe venni az egyiket.
Behunyja először a jobb szemét, és úgy néz végig rajta, azután a bal szemét hunyja be, miközben már függőlegesen tartja a kaszát, majd leereszti a hegyével, végül pedig fölemeli a feje fölé, s alulról sandít rá hosszadalmasan.
– Hogy ez? – veti oda közömbösen.
– Két forint.
– Ez a kasza? – kérdi gúnyosan. – Nem lehet az! Már hogy ez a kasza?
Végigfekteti a pudlin, s a kezével egy vonalat húz a levegőben, amerre a nyél fog. következni, hogy miképp veszi majd ki magát. Aztán a bütykös nagyujját végighúzza a pengéjén mind a két oldalon, megkopogtatja négy-öt helyen a mutatóujja kalácsával, majd leereszti a földre, és a féltérdén meghajlítja.
– Hüm... No... igazán két forint ez a kasza
A kereskedő esküdözik, nem adhatja olcsóbban. Neki magának is annyiba van.
– Pedig nincs jól kiégetve, hallja az úr.
– A legfinomabb angol kasza.
– Ugyan ne tegyen bolonddá az úr. Ócska kaszából van ez megkalapálva.
– Kitűnő matéria! Holtig eltart.
– Ha ki nem csorbul – teszi hozzá nevetve Csomák Gergely.
– Ilyen kaszája még nem volt kendnek.
– Mármint nékem? Hát minek gondol engem az úr?
– Csak nézze meg, kérem, azt a kaszát.
– Megnézzem? Minek nézzem? Kasza, kasza. Egyik olyan kasza, mint a másik. Nem nézem biz én. Amelyik éppen a kezembe került. Azért csak ki a színnel szaporán, mit kíván érte, nekem sürgős dolgom van a piacon.
– Mondtam már, két forint!
– Hát van istene az úrnak? Két forintot kérni egy ilyen jószágért. Csak már legalább tudnám, mi van rajta.
S azzal ismétlen vizsgálat alá veszi a kaszát, suhint vele egyet, majd fölkerekedik, s kifelé viszi a nagyobb világosság okáért. A küszöbről bekiált:
– A kalapomat odabent hagytam.
Ott künn megtáncoltatja a pengén a napsugarakat, amik pajkosan futnak át a kékes sima lapon. A szájához emeli, rálehel, s várja mély áhítattal, mekkora darabon vonta be hályogosra a lehelet, s mily gyorsan illan. Azután megpengeti a kövezeten.
– Bolond egy csengése van – dörmögi, s erre besompolyog a boltba, még ott is ezen nyargal: – Nem tetszik nekem a csengése. Ideadja az úr egy forint nyolcvan krajcárért, vagy nem?
– Isten neki, egy hatost engedek. Vigye el egy forint kilencvenért.
– Nem lehet, nem éri meg. Kiátkoznának a gyermekeim. Adja, nem adja úgy?
– Nem adom alább.
– Akkor isten áldja meg!
Kioldalog, de csak az utca közepéig, onnan legott visszatér, és még egyszer bekurjant:
– Adja vagy nem adja?
– Nem adom.
Zavartan, fejcsóválva forgatja zsíros kalapját a markában.
– No, még ilyen kemény lélekkel sem volt dolgom, mióta az eszemet tudom. Hát tudja mit az úr? Tegye félre ezt a kaszát ide a sarokba. Majd meggondolom még egy kicsit odakünn.
Egy jó óra múlva visszatér egy más atyafival.
– Eljöttem – lihegi a verejtéket törülgetve homlokáról –, ez itt a keresztkomám Dorozsmáról, a Komót Istók. Azt gondoltuk ki, hogy ő is kaszát veszen, ha már így van, mert hogy hát az volna a rendje, ha ketten két kaszát veszünk, mindenik olcsóbban kapja a magáét.
– Nem adhatom olcsóbban… százszor megmondtam.
– Fontolja meg az úr, ne hirtelenkedje el a dolgot.
– Egy szó, mint száz.
– Nem enged? – pattan föl dühösen.
– Nem engedek – felel az határozottan.
– Hát akkor én mit mondjak? – toldítja engesztelődve.
– Mondjon, amit tetszik. Én többet nem beszélek kenddel.
– Nono, nem kell ám mindjárt megharagudni. Ha a szavát sajnálja tőlem az úr, akkor hát adja ide a tenyerét.
Csomák Gergely uram most már belecsap a vaskereskedő tenyerébe nagy vidáman.
– Eb, aki megbánja. Megvan a vásár!
Lassú ünnepélyességgel kezdi kigombolgatni a lajbliját, mialatt a világért sem venné le a tekintetét a sarokról, ahol a megvett kasza áll megtámasztva.
– De nini – villan fel agyában –, mintha görbébb, kisebb lenne az a kasza.
Gyanakvó arccal fürkészi a bolt személyzetét. Majd felkapja a kaszát, s mérlegeli a súlyra nézve.
– Ez más kasza – tör ki zordonan –, akármi legyek, ez nem az én kaszám.
S hirtelen összegombolja az ólompitykéket a mellényén.
– Már hogyne volna az a kasza? Ne okoskodjék, Gergely bácsi, mert kijövök a béketűrésből!
– No már, no már…. ej, ej… De minek is vitt el az ördög innen? Magam vagyok az oka. Itt van ni! Most már mit csináljak?
– De ha mondom, hogy az a kasza.
– Mármint ez? Hiszen nekem is megvan a két látó szemem.
Végighúzza pengéjén az ujját, meghajlítja a térdén, megkopogtatja, kiviszi az utcára, odaveregeti a kövezethez, rálehel, suhint vele, és betámolyog nagy szomorúan.
– Ez nem az a kasza! Ezért nem adhatok többet négy váltó forintnál.
– Ne csináljon komédiákat. Ha nem tetszik a kasza, ott van valamennyi, válasszon közülök másikat.
– Azt a bolondot nem teszem, hogy elölről kezdjem a vesződséget. Maradjon ez a kasza, de az illendő árán, amennyivel kevesebbet ér.
– Egy szót se többet.
– Mi? Csakugyan nekem kell károsodnom? Jó. Hát csakugyan elveszi az úr tőlem azt a fölösleget? Ráfér a lelkére?
– Fizessen kend hamar, és ne tartson itt prédikációkat.
– Jó – kiált fel Csomák Gergely uram keserűen. – Legyen az úrnak igaza. De vágjuk az igazságot kétfelé, hogy énrajtam se essék igazságtalanság. Felezzük meg az egy váltó forintot.
– Nem felezek.
– Akkor hát itt van a pénze! Fogja!
Újra hozzálátott a lajbli kigombolásához, amelynek a belső zsebéből nagy nehezen kihalász vala egy harisnyát, aminek a legfenekéről kivett egy forintos bankót, és odaadta a kereskedőnek.
– A többit mindjárt hozzáolvasom.
A mellény külső zsebéből előhúzott egy kéthatosost, a másikból egy négykrajcárost…
– Hogyis csak? Ez huszonnégy…
Benyúlt a nadrágzsebébe, ahol 33 krajcárra akadt.
– Huszonnégy és harminchárom, az ötvenhét… Mennyi kell még?
– Még harminchárom krajcár…
– Annyi – teszi hozzá jámbor képpel –, de nehezen lesz.
S ezalatt ártatlan, jámbor arccal kémleli a kereskedő hangulatát.
– Hopp… azaz, hogy… Megállj csak, megállj. Hová is tettem? Mit gondol, komámuram? Aha, itt lesz a kendő csücskében…
A fehér gyolcskendő szélibe csakugyan egy kéthatos volt bekötve.
– Ez az irmag, nemzetes uram – mondja nyájasan –, ott az isten se vesz, ahol nem talál.
– Még tizenhárom krajcár – sürgeti a kereskedő könyörtelenül.
– Ugyan ne okoskodjék, nemzetes uram. Mire való az? Így is rosszabb kaszát kaptam, mint kellett volna. Osztég nincs nálam egy garas sem, ott hagytam a szekeren a guba ujjában, azt csak nem kívánja, hogy olyan messze szaladjak azért az egypár fillérért. Majd kipótolom máskor.
– Nekem az egész összeg kell. Menjen a pénzért, addig a kasza el nem szalad.
De már erre méregre gyulladt Csomák Gergely:
– Mit? Nekem annyi becsületem sincs? Nekem az apám, nagyapám is bíróságot viselt perszóna volt, hallja az úr! Nem kell nekem senkinek a kegyelme. Nem a szemeten szedtek fel engem. Lökje neki oda, komámuram, azt a tizenhárom krajcárt!
S azzal sértődve felkapja a kaszát.
– Gyerünk, komámuram…
A boltajtónál visszafordult kárörvendő, kaján szemekkel, egyet rántott a vállán, s a kaszát diadalmasan megvillogtatva, harsányan bekiáltott:
– Annyit azonban mondhatok az úrnak, hogy ez volt a legjobb kaszája, az a többi nem ér egy hajítófát.
"""


def irasjel_eltavolitas(szoveg: str):
    import string
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli


def szoSzamlalo(szoveg: str, betu: str = "e"):
    szavak = irasjel_eltavolitas(szoveg).split()
    szoszam = len(szavak)
    betusek = sum(1 for szo in szavak if betu in szo)
    szazalek = float(betusek / szoszam) * 100
    print(
        'A szövegben {0} szó áll, melyből {1} ({2:.1f}%) tartalmaz {3} betűt.'.format(szoszam, betusek, szazalek, betu))


szoSzamlalo(szoveg)

"""
6. Jeleníts meg egy ilyen szorzótáblát:

        1   2   3   4   5   6   7   8   9  10  11  12
  :--------------------------------------------------
 1:     1   2   3   4   5   6   7   8   9  10  11  12
 2:     2   4   6   8  10  12  14  16  18  20  22  24
 3:     3   6   9  12  15  18  21  24  27  30  33  36
 4:     4   8  12  16  20  24  28  32  36  40  44  48
 5:     5  10  15  20  25  30  35  40  45  50  55  60
 6:     6  12  18  24  30  36  42  48  54  60  66  72
 7:     7  14  21  28  35  42  49  56  63  70  77  84
 8:     8  16  24  32  40  48  56  64  72  80  88  96
 9:     9  18  27  36  45  54  63  72  81  90  99 108
10:    10  20  30  40  50  60  70  80  90 100 110 120
11:    11  22  33  44  55  66  77  88  99 110 121 132
12:    12  24  36  48  60  72  84  96 108 120 132 144
"""

elrendezes = "{0:>3}{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{2:>4}{10:>4}{11:>4}{12:>4}"

print(elrendezes.format("", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print(elrendezes.format(":", "------", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----",
                        "----"))

for i in range(1, 13):
    print(elrendezes.format(str(i) + ":", i * 1, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11,
                            i * 12))

"""
7. Írj egy függvényt, amely meghatározza egy paraméterként kapott sztring fordítottját. A függvénynek át kell mennie ezeken a teszteken:

teszt(sztring_forditas("boldog") == "godlob")
teszt(sztring_forditas("Python") == "nohtyP")
teszt(sztring_forditas("") == "")
teszt(sztring_forditas("a") == "a")
"""


def sztring_forditas(sztring: str):
    eredmeny = ""
    for karakter in sztring:
        eredmeny = karakter + eredmeny
    return eredmeny


teszt(sztring_forditas("boldog") == "godlob")
teszt(sztring_forditas("Python") == "nohtyP")
teszt(sztring_forditas("") == "")
teszt(sztring_forditas("a") == "a")

"""
8. Írj egy függvényt, amely összefűzi argumentumát annak tükörképével:

teszt(tukor("jo") == "jooj")
teszt(tukor("Python") == "PythonnohtyP")
teszt(tukor("") == "")
teszt(tukor("a") == "aa")
"""


def tukor(sztring: str):
    return sztring + sztring_forditas(sztring)


teszt(tukor("jo") == "jooj")
teszt(tukor("Python") == "PythonnohtyP")
teszt(tukor("") == "")
teszt(tukor("a") == "aa")

"""
9. Írj függvényt, amely eltávolítja egy karakter összes előfordulását egy sztringből. A függvény a karaktert és a sztringet is argumentumként várja.

teszt(betu_eltuntetes("a", "alma") == "lm")
teszt(betu_eltuntetes("a", "banán") == "bnán")
teszt(betu_eltuntetes("z", "banán") == "banán")
teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
teszt(betu_eltuntetes("b", "") == "")
teszt(betu_eltuntetes("b", "c") == "c")
"""


def betu_eltuntetes(karakter: str, sztring: str):
    eredmeny: str = ""
    for k in sztring:
        if k != karakter:
            eredmeny += k
    return eredmeny


teszt(betu_eltuntetes("a", "alma") == "lm")
teszt(betu_eltuntetes("a", "banán") == "bnán")
teszt(betu_eltuntetes("z", "banán") == "banán")
teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
teszt(betu_eltuntetes("b", "") == "")
teszt(betu_eltuntetes("b", "c") == "c")

"""
10. Írj függvényt, mely képes a palindromok felismerésére. (Segítség: a korábban megírt sztring_forditas függvény felhasználása megkönnyíti a dolgod!):

teszt(palindrom_e("abba"))
teszt(not palindrom_e("abab"))
teszt(palindrom_e("teret"))
teszt(not palindrom_e("banán"))
teszt(palindrom_e("mesék késem"))
teszt(palindrom_e("a"))
# teszt(palindrom_e(""))    # Egy üres sztring palindrom-e?
"""


def palindrom_e(sztring: str):
    return sztring == sztring_forditas(sztring)


teszt(palindrom_e("abba"))
teszt(not palindrom_e("abab"))
teszt(palindrom_e("teret"))
teszt(not palindrom_e("banán"))
teszt(palindrom_e("mesék késem"))
teszt(palindrom_e("a"))
teszt(palindrom_e(""))  # Egy üres sztring palindrom-e?

"""
11. Írj egy függvényt, amely meghatározza, hányszor szerepel egy sztringben egy másik sztring:

teszt(szamlalas("gö", "görögös") == 2)
teszt(szamlalas("pa", "papaja") == 2)
teszt(szamlalas("apa", "papaja") == 1)
teszt(szamlalas("papa", "papaja") == 1)
teszt(szamlalas("apap", "papaja") == 0)
teszt(szamlalas("aaa", "aaaaaa") == 4)
"""


def szamlalas(keresett: str, sztring: str):
    szamlalo = 0
    jelzo = sztring.find(keresett)
    while (jelzo != -1):
        szamlalo += 1
        sztring = sztring[jelzo + 1:]
        jelzo = sztring.find(keresett)
    return szamlalo


teszt(szamlalas("gö", "görögös") == 2)
teszt(szamlalas("pa", "papaja") == 2)
teszt(szamlalas("apa", "papaja") == 1)
teszt(szamlalas("papa", "papaja") == 1)
teszt(szamlalas("apap", "papaja") == 0)
teszt(szamlalas("aaa", "aaaaaa") == 4)

"""
Írj függvényt, amely eltávolítja egy sztringből egy másik sztring első előfordulását:

teszt(torles("alma", "almafa") == "fa")
teszt(torles("an", "banán") == "bán")
teszt(torles("pa", "papaja") == "paja")
teszt(torles("pa", "Papaja") == "Paja")
teszt(torles("alma", "kerékpár") == "kerékpár")
"""


def torles(keresett: str, sztring: str):
    index = sztring.find(keresett)
    if index == -1:
        return sztring
    hossz = len(keresett)
    return sztring[:index] + sztring[index + hossz:]


teszt(torles("alma", "almafa") == "fa")
teszt(torles("an", "banán") == "bán")
teszt(torles("pa", "papaja") == "paja")
teszt(torles("pa", "Papaja") == "Paja")
teszt(torles("alma", "kerékpár") == "kerékpár")

"""
13. Írj függvényt, amely eltávolítja egy sztringből egy másik sztring minden előfordulását. (A törlés hatására új előfordulások is keletkezhetnek. Rád bízzuk, hogy ezeket eltűnteted-e.):

teszt(alapos_torles("an", "banán") == "bán")
teszt(alapos_torles("pa", "papaja") == "ja")
teszt(alapos_torles("pa", "Papaja") == "Paja")
teszt(alapos_torles("alma", "kerékpár") == "kerékpár")
teszt(alapos_torles("pa", "ppapaa" ) == "")
"""


def alapos_torles(keresett: str, sztring: str):
    eredmeny = sztring
    index = eredmeny.find(keresett)
    while index != -1:
        eredmeny = torles(keresett, eredmeny)
        index = eredmeny.find(keresett)
    return eredmeny


teszt(alapos_torles("an", "banán") == "bán")
teszt(alapos_torles("pa", "papaja") == "ja")
teszt(alapos_torles("pa", "Papaja") == "Paja")
teszt(alapos_torles("alma", "kerékpár") == "kerékpár")
teszt(alapos_torles("pa", "ppapaa") == "")
