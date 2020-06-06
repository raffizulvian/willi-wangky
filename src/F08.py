# F08 - Penggunaan Tiket
import F01
import F02

def main():
    global milik_new
    global guna_new
    global panjang_guna

    # Membaca input dari user sesuai spesifikasi
    id = input("Masukkan ID wahana: ")
    date = input("Masukkan tanggal hari ini: ")
    ticket_ammount = int(input("Jumlah tiket yang digunakan: "))
    
    isFound = False

    # Melakukan pengecekan ke data kepemilikan tiket
    for i in range(F01.panjang_milik):
        if (F01.milik_new[i][0] == F02.p_username and F01.milik_new[i][1] == id):

            # Melakukan pengurangan jumlah tiket pada data kepemilikan tiket
            if (int(F01.milik_new[i][2]) >= ticket_ammount):
                F01.milik_new[i][2] = str(int(F01.milik_new[i][2]) - ticket_ammount)

                # Menambahkan data penggunaan tiket
                for j in range(F01.panjang_guna+1):
                    if (F01.guna_new[j][0] == '*'):
                        F01.guna_new[j][0] = F02.p_username
                        F01.guna_new[j][1] = date
                        F01.guna_new[j][2] = id
                        F01.guna_new[j][3] = ticket_ammount
                        F01.panjang_guna += 1
                        break
                print()
                print("Terima kasih telah bermain.")
                isFound = True
                break

    if (isFound == False):
        print()
        print("Tiket Anda tidak valid dalam sistem kami")
