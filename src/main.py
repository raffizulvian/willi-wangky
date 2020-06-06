# Gabungan
import F01
import F02
import F03
import F04
import F05
import F06
import F07
import F08
import F09
import F10
import F11
import F12
import F13
import F14
import F15
import F16
import B02
import B03
import B04


# MAIN PROGRAM

F01.load()

print('''
--------------------------------------------------------
    *Selamat Datang di Taman Bermain Willy Wangky!*
“If you want to view paradise, take around and view it.”
       [ Sudah siapkah kamu bersenang-senang? ]
--------------------------------------------------------
''')

F02.login()
while True:
    if (F02.p_role == "Admin"):
        print('''
Apa yang akan kamu lakukan?
1. Sign Up User
2. Top Up Saldo
3. Upgrade akun gold
4. Menambahkan Wahana Baru
5. Mencari Pemain
6. Mencari Wahana
7. Melihat Jumlah Tiket Pemain
8. Melihat Riwayat Penggunaan Wahana
9. Melihat Kritik dan Saran
10. Melihat Best Wahana
11. Save File
12. Exit
            ''')
        pilihan = int(input("Masukkan pilihanmu: "))
        if (pilihan == 1):
            F04.signup()
        elif (pilihan == 2):
            F13.topup()
        elif (pilihan == 3):
            B02.upgrade_gold()
        elif (pilihan == 4):
            F12.tambah_wahana()
        elif (pilihan == 5):
            F05.cari_pemain()
        elif (pilihan == 6):
            F06.cari_wahana()
        elif (pilihan == 7):
            F15.tiket_pemain()
        elif (pilihan == 8):
            F14.riwayat_wahana()
        elif (pilihan == 9):
            F11.lihat_laporan()
        elif (pilihan == 10):
            B03.best_wahana()
        elif (pilihan == 11):
            F03.save()
        elif (pilihan == 12):
            F16.exit()
            print('''
-------------------------------------------------------------
Terima kasih telah berkunjung di Taman Bermain Willy Wangky!
               *NOT JUST A CHOCOLATE FACTORY*
               
              Semoga kamu benar benar senang :)

                                               -Willy Wangky
-------------------------------------------------------------
                ''')

    elif (F02.p_role == "Pemain"):
        print('''
Apa yang akan kamu lakukan?
1. Mencari Wahana
2. Membeli Tiket
3. Menggunakan Tiket
4. Refund Tiket
5. Kritik dan Saran
6. Melihat Best Wahana
7. Lapor Kehilangan Tiket
8. Save File
9. Exit
            ''')
        pilihan = int(input("Masukkan pilihanmu: "))
        if (pilihan == 1):
            F06.cari_wahana()
        elif (pilihan == 2):
            F07.beli_tiket()
        elif (pilihan == 3):
            F08.main()
        elif (pilihan == 4):
            F09.refund()
        elif (pilihan == 5):
            F10.kritik_saran()
        elif (pilihan == 6):
            B03.best_wahana()
        elif (pilihan == 7):
            B04.tiket_hilang()
        elif (pilihan == 8):
            F03.save()
        elif (pilihan == 9):
            F16.exit()
            print('''
-------------------------------------------------------------
Terima kasih telah berkunjung di Taman Bermain Willy Wangky!
               *NOT JUST A CHOCOLATE FACTORY*
               
              Semoga kamu benar benar senang :)

                                               -Willy Wangky
-------------------------------------------------------------
                ''')
