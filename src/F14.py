# F14 - Melihat Riwayat Penggunaan Wahana
import F01

def riwayat_wahana():
    global panjang_guna
    
    ID_Wahana = input("Masukkan ID Wahana: ")

    # Mencetak seluruh riwayat dari wahana yang ID nya diminta
    print("Riwayat: ")
    for i in range(F01.panjang_guna+1):
        while (ID_Wahana == F01.guna_new[i][2]):
            print(F01.guna_new[i][1],F01.guna_new[i][0],F01.guna_new[i][3], sep=' | ')
            break
