import random

min = int(input("Minimum deger: "))
max = int(input("Maximum deger: "))
adet = int(input("Adet: "))
dizi = []

if(min < max):
    if(max-min > adet):
        while len(dizi) < adet:
            sayi = random.randint(min,max)
            if(sayi not in dizi):
                dizi.append(sayi)
    else:
        while len(dizi) < adet:
            sayi = random.randint(min,max)
            dizi.append(sayi)

print(dizi)