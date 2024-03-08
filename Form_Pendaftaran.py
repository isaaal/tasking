nama = str(input("Nama :"))
TmptL = str(input("Tempat lahir :"))
TgL = int(input("Tanggal Lahir :"))
ThnL = int(input("Tahun Lahir :"))
jenis = str(input("Gender :"))
inggris = int(input("Nilai Inggris :"))
mtk = int(input("Nilai Matematika :"))
indo = int(input("Nilai B.Indonesia :"))

rata= (inggris + indo + mtk)/3          #menghitung nilai rata-rata 
umur = 2024 - ThnL                      #menentukan umur 
gender = jenis.lower                    #agar inputan menjadi huruf kecil/bukan huruf kapital
gender == "laki-laki" or "perempuan"    

if rata >=80 and gender and umur>=25:
    jurusan = "Teknik Informatika"
elif rata >= 80 and gender and umur>=25:
    jurusan = "Sistem Operasi"
elif umur >=25:
    jurusan = "DKV"
else:
    jurusan ="Maaf anda tidak di terima"

print("Nama : ",nama)
print("TTL : ",TmptL, TgL, ThnL)
print("Gender :",jenis)
print("Nilai Rata-rata anda :",rata)
print("Rekomendasi untuk anda :",jurusan)