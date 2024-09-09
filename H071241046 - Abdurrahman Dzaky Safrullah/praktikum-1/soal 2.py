### MENCARI KARAKTER DALAM KALIMAT
### SOAL 2


karakter = input("masukkan karakter : ")
kalimat = input("masukkan kalimat : ")

kondisi = {
    True: f'{karakter} ditemukan dalam "{kalimat}"',
    False: f'{karakter} tidak ditemukan dalam "{kalimat}"'
}

hasil = kondisi[karakter in kalimat]
print(hasil)

