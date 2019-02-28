def faktoriyel(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *= i
    return sonuc

n = int(input("Eleman sayısı giriniz (n): "))
r = int(input("Seçim sayısı giriniz (r): "))

faktoriyel = faktoriyel(n) / ( faktoriyel(r) * faktoriyel(n-r) )
print("Faktoriyel: ", str(faktoriyel))