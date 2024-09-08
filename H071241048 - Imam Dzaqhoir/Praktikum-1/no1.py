# print('=' * 35)
# print('Pencari rekomendasi  investasi')
# print('=' * 35 + "\n")

kemarin = float(input("Masukkan harga saham kemarin: "))
hari_ini = 105.0
output = ["Jual", "Tahan", "Beli"]

persen_baru = ((hari_ini - kemarin) / kemarin) * 100
hasil = output[(persen_baru > -3) + (persen_baru > 5)]

print(f"Perubahan persentase harga saham: {persen_baru:.2f}%")
print(f"Rekomendasi investasi: {hasil}")
