#inputan nilai
#menginput teks
nama=str(input("Masukkan nama siswa :"))
print("Hello....%s"%nama)

alamat=input("Masukkan Alamat Siswa :")
print("Alamat %s adalah %s dekat rumah saya"%(nama,alamat))

#menginput angka bulat
usia=int(input("Masukkan usia Siswa :"))
print("Usia %s adalah %d Tahun"%(nama,usia))

#menginput angka berkoma atau bulat
luas=float(input("Masukkan luas kuburan siswa :"))
print("Luas %s adalah %.2f di daerah %s"%(nama,luas,alamat))
