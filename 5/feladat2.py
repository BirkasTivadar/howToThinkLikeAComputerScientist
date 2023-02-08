# 2. Elmész egy gyönyörű nyaralásra (talán börtönbe, ha nem kedveled a mókás feladatokat) és a 2-es számú napon (tehát szerdán) indulsz. 137 ott alvás után térsz haza. Írj egy programot, amely megkérdezi, hogy hányas számú napon indultál és hány óráig voltál távol, majd megmondja annak a napnak a nevét, amikor hazatérsz.

import feladat1

def hazateres_napja(indulas: int, maradas_ora: int):
    maradas_nap: int = maradas_ora // 24
    result = (indulas + maradas_nap) % 7
    return feladat1.het_napja(result)

