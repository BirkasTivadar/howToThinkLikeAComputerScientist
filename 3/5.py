# 5. Tételezzük fel, hogy van egy xs = [12, 10, 32, 3, 66, 17, 42, 99, 20] értékadásunk.
#
#   a. Írj egy ciklust, amely mindegyik számot kiírja egy új sorba!
#   b. Írj egy ciklust, amely mindegyik számot és azok négyzetét is kiírja egy új sorba!
#   c. Írj egy ciklust, amely összeadja a listában szereplő összes számot egy összeg változóba! Az összeg változónak 0 értéket kell adnod az összegzés előtt, majd a ciklus befejezése után az összeg változó értékét írasd ki!
#   d. Írasd ki a listában szereplő összes szám szorzatát!

xs: list[int] = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a. Írj egy ciklust, amely mindegyik számot kiírja egy új sorba!
for i in xs:
    print(i)

# b. Írj egy ciklust, amely mindegyik számot és azok négyzetét is kiírja egy új sorba!
for i in xs:
    print(i, i * i)

# c. Írj egy ciklust, amely összeadja a listában szereplő összes számot egy összeg változóba! Az összeg változónak 0 értéket kell adnod az összegzés előtt, majd a ciklus befejezése után az összeg változó értékét írasd ki!
sum: int = 0
for i in xs:
    sum += i

print(sum)

# d. Írasd ki a listában szereplő összes szám szorzatát!
result: int = 1
for i in xs:
    result *= i

print(result)