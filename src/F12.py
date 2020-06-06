# F12 - Menambahkan Wahana Baru
import F01

def tambah_wahana():
    global panjang_wahana
    global wahana_new

    # Memasukan data wahana baru ke array
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    F01.wahana_new[F01.panjang_wahana][0] = input("Masukkan ID Wahana: ")
    F01.wahana_new[F01.panjang_wahana][1] = input("Masukkan Nama Wahana: ")
    F01.wahana_new[F01.panjang_wahana][2] = input("Masukkan Harga Tiket: ")
    F01.wahana_new[F01.panjang_wahana][3] = input("Batasan umur: ")
    F01.wahana_new[F01.panjang_wahana][4] = input("Batasan tinggi badan: ")
    print()
    print("Info wahana telah ditambahkan!")

    F01.panjang_wahana = F01.panjang_wahana+1
