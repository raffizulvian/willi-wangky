# F01 - LOAD
import csv
from panjangData import panjangData

def load():
    global user_new
    global wahana_new
    global beli_new
    global guna_new
    global milik_new
    global refund_new
    global ks_new
    global hilang_new

    global panjang_user
    global panjang_wahana
    global panjang_beli
    global panjang_guna
    global panjang_milik
    global panjang_refund
    global panjang_ks
    global panjang_hilang

    # Melakukan loading file data user dan menyimpan dalam array
    nama_user = input("Masukkan nama File User: ")
    User = open(nama_user,'r')
    reader = csv.reader(User,delimiter=',')
    listreader = list(reader)
    User.close()
    user_old = listreader
    panjang_user = panjangData(nama_user)
    user_new = [['*' for i in range(8)] for j in range(1000000)]
    for j in range(panjang_user):
        for i in range(8):
            user_new[j][i] = user_old[j][i]

    # Melakukan loading file data wahana dan menyimpan dalam array
    nama_wahana = input("Masukkan nama File Daftar Wahana: ")
    Wahana = open(nama_wahana,'r')
    reader = csv.reader(Wahana,delimiter=',')
    listreader = list(reader)
    Wahana.close()
    wahana_old = listreader
    panjang_wahana = panjangData(nama_wahana)
    wahana_new = [['*' for i in range(5)] for j in range(1000000)]
    for j in range(panjang_wahana):
        for i in range(5):
            wahana_new[j][i] = wahana_old[j][i]

    # Melakukan loading file data pembelian dan menyimpan dalam array
    nama_beli = input("Masukkan nama File Pembelian Tiket: ")
    Beli = open(nama_beli,'r')
    reader = csv.reader(Beli,delimiter=',')
    listreader = list(reader)
    Beli.close()
    beli_old = listreader
    panjang_beli = panjangData(nama_beli)
    beli_new = [['*' for i in range(4)] for j in range(1000000)]
    for j in range(panjang_beli):
        for i in range(4):
            beli_new[j][i] = beli_old[j][i]

    # Melakukan loading file data penggunaan tiket dan menyimpan dalam array
    nama_guna = input("Masukkan nama File Penggunaan Tiket: ")
    Guna = open(nama_guna,'r')
    reader = csv.reader(Guna,delimiter=',')
    listreader = list(reader)
    Guna.close()
    guna_old = listreader
    panjang_guna = panjangData(nama_guna)
    guna_new = [['*' for i in range(4)] for j in range(1000000)]
    for j in range(panjang_guna):
        for i in range(4):
            guna_new[j][i] = guna_old[j][i]

    # Melakukan loading file data kepemilikan tiket dan menyimpan dalam array
    nama_milik = input("Masukkan nama File Kepemilikan Tiket: ")
    Milik = open(nama_milik,'r')
    reader = csv.reader(Milik,delimiter=',')
    listreader = list(reader)
    Milik.close()
    milik_old = listreader
    panjang_milik = panjangData(nama_milik)
    milik_new = [['*' for i in range(3)] for j in range(1000000)]
    for j in range(panjang_milik):
        for i in range(3):
            milik_new[j][i] = milik_old[j][i]

    # Melakukan loading file data refund dan menyimpan dalam array
    nama_refund = input("Masukkan nama File Refund Tiket: ")
    Refund = open(nama_refund,'r')
    reader = csv.reader(Refund,delimiter=',')
    listreader = list(reader)
    Refund.close()
    refund_old = listreader
    panjang_refund = panjangData(nama_refund)
    refund_new = [['*' for i in range(4)] for j in range(1000000)]
    for j in range(panjang_refund):
        for i in range(4):
            refund_new[j][i] = refund_old[j][i]

    # Melakukan loading file data kritik saran dan menyimpan dalam array
    nama_ks = input("Masukkan nama File Kritik dan Saran: ")
    Ks = open(nama_ks,'r')
    reader = csv.reader(Ks,delimiter=',')
    listreader = list(reader)
    Ks.close()
    ks_old = listreader
    panjang_ks = panjangData(nama_ks)
    ks_new = [['*' for i in range(4)] for j in range(1000000)]
    for j in range(panjang_ks):
        for i in range(4):
            ks_new[j][i] = ks_old[j][i]

    # Melakukan loading file data kehilangan dan menyimpan dalam array
    nama_hilang = input("Masukkan nama File Kehilangan Tiket: ")
    Hilang = open(nama_hilang,'r')
    reader = csv.reader(Hilang,delimiter=',')
    listreader = list(reader)
    Hilang.close()
    hilang_old = listreader
    panjang_hilang = panjangData(nama_hilang)
    hilang_new = [['*' for i in range(4)] for j in range(1000000)]
    for j in range(panjang_hilang):
        for i in range(4):
            hilang_new[j][i] = hilang_old[j][i]
            
    print()
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
