sayi = int(input("Olasılık sayısı: "))
olasilik = 0

olmaOlasiligi = []
olmamaOlasiligi = []
bayes = []

for i in range(sayi):
    veri1 = float(input("A" + str(i) + " : olayının olma olasılığı: "))
    veri2 = float(input("A" + str(i) + "/B : olayının olma olasılığı: "))
    olmaOlasiligi.append(veri1)
    olmamaOlasiligi.append(veri2)

for i in range(sayi):
    olasilik += olmaOlasiligi[i] * olmamaOlasiligi[i]

for i in range(sayi):
    bayes.append((olmaOlasiligi[i] * olmamaOlasiligi[i]) / olasilik)

print("Toplam olasılık: " + str(olasilik))

for i in range(sayi):
    print("Bayes (A"+ str(i) + "): " + str(bayes[i]))