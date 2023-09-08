print('Menentukan Jurusan Siswa')
print('-'*40)
nama = input('Masukan Nama Siswa\t\t: ')
mate = int(input('Masukan Nilai MTK\t\t: '))
fisi = int(input('Masukan Nilai Fisika\t\t: '))
bio = int(input('Masukan Nilai Biologi\t\t: '))
kim = int(input('Masukan Nilai Kimia\t\t: '))
eko = int(input('Masukan Nilai Ekonomi\t\t: '))
geo = int(input('Masukan Nilai Geografi\t\t: '))
sos = int(input('Masukan Nilai Sosialisasi\t: '))

total = mate+fisi+bio+kim+eko+geo+sos
rata = total/7
rata_mipa = (mate+fisi+bio+kim)/4
rata_ips = (mate+eko+geo+sos)/4
status = 'Baik' if rata >= 75 else "gagal"
jurusan = 'MIPA' if rata_mipa >= rata_ips else "IPS"

print('-'*40)
print('Total Nilai Keseluruhan\t: ',total)
print('Rata - Rata Nilai\t: ',rata)
print('Status Nilai\t: ',status)
print('Jurusan\t: ',jurusan)
