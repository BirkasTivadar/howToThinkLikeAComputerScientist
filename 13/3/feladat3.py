"""
3. Írj egy olyan programot, amely beolvas egy szöveges fájlt, és egy kimeneti fájlt hoz létre, amely az eredeti fájl másolata,
kivéve, hogy minden egyes sor első öt oszlopa tartalmaz egy négyjegyű sorszámot, amelyet egy szóköz követ.
A kimeneti fájl sorszámozását 1-től kezd. Győződj meg arról, hogy minden egyes sorszám ugyanolyan széles a kimeneti fájlban.
Használd az egyik Python programot, teszt adatként ehhez a feladathoz: a kimenet a Python program kiírt és sorszámozott listája kell legyen.
"""


def sorSzamozo(readFile: str, writeFile: str):
    f = open(readFile)
    xs = f.readlines()
    f.close()

    g = open(writeFile, "w")
    for i in range(len(xs)):
        sorszam = i + 1
        sor = "{0:>4} {1}"
        g.write(sor.format(sorszam, xs[i]))
    g.close()


sorSzamozo("test3.txt", "sorszamozott.txt")
