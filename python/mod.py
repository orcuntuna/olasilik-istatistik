adet = int(input("Adet giriniz: "))
dizi = []
dizi2 = []

for i in range(adet):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for i in range(len(dizi)-1):
    for j in range(len(dizi)-1):
        if(dizi[j] > dizi[j+1]):
            temp = dizi[j]
            dizi[j] = dizi[j+1]
            dizi[j+1] = temp


maks = -1

for i in range(adet):

    if i-1 == adet:
        sonraki = dizi[i+1]
    else:
        sonraki = None

    if(dizi[i] != sonraki):
        if(maks == dizi.count(dizi[i])):
            dizi2.append(dizi[i])
        elif(maks < dizi.count(dizi[i])):
            dizi2.clear()
            dizi2.append(dizi[i])
            maks = dizi.count(dizi[i])

dizi2 = list(set(dizi2))
print(dizi2)