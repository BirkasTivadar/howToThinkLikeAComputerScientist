# 7. Jelenleg pontosan 14 óra van. Beállítunk egy ébresztőórát úgy, hogy 51 órával később csörögjön. Hány órakor fog az ébresztőóra megszólalni? (Segítség: Ha túlzottan vonz a lehetőség, hogy az ujjaidon számold ki, akkor 51 helyett dolgozz 5100-zal.)

actual_hour: int = 14
plus_hour: int = 51

wake_hour: int = (plus_hour - (24 - actual_hour)) % 24

print(wake_hour)
