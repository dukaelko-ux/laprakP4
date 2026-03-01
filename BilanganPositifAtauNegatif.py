try:
    bilangan = int(input("Masukkan suatu bilangan: "))

    if bilangan > 0:
        print("Bilangan positif.")
    elif bilangan < 0:
        print("Bilangan negatif.")
    else:
        print("Bilangan nol.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")
