# Desicion
n = int(input('Masukan Bilangan : '))

# Menentukan jenis bilangan
if n == 0:
    print("%d Merupakan Bilangan Hampa" % n)
elif n % 2 == 0:
    print("%d Merupakan Bilangan Genap" % n)
else:
    print("%d Merupakan Bilangan Ganjil" % n)
