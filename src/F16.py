# F16 - Exit
import F02
import F03

def exit():
    global p_nama
    global p_lahir
    global p_tinggi
    global p_username
    global p_role
    global p_saldo
    global p_status

    F02.p_nama = ''
    F02.p_lahir = ''
    F02.p_tinggi = ''
    F02.p_username = ''
    F02.p_role = ''
    F02.p_saldo = ''
    F02.p_status = ''

    # Menanyakan pengguna apakah akan melakukan save data baru kemudian kembali ke halaman login
    value = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")
    if (value == 'Y'):
        print()
        F03.save()
        F02.login()

    # Langsung kembali ke halaman login
    else:
        print()
        F02.login()
