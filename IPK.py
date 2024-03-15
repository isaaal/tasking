Algoritma= float(input("MAsukan Nilai Algoritma: "))
sksAlgo = int(input("Masukan sks algoritma :"))

PerancanganObjek= float(input("MAsukan Nilai Perancangan objek: "))
sksPO =int(input("Masukan sks Perancangan objek :"))

Kalkulus= float(input("MAsukan Nilai Kalkulus : "))
sksKalkulus = int(input("Masukan sks kalkulus :"))

EtikaProfesi= float(input("MAsukan Nilai Etika profesi: "))
sksEF = int(input("Masukan sks Etika profesi : "))

DataBase= float(input("MAsukan Nilai Data base: "))
sksDB =int(input("Masukan sks data base : "))

Inggris1= float(input("MAsukan Nilai Inggris: ") )
sksEng = int(input("Masukan sks Inggris"))

def Klasiafikasi_Nilai (nilai, sks):
    if nilai <30:
        return 0
    elif nilai <=34:
        return 1 * sks
    elif nilai <= 39:
        return 1.25  * sks
    elif nilai <= 44:
        return 1.5 * sks
    elif nilai <= 49:
        return 1.75  * sks
    elif nilai <= 54:
        return 2 * sks
    elif nilai <= 59:
        return 2.25 * sks
    elif nilai <= 64:
        return 2.5  * sks
    elif nilai <= 69:
        return 2.75 * sks
    elif nilai <= 74:
        return 3  * sks
    elif nilai <= 79:
        return 3.25  * sks
    elif nilai <= 84:
        return 3.5  * sks
    elif nilai <= 89:
        return 3.75  * sks
    else:
        return 4 * sks


hasila = Klasiafikasi_Nilai(Algoritma, sksAlgo) 
hasilb = Klasiafikasi_Nilai(PerancanganObjek, sksPO) 
hasilc = Klasiafikasi_Nilai(Kalkulus, sksKalkulus) 
hasild = Klasiafikasi_Nilai(EtikaProfesi, sksEF) 
hasile = Klasiafikasi_Nilai(DataBase, sksDB) 
hasilf = Klasiafikasi_Nilai(Inggris1, sksEng) 

print("Nilai Algoritma =" ,hasila)
print("Nilai Perancangan Objek =",hasilb)
print("Nilai Kalkulus =",hasilc)
print("Nilai Etika Profesi =",hasild)
print("Nilai Data Base",hasile)
print("Nilai Inggris =",hasilf)

ip = (hasila + hasilb + hasilc + hasild + hasile + hasilf)/(sksAlgo+sksEng+sksDB+sksEF+sksKalkulus+sksPO)
print("Nilai IP anda =", ip)