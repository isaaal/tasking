bulan = 30
gaji_pokok = 10000000
uang_transport = 100000
uang_makan=50000
lama_lembur = int(input("Lama waktu lembur: "))
if lama_lembur == 1:
   A = 1
   uang = 100000
   elif lama_lembur == 2:
       A = 2
       uang = 100000
       elif lama_lembur > 2:
           A = lama_lembur - 2
           uang = 150000
       else:
           A = 0
           uang = 0
total_lembur = A * uang
total_transport = uang_transport * bulan
total_makan = uang_makan * bulan
honor =gaji_pokok + total_transport + total_makan + total_lembur
print("Gaji pokok: %i, Upah transport:%i/%i, Upah makan:%i/%i, Upah lembur:%i, total upah:%i"%(gaji_pokok, uang_transport, bulan, uang_makan, bulan, total_lembur, honor))