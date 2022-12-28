# 5. Írj programot, amely meghatározza, mennyi lesz egy betét értéke a futamidő végén, ha 10000 Ft-t helyezünk betétbe 8%-os névleges kamatláb mellett. Az évközi kamatozások száma (m) 12. Az évek számát, vagyis a t értékét a felhasználótól kérje be a program. A futamidő végén nézett értéket (FV) az 5.png ábrán lévő képlet alapján számold:


C: int = 10000
r: float = 0.08
m: int = 12

t: int = int(input("Kérem az évek számát: "))

FV: float = C * (1 + r / m) ** (m * t)

print(FV)
