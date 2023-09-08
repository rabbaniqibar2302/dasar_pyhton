print('Konversi Suhu Ruangan')
print("="*20)

cel = float(input("Nilai Celcius\t\t: "))

reamur = 4/5*cel
fare = 9/5*cel+32
kel = 273+cel

print('Nilai Reamur\t\t: %.2f'%reamur)
print('Nilai Farenheit\t\t: %.2f'%fare)
print('Nilai Kelvin\t\t: %.2f'%kel)