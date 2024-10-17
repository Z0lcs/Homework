import random
veletlen_szam = random.randint(1, 12)
numbers_szama = 0
harom_szam = 0

while numbers_szama != 20:
    veletlen_szam = random.randint(1, 12)
    numbers_szama += 1
    if veletlen_szam % 3 == 0:
        print(veletlen_szam)
        harom_szam += 1
print(str(harom_szam) + " darab szám osztható 3-mal!")
