"""
2. Írj egy olyan programot, amely beolvas egy fájlt,
és csak azokat a sorait írja ki, melyek tartalmazzák az info részsztringet.
"""


def sorInfo(fileName: str):
    kezelo = open(fileName)
    while True:
        sor = kezelo.readline()
        if len(sor) == 0:
            break
        if "info" in sor:
            print(sor)
    kezelo.close()


sorInfo("test2.txt")
