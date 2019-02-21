import random

N = int(input("N giriniz: "))
n = int(input("n giriniz: "))
k = N//n
dizi = []

rasgele = random.randint(1,k)
dizi.append(rasgele)
son = rasgele

for i in range(n-1):
    dizi.append(son + k)
    son += k

print(dizi)