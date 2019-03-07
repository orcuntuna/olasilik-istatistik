adet = int(input("Adet giriniz: "))
carpim = 1

for i in range(adet):
    sayi = int(input(str(i+1) + ". sayi: "))
    carpim *= sayi

kok = carpim ** (1.0/adet)
print(carpim)

print("Geometrik ortalama: ", round(kok,3))