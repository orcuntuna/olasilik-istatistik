adet = int(input("Adet giriniz: "))
dizi = []
bulunanlar = []
toplam = 0

for i in range(adet):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for x in range(len(dizi)):
    sayi = dizi[x]
    tekrar = 0
    for y in range(len(dizi)):
        sayi2 = dizi[y]
        if(sayi == sayi2):
            tekrar += 1
    if sayi not in bulunanlar:
        bulunanlar.append(sayi)
        print(str(sayi) + " - "  + str(tekrar))
        toplam += tekrar

print("Toplam frekans: " + str(toplam))
print(bulunanlar)