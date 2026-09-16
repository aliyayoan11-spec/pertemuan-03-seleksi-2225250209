print("==========================================")
print("   ANALISIS PERSAMAAN KUADRAT (ax^2+bx+c) ")
print("==========================================")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("\n[ERROR] Nilai 'a' tidak boleh 0! Ini bukan persamaan kuadrat.")
else:
    # Hitung Diskriminan D = b^2 - 4ac
    D = (b ** 2) - (4 * a * c)
    print(f"\nNilai Diskriminan (D) = {D:.2f}")

    if D > 0:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b - (D ** 0.5)) / (2 * a)
        print("Sifat Akar : Memiliki 2 Akar Real Berbeda")
        print(f"Akar x1    : {x1:.2f}")
        print(f"Akar x2    : {x2:.2f}")
    elif D == 0:
        x = -b / (2 * a)
        print("Sifat Akar : Memiliki 1 Akar Real Kembar")
        print(f"Akar x     : {x:.2f}")
    else:
        print("Sifat Akar : Tidak Memiliki Akar Real (Akar Imajiner / Kompleks)")