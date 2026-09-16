# Latihan 3: Kelulusan Bersyarat (Nilai & Kehadiran)
nilai = float(input("Masukkan nilai akhir (0-100): "))
kehadiran = float(input("Masukkan persentase kehadiran (0-100): "))

if nilai >= 60 and kehadiran >= 80:
    print("Selamat, Anda DILATIKAN LULUS!")
else:
    print("Maaf, Anda BELUM LULUS. Periksa nilai atau kehadiran Anda.")