"""
8. Készíts egy wordtools.py modult, mely lehetővé teszi az egységteszt használatát helyben.

Most add hozzá a függvényeket ezekhez a tesztekhez.
"""
from egyseg_teszt import *
from wordtools import *

teszt(szo_tisztitas("hogyan?") == "hogyan")
teszt(szo_tisztitas("'most!'") == "most")
teszt(szo_tisztitas("?+='s-z-a-v!a,k@$()'") == "szavak")

teszt(van_duplavonal("kicsi--nagy") == True)
teszt(van_duplavonal("") == False)
teszt(van_duplavonal("magas--") == True)
teszt(van_duplavonal("piros--fekete") == True)
teszt(van_duplavonal("-igen-nem-") == False)

teszt(szavakra_bontas(" Most van itt az idő? Igen, most.") ==
      ['most', 'van', 'itt', 'az', 'idő', 'igen', 'most'])
teszt(szavakra_bontas("Ő megpróbált udvariasan viselkedni!") ==
      ['ő', 'megpróbált', 'udvariasan', 'viselkedni'])

teszt(szavak_szama("most", ["most", "később", "soha", "most"]) == 2)
teszt(szavak_szama("itt", ["itt", "ott", "amott", "itt", "ott", "amott", "itt"]) == 3)
teszt(szavak_szama("tél", ["tavasz", "nyár", "ősz", "tél", "tavasz", "nyár", "ősz"]) == 1)
teszt(szavak_szama("kakukk", ["cinege", "fecske", "gólya", "sas", "veréb", "páva", "rigó"]) == 0)

teszt(szo_halmaz(["most", "van", "itt", "most", "van", "itt"]) ==
      ["itt", "most", "van"])
teszt(szo_halmaz(["én", "te", "ő", "én", "te", "ő", "mi", "én"]) ==
      ["én", "mi", "ő", "te"])
teszt(szo_halmaz(["egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc"]) ==
      ["egy", "három", "hat", "hét", "kettő", "négy", "nyolc", "öt"])

teszt(leghosszabb_szo(["alma", "eper", "körte", "szőlő"]) == 5)
teszt(leghosszabb_szo(["én", "te", "ő", "mi"]) == 2)
teszt(leghosszabb_szo(["ez", "szórakoztatóelektronikai"]) == 24)
teszt(leghosszabb_szo([]) == 0)

"""
Mentsd el ezt a modult, hogy használhasd az eszközeit a jövőbeni programjaiban!
"""
