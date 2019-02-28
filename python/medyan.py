adet = int(input("Adet giriniz: "))
dizi = []

for i in range(adet):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for i in range(len(dizi)-1):
    for j in range(len(dizi)-1):
        if(dizi[j] > dizi[j+1]):
            temp = dizi[j]
            dizi[j] = dizi[j+1]
            dizi[j+1] = temp

if len(dizi)%2 == 1:
    orta = (len(dizi) + 1) / 2
    print(orta)
    print("Medyan eleman: ", dizi[int(orta)])
else:
    orta = int(len(dizi) / 2) - 1
    sonuc = (dizi[orta] + dizi[orta+1]) / 2
    print("Medyan eleman: ", sonuc)
  