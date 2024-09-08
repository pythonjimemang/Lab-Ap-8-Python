## KONVERSI DETIK KE FORMAT WAKTU JAM
## SOAL 3


print("\n"+"="*40)

detik = int(input("Masukkan jumlah detik : "))

jam = detik // 3600
menit = (detik % 3600) // 60
detikk = detik % 60

print(f"{jam:02} jam : {menit:02} menit :{detikk:02} detik")