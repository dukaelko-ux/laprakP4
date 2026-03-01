try:
    bulan = int(input("Masukkan bulan (1-12): "))

    hari_per_bulan = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if 1 <= bulan <= 12:
        print(f"Jumlah hari: {hari_per_bulan[bulan]}")
    else:
        print("Bulan tidak valid! Masukkan angka antara 1 hingga 12.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat antara 1 hingga 12.")
