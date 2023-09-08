print("Menentukan Total Belanja Pupuk")
print("="*50)

# input
nama = input("Masukan Nama Pelanggan\t\t: ")
kode = int(input("Masukan Kode Pupuk\t\t: "))
jumlah = int(input("Masukan Jumlah Pembelian\t: "))
# input

if kode == 1:
    nama = "Pupuk Urea"
    harga = 800000
elif kode == 2:
    nama = "Pupuk HCL"
    harga = 550000
elif kode == 3:
    nama = "Pupuk Nabati"
    harga = 600000
elif kode == 4:
    nama = "Pupuk Buah"
    harga = 400000
else:
    exit()

# Hasil
print("Total Harga Pupuk\t\t: ")
print("Diskon Harga Pupuk\t\t: ")
print("Total bayar\t\t\t: ")
# Hasil