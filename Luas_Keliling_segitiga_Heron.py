sisi1 = float(input("Tentukan sisi pertama : "))
sisi2 = float(input("Tentukan sisi ke-dua : "))
sisi3 = float(input("Tentukan sisi ke-tiga : "))

P = sisi1 + sisi2 + sisi3
S = P / 2
L = (S*(S-sisi1)*(S-sisi2)*(S-sisi3))**0.5

print("Keliling segitiga adalah ", P, "dan  luas segitiga adalah ", L)