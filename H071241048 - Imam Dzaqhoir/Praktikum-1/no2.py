# print('=' * 25)
# print('Pencari karakter')
# print('=' * 25 + "\n")

Char = input("Masukkan karakter yang ingin dicari: ")
Text = input("Masukkan kalimat: ")

hasil = ["Tidak ditemukan dalam","Merupakan bagian dari",][Char in Text]

print(f'{Char} {hasil} "{Text}"')