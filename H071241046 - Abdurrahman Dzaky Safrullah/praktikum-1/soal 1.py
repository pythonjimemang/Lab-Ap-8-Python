# REKOMENDASI STATUS SAHAM
# SOAL 1

print("\n"+"="*20)

kemarin = float(input("Harga saham kemarin : "))
sekarang = 105.0

a = {
    0 : "JUAL",
    1 : "TAHAN",
    2 : "BELI"
}

persen = ((sekarang-kemarin) / kemarin) * 100

kondisi = (persen >= -3) + (persen > 5)

rekomendasi = a[kondisi]

print("="*10)
print(f"Harga saham kemarin yaitu : {kemarin}")
print(f"Harga saham hari ini yaitu : {sekarang}")
print(f"Kenaikan : {persen:.1f}%")
print(f"Rekomendasi : {rekomendasi}")

