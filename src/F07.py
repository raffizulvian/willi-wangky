# F07 - Beli Tiket
import F01
import F02

def beli_tiket():
    global p_saldo
    global panjang_beli
    global panjang_milik
    global beli_new
    global milik_new
    global user_new
    global wahana_new
    global price

    # Membaca input dari user sesuai spesifikasi
    id = input("Masukkan ID wahana: ")
    date = input("Masukkan tanggal hari ini: ")
    ticket_ammount = int(input("Jumlah tiket yang dibeli: "))
    
    # Melakukan pengecekan ke data wahana
    for i in range(F01.panjang_wahana):
        if (F01.wahana_new[i][0] == id):
            
            if (int(F02.p_tinggi) < 170 and F01.wahana_new[i][4] == "Lebih dari 170 cm") or (int(date[6:10])-int(F02.p_lahir[6:10]) > 18 and F01.wahana_new[i][3] == "Anak-anak") or (int(date[6:10])-int(F02.p_lahir[6:10]) <= 18 and F01.wahana_new[i][3] == "Dewasa"):
                # Penggolongan Anak-anak dengan selisih tahun pembelian tiket dan tahun kelahiran <= 18
                # Penggolongan Dewasa dengan selisih tahun pembelian tiket dan tahun kelahiran > 18
                print()
                print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")

            else:
                
                # Mengambil data harga tiket wahana
                for m in range(F01.panjang_wahana):
                    if (F01.wahana_new[m][0] == id):
                        price = int(F01.wahana_new[m][2])
                        if (F02.p_status == 'yes'):
                            price = int(price/2)
                        break
                    
                # Melakukan pemotongan saldo pemain
                if (int(ticket_ammount*price) <= F02.p_saldo):
                    F02.p_saldo = F02.p_saldo - ticket_ammount*price
                    for n in range(F01.panjang_user):
                        if (F01.user_new[n][3] == F02.p_username):
                            F01.user_new[n][6] = str(F02.p_saldo)
                            break

                    # Menambahkan data pembelian tiket
                    for j in range(F01.panjang_beli+1):
                        if (F01.beli_new[j][0] == '*'):
                            F01.beli_new[j][0] = F02.p_username
                            F01.beli_new[j][1] = date
                            F01.beli_new[j][2] = id
                            F01.beli_new[j][3] = ticket_ammount
                            F01.panjang_beli += 1
                            break
                    # Menambahkan data kepemilikan tiket    
                    for k in range(F01.panjang_milik+1):
                        if (F01.milik_new[k][0] == F02.p_username and F01.milik_new[k][1] == id):
                            F01.milik_new[k][2] = str(int(F01.milik_new[k][2]) + ticket_ammount)
                            break
                        elif (F01.milik_new[k][0] == '*'):
                            F01.milik_new[k][0] = F02.p_username
                            F01.milik_new[k][1] = id
                            F01.milik_new[k][2] = ticket_ammount
                            F01.panjang_milik += 1
                            break

                    print()
                    print("Selamat bersenang-senang di " + str(F01.wahana_new[i][1]) + ".")
                    
                else:
                    print()
                    print("Saldo Anda tidak cukup\nSilakan mengisi saldo Anda")
                    
