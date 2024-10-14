szam = int(input("Adj meg egy számot! "))

if szam % 3 == 0 and szam % 4 == 0:
     print("3-mal és 4-gyel osztható a szám!")
elif szam % 3 == 0:
     print("3-mal osztható a szám!")
elif szam % 4 == 0:
     print("4-gyel osztható a szám!")
else:
    print("sem 3-mal, sem 4-gyel nem osztható!")