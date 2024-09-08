# print('=' * 55)
# print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
# print('=' * 55 + "\n")

c = int(input("Masukkan suhu dalam Celcius: "))

r = int(0.8 * c)
f = int(1.8 * c + 32)
k = int(c + 273.15)

print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {k}K")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Reamur adalah : {r}R")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah : {f}F")