# 1.Tételezzük fel, hogy a hét napjai hétfőtől vasárnapig be vannak számozva: 0,1,2,3,4,5,6. Írj egy függvényt, amely megkapja egy nap számát, és visszatér annak nevével!

def het_napja(nap_szama: int):
    het_napjai: list = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    return het_napjai[nap_szama]

