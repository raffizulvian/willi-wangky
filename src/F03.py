# F03 - SAVE
import csv
import F01

def save():

    # Melakukan penyimpanan data user ke file csv
    nama_user = input("Masukkan nama File User: ")
    User = open(nama_user,'w',newline='')
    writer = csv.writer(User,delimiter=',')
    for i in range(F01.panjang_user+1):
        if (F01.user_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.user_new[i])
    User.close()

    # Melakukan penyimpanan data wahana ke file csv
    nama_wahana = input("Masukkan nama File Daftar Wahana: ")
    Wahana = open(nama_wahana,'w',newline='')
    writer = csv.writer(Wahana,delimiter=',')
    for i in range(F01.panjang_wahana+1):
        if (F01.wahana_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.wahana_new[i])
    Wahana.close()

    # Melakukan penyimpanan data pembelian ke file csv
    nama_beli = input("Masukkan nama File Pembelian Tiket: ")
    Beli = open(nama_beli,'w',newline='')
    writer = csv.writer(Beli,delimiter=',')
    for i in range(F01.panjang_beli+1):
        if (F01.beli_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.beli_new[i])
    Beli.close()

    # Melakukan penyimpanan data penggunaan tiket ke file csv
    nama_guna = input("Masukkan nama File Penggunaan Tiket: ")
    Guna = open(nama_guna,'w',newline='')
    writer = csv.writer(Guna,delimiter=',')
    for i in range(F01.panjang_guna+1):
        if (F01.guna_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.guna_new[i])
    Guna.close()

    # Melakukan penyimpanan data kepemilikan tiket ke file csv
    nama_milik = input("Masukkan nama File Kepemilikan Tiket: ")
    Milik = open(nama_milik,'w',newline='')
    writer = csv.writer(Milik,delimiter=',')
    for i in range(F01.panjang_milik+1):
        if (F01.milik_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.milik_new[i])
    Milik.close()

    # Melakukan penyimpanan data refund ke file csv
    nama_refund = input("Masukkan nama File Refund Tiket: ")
    Refund = open(nama_refund,'w',newline='')
    writer = csv.writer(Refund,delimiter=',')
    for i in range(F01.panjang_refund+1):
        if (F01.refund_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.refund_new[i])
    Refund.close()

    # Melakukan penyimpanan data kritik dan saran ke file csv
    nama_ks = input("Masukkan nama File Kritik dan Saran: ")
    Ks = open(nama_ks,'w',newline='')
    writer = csv.writer(Ks,delimiter=',')
    for i in range(F01.panjang_ks+1):
        if (F01.ks_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.ks_new[i])
    Ks.close()

    # Melakukan penyimpanan data kehilangan ke file csv
    nama_hilang = input("Masukkan nama File Kehilangan Tiket: ")
    Hilang = open(nama_hilang,'w',newline='')
    writer = csv.writer(Hilang,delimiter=',')
    for i in range(F01.panjang_hilang+1):
        if (F01.hilang_new[i][0] == '*'):
            continue
        else:
            writer.writerow(F01.hilang_new[i])
    Hilang.close()

    print()
    print("Data berhasil disimpan!")
    print()
