total_uang = int(input("Masukan Jumlah Uang Anda: "))
total_belanjaan = int (input("Masukan Jumlah Belanjaan anda: "))
total = total_belanjaan - diskon
kembalian = total_uang - total
if total_belanjaan >= 60000:
    diskon = 10000
else:
    diskon=0
print("Uang anda: %i , Total belanjaan Anda: %i , Diskon: %i, Kembalian:%i"%(total_uang, total_belanjaan, diskon, kembalian))