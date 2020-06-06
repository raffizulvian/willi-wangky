# F10 - Kritik dan Saran
import F01
import F02

def kritik_saran():
    global panjang_ks
    global ks_new

    # Membaca input dari user sesuai spesifikasi
    id = input("Masukkan ID wahana: ")
    date = input("Masukkan tanggal pelaporan: ")
    kritik_saran = input("Kritik/saran Anda: ")

    # Asumsi ID wahana dan tanggal valid
    # Melakukan penambahan data kritik dan saran
    for i in range(F01.panjang_ks+1):
        if (F01.ks_new[i][0] == '*'):
            F01.ks_new[i][0] = F02.p_username
            F01.ks_new[i][1] = date
            F01.ks_new[i][2] = id
            F01.ks_new[i][3] = kritik_saran
            F01.panjang_ks += 1
            break
    print()
    print("Kritik dan saran Anda kami terima.")
    
