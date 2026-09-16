# Latihan 2: Membandingkan Dua Bilangan
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if a > b:
    print(f"{a} lebih besar dari {b}")
elif b > a:
    print(f"{b} lebih besar dari {a}")
else:
    print("Kedua angka bernilai SAMA")