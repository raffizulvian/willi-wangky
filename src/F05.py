# F05 - Pencarian Pemain
import F01

def cari_pemain():
    pemain = str(input("Masukkan username: "))
    found = False

    # Melakukan pengecekan terhadap data user
    for i in range(F01.panjang_user+1):
        if (pemain == F01.user_new[i][3]):
            Nama = F01.user_new[i][0]
            Tinggi = F01.user_new[i][2]
            Tanggal = F01.user_new[i][1]
            found = True
            break

    # Menampilkan data yang dicari    
    if (found == True):
        print("Nama Pemain:",Nama)
        print("Tinggi Pemain:",Tinggi,"cm")
        print("Tanggal Lahir Pemain:",Tanggal)
        
    elif (found == False):
        print("Username yang anda masukkan tidak terdaftar sebagai pemain.")
