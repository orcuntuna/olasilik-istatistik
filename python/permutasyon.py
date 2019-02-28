def faktoriyel(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *= i
    return sonuc

n = int(input("Eleman sayısı giriniz (n): "))
r = int(input("Seçim sayısı giriniz (r): "))

permutasyon = faktoriyel(n) / faktoriyel(n-r)
print("Permutasyon: ", str(permutasyon))