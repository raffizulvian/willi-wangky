# F15 - Melihat Jumlah Tiket Pemain
import F01

def tiket_pemain():
    global panjang_milik
    global panjang_wahana

    username = input("Masukkan username: ")

    # Mencetak seluruh riwayat pemain yang username nay diminta
    print("Riwayat:")
    for i in range(F01.panjang_milik+1):
        if (username == F01.milik_new[i][0]):
            for j in range(F01.panjang_wahana+1):
                if (F01.milik_new[i][1] == F01.wahana_new[j][0]):
                    print(F01.milik_new[i][1],F01.wahana_new[j][1],F01.milik_new[i][2], sep=' | ')
                    break
