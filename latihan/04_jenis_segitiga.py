# Latihan 4: Menentukan Jenis Segitiga
a = float(input("Masukkan panjang sisi A: "))
b = float(input("Masukkan panjang sisi B: "))
c = float(input("Masukkan panjang sisi C: "))

if a == b == c:
    print("Segitiga Sama Sisi")
elif a == b or b == c or a == c:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")