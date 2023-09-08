import math

print("Latihan Operator")
print("="*20)
print("Nilai A\t\t : 10")
print("Nilai B\t\t : 6")
print()
print("Hasil Perhitungan")
print("="*20)

a = 10
b = 6
tambah = a+b
kurang = a-b
kali = a*b
bagi = a/b
modulus = a%b
bagibulat = a//b
akar=math.sqrt(a)

print("%d + %d = %d" %(a,b,tambah))
print("%d - %d = %d" %(a,b,kurang))
print("%d * %d = %d" %(a,b,kali))
print("%d / %d = %d" %(a,b,bagi))
print("Akar dari %d = %.2f" %(a,akar))
print("%d %% %d = %d" %(a,b,modulus))
print("%d // %d = %.2f" %(a,b,bagibulat))