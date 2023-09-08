# looping for
n = int(input("Masukan Bilangan : "))

# Mencetak teks sebanyak n
for x in range(n):
    print("Saya Belajar Program Pyhton")

print("="*50)
# Penulisan for
for x in range(1,15,1): #start=1, Stop=15, Step=1
    # jika step true maka x < akhir
    # kalau tidak ada nilai step maka defaultnya 1
    # kalau hanya satu, brarti hanya stop saja
    print(x,end=" ")
    

print("="*50)
# decrement
# wajib lengkap jika ingin melakukan perhitungan mundur
for x in range(7,-2):
    print(x,end=" ")