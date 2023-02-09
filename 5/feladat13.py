# 13. Ha kíváncsivá tett, hogy a lebegőpontos számok aritmetikája miért pontatlan néha, akkor egy darab papíron oszd el a 10-et 3-mal és írd le a decimális eredményt! Azt találod, hogy az osztás sohasem fejeződik be és végtelen hosszú papírra lesz szükséged. A számítógépek memóriájában a számok ábrázolásának ugyanez a problémája: a memória véges és lesznek helyiértékek, amelyek eldobásra kerülnek. Így egy kis pontatlanság kerül a dologba. Próbáld ki ezt a szkriptet:

import math

a = math.sqrt(2.0)
print(a, a * a)
print(a * a == 2.0)
