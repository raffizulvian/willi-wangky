# F04 - Sign Up
import F01
import F02
import B01

def signup():
    global panjang_user
    global user_new

    # Menambahkan data baru user ke array user
    F01.user_new[F01.panjang_user][0] = str(input("Masukkan nama pemain: "))
    F01.user_new[F01.panjang_user][1] = str(input("Masukkan tanggal lahir pemain (DD/MM/YYYY): "))
    F01.user_new[F01.panjang_user][2] = str(input("Masukkan tinggi badan pemain (cm): "))
    username = str(input("Masukkan username pemain: "))

    # Melakukan validasi terhadap username yang didaftarkan
    #Asumsi user tidak akan memasukkan username yang sama berulang kali
    for i in range(F01.panjang_user+1):
        if (username == F01.user_new[i][3]):
            print("Username sudah digunakan. Silahkan coba username yang lain.")
            username = str(input("Masukkan username pemain: "))

    # Menambahkan data baru user ke array user        
    F01.user_new[F01.panjang_user][3] = username                
    F01.user_new[F01.panjang_user][4] = B01.hash(str(input("Masukkan password pemain: ")))
    F01.user_new[F01.panjang_user][5] = "Pemain"
    F01.user_new[F01.panjang_user][6] = "0"
    print()
    print("Selamat menjadi pemain,",F01.user_new[F01.panjang_user][0]+". Selamat bermain.")
    
    F01.panjang_user = F01.panjang_user+1
