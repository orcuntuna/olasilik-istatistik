adet = int(input("Adet giriniz: "))
dizi = []
carpim = 1

for i in range(adet):
    sayi = int(input(str(i+1) + ". sayi: "))
    dizi.append(sayi)
    carpim *= sayi

kok = carpim ** (1/2)

print("Geometrik ortalama: ", round(kok,3))