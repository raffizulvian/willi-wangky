# F09 - Refund
import F01
import F02
import F07

def refund() :
    global panjang_milik
    global panjang_wahana
    global panjang_user
    global panjang_refund
    global p_username
    global price
    
    ID = input("Masukkan ID wahana: ")
    date = input("Masukkan Tanggal Refund: ")
    jml_refund = int(input("Jumlah tiket yang di-refund: "))

    # Melakukan pengecekan ke data kepemilikan tiket
    found = 0
    for i in range(F01.panjang_milik+1):
        if (F02.p_username == F01.milik_new[i][0] and ID == F01.milik_new[i][1]):
            if (jml_refund <= int(F01.milik_new[i][2])) :
                F01.refund_new[F01.panjang_refund+1][0] = F02.p_username
                F01.refund_new[F01.panjang_refund+1][1] = date
                F01.refund_new[F01.panjang_refund+1][2] = ID
                F01.refund_new[F01.panjang_refund+1][3] = str(jml_refund)

                F01.milik_new[i][2] = str(int(F01.milik_new[i][2]) - jml_refund)

                # Menambah saldo user sesuai jumlah refund
                for i in range(F01.panjang_user+1):
                    if (F01.user_new[i][3] == F02.p_username):
                         F01.user_new[i][6] = str(int(F01.user_new[i][6]) + int(0.8*F07.price))

                F01.panjang_refund = F01.panjang_refund + 1
                found = 1
                print()
                print("Uang refund sudah kami berikan pada akun Anda.")
            else:
                found = 2
                print()
                print("Anda tidak memiliki tiket terkait.")
    if (found == 0):
        print()
        print("Anda tidak memiliki tiket terkait.")
