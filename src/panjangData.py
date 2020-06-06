# Fungsi untuk mencari panjang dari data

def panjangData(x):     
    Nbaris = 0
    for baris in open(x):
        Nbaris = Nbaris + 1
    return Nbaris

def panjangArray(arr):
    counter = 0
    for element in arr:
        counter += 1
    return counter
