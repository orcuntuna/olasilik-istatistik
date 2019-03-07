adet = int(input("Adet giriniz: "))
dizi = []
toplamlar = 0

for i in range(adet):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for x in range(adet):
    sayi = dizi[x]
    toplamlar += sayi

aritmatik_ort = toplamlar / adet

ust = 0
for i in dizi:
    ust += (aritmatik_ort-i) ** 2

sonuc = (ust/(adet-1)) ** (1/2)
