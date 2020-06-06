# F06 - Pencarian Wahana
import F01

def cari_wahana():
    Umur = "abc"
    Tinggi = "abc"

    print('''
    Jenis batasan umur:
    1. Anak-anak(<17 tahun)
    2. Dewasa (>=17 tahun)
    3. Semua umur

    Jenis batasan tinggi badan:
    1. Lebih dari 170 cm
    2. Tanpa batasan
    ''')

    batUmur = input("Batasan umur pemain: ")
    while (batUmur!='1' and batUmur!='2' and batUmur!='3'):
        print("Batasan umur tidak valid!")
        batUmur = input("Batasan umur pemain: ")

    batTinggi = input("Batasan tinggi badan: ")
    while (batTinggi!='1' and batTinggi!='2'):
        print("Batasan tinggi badan tidak valid!")
        batTinggi = input("Batasan umur pemain: ")
   
    if (batUmur == "1"):
        Umur = "Anak-anak"
    elif (batUmur == "2"):
        Umur = "Dewasa"
    else:
        Umur = "Semua Umur"
    if (batTinggi == "1"):
        Tinggi = "Lebih dari 170 cm"
    else:
        Tinggi = "Tanpa Batasan"

    found = False

    print()
    print("Hasil pencarian: ")

    # Pencarian wahana yang diminta pada data wahana
    for i in range(F01.panjang_wahana):
        while (Umur == F01.wahana_new[i][3]):
            while (Tinggi == F01.wahana_new[i][4]):
                kode = F01.wahana_new[i][0]
                nama = F01.wahana_new[i][1]
                harga = F01.wahana_new[i][2]
                print(kode,nama,harga, sep=" | ")
                found = True
                break
            break

    if (found == False):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
