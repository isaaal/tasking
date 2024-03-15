nilai = int(input("masukan nilai 1 :"))

if nilai < 0:
    hasil = "Bilangan Negatif"
elif nilai > 0:
    hasil = "Bilangan Positif"
else:
    hasil = "Bilangan Netral"
print(nilai, hasil)