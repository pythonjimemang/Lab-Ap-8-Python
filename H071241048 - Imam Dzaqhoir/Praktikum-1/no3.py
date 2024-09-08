# print('=' * 40)
# print('Konversi detik ke jam')
# print('=' * 40 + "\n")

detik = int(input("Masukkan jumlah detik: "))

print(f"Hasil konversi = {detik // 3600:02} jam : {(detik % 3600) // 60:02} menit : {detik % 60:02} detik")


