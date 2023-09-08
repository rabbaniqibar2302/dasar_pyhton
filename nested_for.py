# nested for

n = int(input('Masukan Bilangan : '))

for baris in range(1, n+1, 1):
    for kolom in range (1, n+1, 1):
        if baris % 2 == 0 :
            print ("O", end=" ")
        else:
            print("X", end=" ")
    print()

print("="*50)

for baris in range(1, n+1, 1):
    for kolom in range (1, n+1, 1):
        if baris % 2 == 0 :
            if kolom % 2 == 0 :
                print ("X", end=" ")
            else:
                print("O", end=" ")
        else:
            if kolom % 2 == 0 :
                print ("O", end=" ")
            else:
                print("X", end=" ")
    print()