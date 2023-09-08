# Repository
repository = []
# Repository

# Menu Utama
print('Daftar Menu List:')
print('1.Create\t: Tambah Data')
print('2.Read\t\t: Lihat Data')
print('3.Update\t: Rubah Data')
print('4.Delete\t: Hapus Data')
print('5.Keluar\t: Akhiri Program')
# Menu Utama

# reload
def reload():
    query = input('Apakah anda ingin mengulang program? (ya/tidak): ')
    if query.lower() == 'ya':
        input_menu
    elif query.lower() == 'tidak':
        print('Keluar dari program.')
        exit()
    else:
        print("Menu tidak valid. Silakan pilih lagi.")
# reload

# garis
def garis():
    print('-'*10)
# garis

# Tambah Data
def create():
    count = 1
    while count <= 4:
        elemen = int(input('Masukan Elemen Ke-' + str(count) + ' = '))
        repository.append(elemen)
        count += 1
# Tambah Data

# Lihat Data
def read():
    for(item) in repository:
        print(item)
# Lihat Data

# Update Data
def update():
    print(repository)
    which = int(input('Pilih Elemen yang mau dirubah? '))
    one = int(input('Masukan Elemen yang baru = '))
    if which in repository:
        index = repository.index(which)
        repository[index] = one
# Update Data

# Delete Data
def delete():
    print(repository)
    apus = int(input('Pilih Elemen yang mau didelete? '))
    repository.remove(apus)
# Delete Data

# Looping untuk memilih menu
while True:  
    garis()
    input_menu = int(input('Pilih menu (1/2/3/4/5): '))

    if input_menu == 1:
        garis()
        print('Create : Tambah Data')
        create()  
        reload()
    elif input_menu == 2:
        garis()
        print('Read: Lihat Data')
        read()  
        reload()
    elif input_menu == 3:
        garis()
        print('Update: Rubah Data')
        update()  
        reload()
    elif input_menu == 4:
        garis()
        print('Delete: Hapus Data')
        delete()  
        reload()
    elif input_menu == 5:
        garis()
        print('Keluar dari program.')
        break
    else:
        print("Menu tidak valid. Silakan pilih lagi.")
# Looping untuk memilih menu