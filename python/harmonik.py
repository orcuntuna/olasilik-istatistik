adet = int(input("Adet giriniz: "))
dizi = []

for i in range(adet):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

toplamlar = 0

for sayi in dizi:
    toplamlar += 1 / sayi

sonuc = adet / toplamlar
print(sonuc)