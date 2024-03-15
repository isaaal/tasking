pilihan1 = str(input("Masukan pilihan anda : "))
pilihan2 = str(input("Masukan pilihan anda : "))

A = "kertas"
B = "gunting"
C = "batu"

if pilihan1 == A and pilihan2 == B:
    print(B, " menang dari ", A)
elif pilihan1 == B and pilihan2 == C:
    print(C, " menang dari ", B)
elif pilihan1 == C and pilihan2 == A:
    print(A, " menang dari ", C)
elif pilihan1 == B and pilihan2 == A:
    print(A, " menang dari ", B)
elif pilihan1 == C and pilihan2 == B:
    print(B, " menang dari ", C)
elif pilihan1 == A and pilihan2 == C:
    print(C, " menang dari ", A)
else:
    print("seri")