# F13 - Top Up Saldo
import F01

def topup() :
    global panjang_user
    global user_new

    username = input("Masukkan username: ")
    topup = int(input("Masukkan saldo yang ingin di-top up: "))

    # Melakukan pengecekan data user
    for i in range(F01.panjang_user+1) :
        if (username == F01.user_new[i][3]):

            # Menambahkan saldo user
            F01.user_new[i][6] = str(int(F01.user_new[i][6]) + topup)
            print()
            print("Top up berhasil. Saldo",F01.user_new[i][0],"bertambah menjadi",F01.user_new[i][6])
            
