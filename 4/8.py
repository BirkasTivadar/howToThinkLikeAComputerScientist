# 8. Írj egy kor_terulet(r) fejlécű produktív függvényt, amely egy r sugarú kör területét adja vissza.

def kor_terulet(r: float):
    return r * r * 3.14159265359


r: float = float(input("Kérem a kör sugarát: "))

print("A kör területe: ", kor_terulet(r))
