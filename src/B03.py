import panjangData as pd
import F01

def best_wahana():
    rank = [[0 for i in range(4)] for j in range(3)]
    arr = [[0 for i in range(2)] for i in range(F01.panjang_wahana)]

    # Menghitung total penjualan tiket tiap wahana
    for i in range(F01.panjang_wahana-1):
        counter = 0
        for j in range(F01.panjang_beli-1):
            if (F01.wahana_new[i+1][0] == F01.beli_new[j+1][2]):
                counter += int(F01.beli_new[j+1][3])
        arr[i][0] = F01.wahana_new[i+1][0]
        arr[i][1] = counter

    # Melakukan sorting pada wahana berdasarkan jumlah penjualan tiket
    for key in range(pd.panjangArray(arr)):
        temp = arr[key][1]
        tempgeser = arr[key]
        j = key - 1
        while (j > 0 and temp < arr[j][1]):
            arr[j+1] = arr[j]
            j -= 1
        if (temp >= arr[j][1]):
            arr[j+1] = tempgeser
        elif (j == 0):
            arr[j+1] = arr[j]
            arr[j] = tempgeser

    # Menampilkan hasil pemeringkatan untuk 3 wahana dengan penjualan tiket terbanyak
    for i in range(pd.panjangArray(rank)):
        for j in range(F01.panjang_wahana):
            rank[i][0] = 1 + i
            rank[i][1] = arr[pd.panjangArray(arr)-1-i][0]
            if (arr[pd.panjangArray(arr)-1-i][0] == F01.wahana_new[j][0]):
                rank[i][2] = F01.wahana_new[j][1]
            rank[i][3] = arr[pd.panjangArray(arr)-1-i][1]
        print(rank[i][0],rank[i][1],rank[i][2],rank[i][3], sep=' | ')
