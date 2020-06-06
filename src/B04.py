import F01

def tiket_hilang():
    global milik_new
    global hilang_new
    
    # Membaca input dari user sesuai spesifikasi
    username = input("Masukkan username: ")
    date = input("Tanggal kehilangan tiket: ")
    id = input("ID wahana: ")
    ticket_loss = int(input("Jumlah tiket yang dihilangkan: "))

    # Melakukan pengecekan ke data kepemilikan tiket
    for i in range(F01.panjang_milik):
        if (F01.milik_new[i][0] == username and F01.milik_new[i][1] == id and int(F01.milik_new[i][2]) >= ticket_loss):

            # Mengurangi data jumlah tiket yang dimiliki dengan tiket yang hilang
            # Asumsi jumlah tiket awal lebih banyak atau sama dengan jumlah tiket hilang
            F01.milik_new[i][2] = str(int(F01.milik_new[i][2]) - ticket_loss)

            # Mencatat laporan kehilangan ke file data eksternal
            for j in range(F01.panjang_hilang+1):
                if (F01.hilang_new[j][0] == '*'):
                    F01.hilang_new[j][0] = username
                    F01.hilang_new[j][1] = date
                    F01.hilang_new[j][2] = id
                    F01.hilang_new[j][3] = str(ticket_loss)
                    break

            print()
            print("Laporan kehilangan tiket Anda telah direkam.")
            break
