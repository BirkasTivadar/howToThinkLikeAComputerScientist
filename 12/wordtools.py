import string


def szo_tisztitas(szoveg: str):
    tiszta = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            tiszta += karakter
    return tiszta


def van_duplavonal(szoveg: str):
    return "--" in szoveg


def szavakra_bontas(szoveg: str):
    return szo_tisztitas(szoveg).lower().split()


def szavak_szama(szo: str, szavak: list):
    return sum(1 for elem in szavak if elem == szo)


def szo_halmaz(szavak: list):
    import locale
    import functools

    szavak_halmaza = list(set(szavak))
    locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")
    szavak_halmaza.sort(key=functools.cmp_to_key(locale.strcoll))
    return szavak_halmaza


def leghosszabb_szo(szavak: list):
    if len(szavak) == 0:
        return 0
    else:
        return max(map(lambda szo: len(szo), szavak))
