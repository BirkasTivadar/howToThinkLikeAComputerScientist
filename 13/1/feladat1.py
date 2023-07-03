"""
1. Írj egy olyan programot, amely beolvas egy fájlt, és a sorait fordított sorrendben írja be egy új fájlba
(például az első sor a régi fájlban az utolsó, és az utolsó sor a régi fájlban az első).
"""


def sorFordito(readFile: str, writeFile: str):
    f = open(readFile)
    xs = f.readlines()
    f.close()

    xs[len(xs) - 1] += "\n"

    g = open(writeFile, "w")
    for i in range(len(xs)):
        g.write(xs[-(i + 1)])
    g.close()


sorFordito("test1.txt", "forditott.txt")
