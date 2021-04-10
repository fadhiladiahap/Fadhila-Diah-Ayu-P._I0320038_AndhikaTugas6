angka = []
total= 0

banyak = int(input("Masukkan banyak bilangan: "))

for a in range (0,banyak):
    temp = int(input("Masukkan nilai ke-%d: "%(a+1)))
    angka.append(temp)
    total += angka[a]
    rata_bilangan = total/banyak
print("Rata-rata",banyak,"bilangannya adalah",round(rata_bilangan,2))