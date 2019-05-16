import math

#adet = int(input("Adet giriniz: "))
dizi = [145,150,155,170,175,200,205,210,210,235]

#for i in range(adet):
#    dizi.append(int(input(str(i+1) + ". sayi: ")))

n = len(dizi)
R = max(dizi) - min(dizi)
k = math.ceil(n ** (1/2))
h = math.ceil(R / k)

alt_sinirlar = []
ust_sinirlar = []

alt_sinirlar.append(min(dizi))
ust_sinirlar.append(alt_sinirlar[0] + (h-1))

for i in range(k):
    if i != 0:
        son_eleman = alt_sinirlar[len(alt_sinirlar)-1]
        yeni_eleman = son_eleman + h
        alt_sinirlar.append(yeni_eleman)
        ust_sinirlar.append(yeni_eleman + (h-1))

frekanslar = []

for i in range(len(alt_sinirlar)):
    frekans = 0
    for x in (dizi):
        if x >= alt_sinirlar[i] and x < ust_sinirlar[i]:
            frekans += 1
    frekanslar.append(frekans)


sinif_alt_sinirlar = []
sinif_ust_sinirlar = []

for i in range(len(alt_sinirlar)):
    sinif_alt_sinirlar.append(alt_sinirlar[i] - 0.5)
    sinif_ust_sinirlar.append(ust_sinirlar[i] + 0.5)

sinif_degerleri = []

for i in range(len(alt_sinirlar)):
    sinif_degerleri.append((sinif_alt_sinirlar[i] + sinif_ust_sinirlar[i]) / 2)


sinif_frekanslari = []

for i in range(len(alt_sinirlar)):
    frekans = 0
    for x in (dizi):
        if x >= sinif_alt_sinirlar[i] and x < sinif_ust_sinirlar[i]:
            frekans += 1
    sinif_frekanslari.append(frekans)


sinif_orta_noktalar = []

for i in range(len(alt_sinirlar)):
    sinif_orta_noktalar.append((sinif_alt_sinirlar[i] + sinif_ust_sinirlar[i]) / 2)

sinif_eklenik_frekanslari = []
eklenik_temp = 0

for i in range(len(alt_sinirlar)):
    eklenik_temp += sinif_frekanslari[i]
    sinif_eklenik_frekanslari.append(eklenik_temp)

sinif_oransal_frekanslari = []

for i in range(len(alt_sinirlar)):
    sinif_oransal_frekanslari.append(sinif_frekanslari[i] / len(dizi))

sinif_eklenik_oransal_frekanslari = []

for i in range(len(alt_sinirlar)):
    sinif_eklenik_oransal_frekanslari.append(sinif_eklenik_frekanslari[i] / len(dizi))

# çıktı

for i in range(len(alt_sinirlar)):
    print( str(alt_sinirlar[i]) + " - " + str(ust_sinirlar[i]) + "\t" + str(frekanslar[i]) + "\t" + str(sinif_alt_sinirlar[i]) + " - " + str(sinif_ust_sinirlar[i]) + "\t" + str(sinif_frekanslari[i]) + "\t" + str(sinif_orta_noktalar[i]) + "\t" + str(sinif_eklenik_frekanslari[i]) + "\t" + str(sinif_oransal_frekanslari[i]) + "\t" + str(sinif_eklenik_oransal_frekanslari[i]))


