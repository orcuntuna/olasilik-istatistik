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

alt_ceyreklik_n = n / len(alt_sinirlar)

for i in range(len(alt_sinirlar)):
    if sinif_eklenik_frekanslari[i] >= alt_ceyreklik_n:
        alt_ceyreklik_sinif = i
        break

alt_ceyreklik_j = 0

if alt_ceyreklik_sinif > 0:
    for i in range(alt_ceyreklik_sinif):
        alt_ceyreklik_j += sinif_frekanslari[i]

alt_ceyreklik_j = alt_ceyreklik_n - alt_ceyreklik_j

alt_ceyreklik_fq = sinif_frekanslari[alt_ceyreklik_sinif]
alt_ceyreklik_alt_sinir = sinif_alt_sinirlar[alt_ceyreklik_sinif]

alt_ceyreklik = alt_ceyreklik_alt_sinir + ((alt_ceyreklik_j*h)/alt_ceyreklik_fq)

ust_ceyreklik_n = 3 * alt_ceyreklik_n

for i in range(len(alt_sinirlar)):
    if sinif_eklenik_frekanslari[i] >= ust_ceyreklik_n:
        ust_ceyreklik_sinif = i
        break

ust_ceyreklik_j = 0

if ust_ceyreklik_sinif > 0:
    for i in range(ust_ceyreklik_sinif):
        ust_ceyreklik_j += sinif_frekanslari[i]


ust_ceyreklik_j = ust_ceyreklik_n - ust_ceyreklik_j

ust_ceyreklik_fq = sinif_frekanslari[ust_ceyreklik_sinif]
ust_ceyreklik_alt_sinir = sinif_alt_sinirlar[ust_ceyreklik_sinif]


ust_ceyreklik = ust_ceyreklik_alt_sinir + ((ust_ceyreklik_j*h)/ust_ceyreklik_fq)

# çıktı

for i in range(len(alt_sinirlar)):
    print( str(alt_sinirlar[i]) + " - " + str(ust_sinirlar[i]) + "\t" + str(frekanslar[i]) + "\t" + str(sinif_alt_sinirlar[i]) + " - " + str(sinif_ust_sinirlar[i]) + "\t" + str(sinif_frekanslari[i]) + "\t" + str(sinif_orta_noktalar[i]) + "\t" + str(sinif_eklenik_frekanslari[i]) + "\t" + str(sinif_oransal_frekanslari[i]) + "\t" + str(sinif_eklenik_oransal_frekanslari[i]))

print("\n")

print("Alt çeyreklik (Q1): " + str(alt_ceyreklik))
print("Üst çeyreklik (Q3): " + str(ust_ceyreklik))

