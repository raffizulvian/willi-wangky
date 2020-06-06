import panjangData
import F01

def upgrade_gold():
    global user_new

    # Membaca input dari user sesuai spesifikasi
    username = input("Masukkan username yang ingin di-upgrade: ")

    # Melakukan pengecekan ke data user
    for i in range(F01.panjang_user):
        if (F01.user_new[i][3] == username and int(F01.user_new[i][6]) >= 200000):

            # Mengurangi jumlah saldo pemain dengan biaya upgrade
            F01.user_new[i][6] = str(int(F01.user_new[i][6]) - 200000)

            # Menandai database user sebagai akun gold
            F01.user_new[i][7] = 'yes'
            
            print("Akun Anda telah diupgrade.")
            break
        elif (F01.user_new[i][3] == username and int(F01.user_new[i][6]) < 200000):
            print("Saldo anda tidak cukup")
            break
