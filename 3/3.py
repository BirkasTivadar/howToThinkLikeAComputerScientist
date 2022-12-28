# 3. Írj egy programot, ami a for ciklus használatával az alábbi szöveget írja ki
# Az év egyik hónapja január.
# Az év egyik hónapja február.
# stb.

months: list[str] = ["jaunár", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember",
                     "október", "november", "december"]

for month in months:
    print("Az év egyik hónapja {0}".format(month))
