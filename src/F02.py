# F02 - Login User
import F01
import B01

def login():
    global p_nama
    global p_lahir
    global p_tinggi
    global p_username
    global p_role
    global p_saldo
    global p_status

    found = False
    Admin = False

    # Melakukan validasi berulang sampai input sesuai dengan data user
    while (found == False):
        Username = str(input("Masukkan username: "))
        Password = str(input("Masukkan password: "))

        # Melakukan pengecekan kesesuaian data user
        for i in range(F01.panjang_user):
            if (Username == F01.user_new[i][3]):
                if (B01.check(F01.user_new[i][4], Password)):

                    # Menyimpan data user yang sedang login ke dalam variabel
                    p_nama = F01.user_new[i][0]
                    p_lahir = F01.user_new[i][1]
                    p_tinggi = F01.user_new[i][2]
                    p_username = F01.user_new[i][3]
                    p_role = F01.user_new[i][5]
                    p_saldo = int(F01.user_new[i][6])
                    p_status = F01.user_new[i][7]
                    found = True
                    break
                
        if (found == True):
            print()
            print("Selamat bersenang-senang,",p_nama+"!")
            
        elif (found == False):
            print()
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
