# 8. Írj egy Python programot az előző feladat általános megoldására. Kérd be a felhasználótól az aktuális időt (csak az órákat) és azt, hogy hány órával később szólaljon meg az ébresztőóra, majd jelenítsd meg a képernyőn, hogy hány órakor fog megszólalni az ébresztőóra.

actual_hour: int = int(input("Hány óra van most?\n"))
plus_hour: int = int(input("Hány óra múlva szóljon az ébresztő?\n"))

wake_hour: int = (plus_hour - (24 - actual_hour)) % 24

print(wake_hour)
