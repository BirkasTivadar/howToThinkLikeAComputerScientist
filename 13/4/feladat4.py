"""
4. Írj egy olyan programot, amely megszünteti az előző gyakorlat számozását:
ennek egy beszámozott sorokat tartalmazó fájlt kellene beolvasnia,
és egy másik fájlt előállítani a sorszámok nélkül.
"""


def sorszamKiszedo(readFile: str, writeFile: str):
    f = open(readFile)
    xs = f.readlines()
    f.close()

    g = open(writeFile, "w")
    for i in range(len(xs)):
        sor = xs[i][5:]
        g.write(sor)
    g.close()

sorszamKiszedo("test4.txt", "sorszamtalan.txt")
