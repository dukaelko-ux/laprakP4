try:
    bilangan = int(input("Masukkan suatu bilangan: "))

    hasil = "Bilangan positif." if bilangan > 0 else "Bilangan negatif." if bilangan < 0 else "Bilangan nol."

    print(hasil)

except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")
