# F11 - Melihat Kritik dan Saran
import F01

def lihat_laporan() :
    global panjang_ks

    # Mencetak seluruh kritik dan saran yang ada di data kritiksaran
    print("Kritik dan saran: ")
    for i in range(1,F01.panjang_ks) :
        print(F01.ks_new[i][2],F01.ks_new[i][1],F01.ks_new[i][0],F01.ks_new[i][3], sep = ' | ')
