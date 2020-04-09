vaka = [10827, 13531, 15679, 18315, 20921, 23934, 27069, 30217, 34109, 38226]
n = len(vaka)
xtoplam = 0
ytoplam = sum(vaka)
xiyitoplam = 0
xikaretoplam = 0
yortalama = sum(vaka)/n
tstandartsapma = 0
shatatahmini = 0

for i in range(n):
    xtoplam += i + 1
    xiyitoplam += (i+1)*vaka[i]
    xikaretoplam += (i+1)*(i+1)

xortalama = xtoplam / n
a1 = (n*xiyitoplam-xtoplam*ytoplam)/(n*xikaretoplam-xtoplam**2)
a0 = (ytoplam-a1*xtoplam)/n

for i in range(n):
    tstandartsapma += (vaka[i]-yortalama)**2
    shatatahmini += vaka[i] - a0 - a1*(i+1)

print("ao= ", a0, ", a1= ", a1)

for i in range(n):
    print(vaka[i], a0+a1*(i+1))
