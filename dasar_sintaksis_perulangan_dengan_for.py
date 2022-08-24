"""
Program perulangan baca buku dengan for
"""
# dengan menggunakan 'for'
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print(" ")
print("Dengan for")
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1) :
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')
print(" ")

# tanpa menggunakan 'for'
print("Tanpa for")
print("Membaca buku ke-1")
print("Membaca buku ke-2")
print("Membaca buku ke-3")
print("Dst")