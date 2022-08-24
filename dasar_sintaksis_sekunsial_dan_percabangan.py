"""
Semua sintaksis dasar bahasa pemograman terdiri dari
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensal
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_susu_botol = 173
jumlah_telur = 1587
print(f"Jumlah susu botol {jumlah_susu_botol} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_susu_botol > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 susu botol")
    else:
        print("Budi tidak jadi membeli 1 susu botol")
else:
    print("Budi tidak jadi membeli 1 susu botol")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")
