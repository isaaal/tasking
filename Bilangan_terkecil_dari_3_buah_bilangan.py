nilai1 = int(input("Masukan nilai satu :"))   
nilai2 = int(input("Masukan nilai dua :"))   
nilai3 = int(input("Masukan nilai tiga :"))   

if nilai1 < nilai2 and nilai1 < nilai3:
    print(nilai1," Lebih kecil dari ", nilai2, " dan ", nilai3)
elif nilai2 < nilai1 and nilai2 < nilai3 :
    print(nilai2, " Lebih beasr dari ", nilai1, " dan ", nilai3) 
elif nilai3< nilai1 and nilai3 < nilai2:
   print(nilai3, " Lebih kecil dari ", nilai1, " dan ", nilai2)
else:
    print(nilai1 , nilai2, nilai3, " sama besar")